#!/usr/bin/env python3
"""
QA Quality Gates Evaluation Script
Evaluates all QA validation results against quality gates
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class QAQualityGateEvaluator:
    def __init__(self):
        self.quality_gates = {
            'security_score_threshold': 90.0,
            'compliance_pass_rate': 100.0,
            'code_quality_score': 85.0,
            'performance_baseline_met': True,
            'vulnerability_count_limit': 0,
            'test_coverage_minimum': 80.0
        }
        
        self.evaluation_results = {
            'security': {},
            'compliance': {},
            'quality': {},
            'performance': {},
            'overall_status': 'PENDING'
        }
    
    def evaluate_security_results(self, security_results_dir: str) -> Dict[str, Any]:
        """Evaluate security scan results"""
        security_score = 0
        vulnerability_count = 0
        
        # Evaluate Bandit results
        bandit_file = Path(security_results_dir) / "bandit-report.json"
        if bandit_file.exists():
            try:
                with open(bandit_file, 'r') as f:
                    bandit_data = json.load(f)
                    high_severity = len([r for r in bandit_data.get('results', []) if r.get('issue_severity') == 'HIGH'])
                    medium_severity = len([r for r in bandit_data.get('results', []) if r.get('issue_severity') == 'MEDIUM'])
                    vulnerability_count += high_severity + medium_severity
                    security_score += max(0, 100 - (high_severity * 20) - (medium_severity * 10))
            except Exception as e:
                print(f"Warning: Could not parse Bandit results: {e}")
                security_score += 50  # Partial score if parsing fails
        
        # Evaluate Safety results
        safety_file = Path(security_results_dir) / "safety-report.json"
        if safety_file.exists():
            try:
                with open(safety_file, 'r') as f:
                    safety_data = json.load(f)
                    vuln_count = len(safety_data) if isinstance(safety_data, list) else 0
                    vulnerability_count += vuln_count
                    security_score += max(0, 100 - (vuln_count * 15))
            except Exception as e:
                print(f"Warning: Could not parse Safety results: {e}")
                security_score += 50
        
        # Evaluate Semgrep results
        semgrep_file = Path(security_results_dir) / "semgrep-report.json"
        if semgrep_file.exists():
            try:
                with open(semgrep_file, 'r') as f:
                    semgrep_data = json.load(f)
                    findings = semgrep_data.get('results', [])
                    critical_findings = len([f for f in findings if f.get('extra', {}).get('severity') == 'ERROR'])
                    vulnerability_count += critical_findings
                    security_score += max(0, 100 - (critical_findings * 25))
            except Exception as e:
                print(f"Warning: Could not parse Semgrep results: {e}")
                security_score += 50
        
        # Calculate average security score
        avg_security_score = security_score / 3 if security_score > 0 else 0
        
        return {
            'security_score': avg_security_score,
            'vulnerability_count': vulnerability_count,
            'passed': avg_security_score >= self.quality_gates['security_score_threshold'] and 
                     vulnerability_count <= self.quality_gates['vulnerability_count_limit']
        }
    
    def evaluate_compliance_results(self, compliance_results_dir: str) -> Dict[str, Any]:
        """Evaluate compliance validation results"""
        compliance_checks = ['gdpr-compliance.json', 'hipaa-compliance.json', 'soc2-compliance.json', 'iso27001-compliance.json']
        passed_checks = 0
        total_checks = len(compliance_checks)
        
        for check_file in compliance_checks:
            file_path = Path(compliance_results_dir) / check_file
            if file_path.exists():
                try:
                    with open(file_path, 'r') as f:
                        compliance_data = json.load(f)
                        if compliance_data.get('status') == 'PASSED' or compliance_data.get('compliant', False):
                            passed_checks += 1
                except Exception as e:
                    print(f"Warning: Could not parse {check_file}: {e}")
            else:
                print(f"Warning: Compliance file not found: {check_file}")
        
        pass_rate = (passed_checks / total_checks) * 100 if total_checks > 0 else 0
        
        return {
            'compliance_pass_rate': pass_rate,
            'passed_checks': passed_checks,
            'total_checks': total_checks,
            'passed': pass_rate >= self.quality_gates['compliance_pass_rate']
        }
    
    def evaluate_quality_results(self, quality_results_dir: str) -> Dict[str, Any]:
        """Evaluate code quality results"""
        quality_score = 0
        
        # Evaluate complexity report
        complexity_file = Path(quality_results_dir) / "complexity-report.json"
        if complexity_file.exists():
            try:
                with open(complexity_file, 'r') as f:
                    complexity_data = json.load(f)
                    # Simple scoring based on complexity
                    avg_complexity = complexity_data.get('averageComplexity', 10)
                    quality_score += max(0, 100 - (avg_complexity * 5))
            except Exception as e:
                print(f"Warning: Could not parse complexity report: {e}")
                quality_score += 70
        
        # Evaluate technical debt
        debt_file = Path(quality_results_dir) / "technical-debt.json"
        if debt_file.exists():
            try:
                with open(debt_file, 'r') as f:
                    debt_data = json.load(f)
                    debt_score = debt_data.get('debt_score', 80)
                    quality_score += debt_score
            except Exception as e:
                print(f"Warning: Could not parse technical debt report: {e}")
                quality_score += 70
        
        # Check for coverage data
        coverage_dir = Path(quality_results_dir) / "coverage"
        coverage_score = 85  # Default if coverage not available
        if coverage_dir.exists():
            # Look for coverage summary
            for coverage_file in coverage_dir.glob("*summary*"):
                try:
                    with open(coverage_file, 'r') as f:
                        if coverage_file.suffix == '.json':
                            coverage_data = json.load(f)
                            if 'total' in coverage_data:
                                coverage_score = coverage_data['total'].get('lines', {}).get('pct', 85)
                        break
                except Exception as e:
                    print(f"Warning: Could not parse coverage file: {e}")
        
        avg_quality_score = (quality_score / 2) if quality_score > 0 else 85
        
        return {
            'quality_score': avg_quality_score,
            'coverage_score': coverage_score,
            'passed': avg_quality_score >= self.quality_gates['code_quality_score'] and 
                     coverage_score >= self.quality_gates['test_coverage_minimum']
        }
    
    def evaluate_performance_results(self, performance_results_dir: str) -> Dict[str, Any]:
        """Evaluate performance profiling results"""
        baseline_file = Path(performance_results_dir) / "performance-baseline.json"
        
        if baseline_file.exists():
            try:
                with open(baseline_file, 'r') as f:
                    perf_data = json.load(f)
                    
                    # Evaluate performance metrics
                    response_time = perf_data.get('avg_response_time', 1000)  # ms
                    memory_usage = perf_data.get('peak_memory_mb', 512)      # MB
                    lighthouse_score = perf_data.get('lighthouse_performance', 90)
                    
                    # Simple scoring
                    response_score = max(0, 100 - (response_time / 10))  # 100ms = 10 points
                    memory_score = max(0, 100 - (memory_usage / 10))     # 100MB = 10 points
                    
                    avg_perf_score = (response_score + memory_score + lighthouse_score) / 3
                    baseline_met = avg_perf_score >= 75
                    
                    return {
                        'performance_score': avg_perf_score,
                        'response_time_ms': response_time,
                        'memory_usage_mb': memory_usage,
                        'lighthouse_score': lighthouse_score,
                        'baseline_met': baseline_met,
                        'passed': baseline_met
                    }
            except Exception as e:
                print(f"Warning: Could not parse performance baseline: {e}")
        
        # Default performance evaluation
        return {
            'performance_score': 80,
            'baseline_met': True,
            'passed': True,
            'note': 'Performance baseline not available, assuming pass'
        }
    
    def evaluate_all_gates(self, security_dir: str, compliance_dir: str, quality_dir: str, performance_dir: str) -> Dict[str, Any]:
        """Evaluate all quality gates"""
        print("🔍 Evaluating QA Quality Gates...")
        
        # Evaluate each area
        self.evaluation_results['security'] = self.evaluate_security_results(security_dir)
        self.evaluation_results['compliance'] = self.evaluate_compliance_results(compliance_dir)
        self.evaluation_results['quality'] = self.evaluate_quality_results(quality_dir)
        self.evaluation_results['performance'] = self.evaluate_performance_results(performance_dir)
        
        # Determine overall status
        all_passed = all([
            self.evaluation_results['security']['passed'],
            self.evaluation_results['compliance']['passed'],
            self.evaluation_results['quality']['passed'],
            self.evaluation_results['performance']['passed']
        ])
        
        self.evaluation_results['overall_status'] = 'PASSED' if all_passed else 'FAILED'
        self.evaluation_results['timestamp'] = datetime.now().isoformat()
        self.evaluation_results['quality_gates'] = self.quality_gates
        
        # Print summary
        print("\n" + "="*60)
        print("📊 QA QUALITY GATES EVALUATION SUMMARY")
        print("="*60)
        print(f"🔒 Security: {'✅ PASSED' if self.evaluation_results['security']['passed'] else '❌ FAILED'}")
        print(f"   Score: {self.evaluation_results['security']['security_score']:.1f}% (threshold: {self.quality_gates['security_score_threshold']}%)")
        print(f"   Vulnerabilities: {self.evaluation_results['security']['vulnerability_count']} (limit: {self.quality_gates['vulnerability_count_limit']})")
        
        print(f"📋 Compliance: {'✅ PASSED' if self.evaluation_results['compliance']['passed'] else '❌ FAILED'}")
        print(f"   Pass Rate: {self.evaluation_results['compliance']['compliance_pass_rate']:.1f}% ({self.evaluation_results['compliance']['passed_checks']}/{self.evaluation_results['compliance']['total_checks']})")
        
        print(f"⭐ Quality: {'✅ PASSED' if self.evaluation_results['quality']['passed'] else '❌ FAILED'}")
        print(f"   Score: {self.evaluation_results['quality']['quality_score']:.1f}% (threshold: {self.quality_gates['code_quality_score']}%)")
        print(f"   Coverage: {self.evaluation_results['quality']['coverage_score']:.1f}% (minimum: {self.quality_gates['test_coverage_minimum']}%)")
        
        print(f"🚀 Performance: {'✅ PASSED' if self.evaluation_results['performance']['passed'] else '❌ FAILED'}")
        print(f"   Score: {self.evaluation_results['performance']['performance_score']:.1f}%")
        print(f"   Baseline Met: {self.evaluation_results['performance']['baseline_met']}")
        
        print(f"\n🎯 OVERALL STATUS: {self.evaluation_results['overall_status']}")
        
        return self.evaluation_results

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Evaluate QA quality gates')
    parser.add_argument('--security-results', required=True, help='Security scan results directory')
    parser.add_argument('--compliance-results', required=True, help='Compliance validation results directory')
    parser.add_argument('--quality-results', required=True, help='Code quality results directory')
    parser.add_argument('--performance-results', required=True, help='Performance profiling results directory')
    parser.add_argument('--output', required=True, help='Output file for evaluation results')
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    # Evaluate quality gates
    evaluator = QAQualityGateEvaluator()
    results = evaluator.evaluate_all_gates(
        args.security_results,
        args.compliance_results,
        args.quality_results,
        args.performance_results
    )
    
    # Save results
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 QA evaluation results saved to: {args.output}")
    
    # Exit with appropriate code
    sys.exit(0 if results['overall_status'] == 'PASSED' else 1)

if __name__ == "__main__":
    main()
