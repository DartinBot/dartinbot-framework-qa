#!/usr/bin/env python3
"""
Create QA Promotion Report
Generates comprehensive report for QA stage promotion
"""

import json
import sys
from datetime import datetime
from pathlib import Path
import argparse

def create_qa_promotion_report(qa_evaluation_file: str, target_stage: str, status: str) -> dict:
    """Create comprehensive QA promotion report"""
    
    # Load QA evaluation results
    try:
        with open(qa_evaluation_file, 'r') as f:
            qa_evaluation = json.load(f)
    except Exception as e:
        print(f"❌ Error loading QA evaluation: {e}")
        qa_evaluation = {}
    
    # Create promotion report
    report = {
        "promotion_report": {
            "timestamp": datetime.now().isoformat(),
            "source_stage": "qa",
            "target_stage": target_stage,
            "promotion_status": status,
            "qa_validation_summary": qa_evaluation.get('overall_status', 'UNKNOWN'),
            "detailed_scores": {
                "security_score": qa_evaluation.get('security', {}).get('security_score', 0),
                "compliance_pass_rate": qa_evaluation.get('compliance', {}).get('compliance_pass_rate', 0),
                "quality_score": qa_evaluation.get('quality', {}).get('quality_score', 0),
                "performance_score": qa_evaluation.get('performance', {}).get('performance_score', 0)
            },
            "security_validation": {
                "vulnerability_count": qa_evaluation.get('security', {}).get('vulnerability_count', 0),
                "security_certified": qa_evaluation.get('security', {}).get('passed', False)
            },
            "compliance_validation": {
                "passed_checks": qa_evaluation.get('compliance', {}).get('passed_checks', 0),
                "total_checks": qa_evaluation.get('compliance', {}).get('total_checks', 0),
                "compliance_validated": qa_evaluation.get('compliance', {}).get('passed', False)
            },
            "next_stage_requirements": {
                "ultra_strict_validation": True,
                "accuracy_threshold": 99.9999,
                "comprehensive_testing": True,
                "performance_benchmarking": True,
                "security_certification_required": True
            }
        },
        "promotion_metadata": {
            "pipeline_version": "3.0.0",
            "qa_stage_version": "2.0.0",
            "validation_framework": "DartinBot Enterprise QA",
            "promotion_automation": True,
            "quality_gates_enforced": True
        }
    }
    
    # Add recommendation based on status
    if status == "PASSED":
        report["promotion_report"]["recommendation"] = "APPROVED - All QA quality gates passed, ready for Testing stage"
        report["promotion_report"]["action_taken"] = "Automatic promotion to Testing stage initiated"
    else:
        report["promotion_report"]["recommendation"] = "REJECTED - QA quality gates failed, requires remediation"
        report["promotion_report"]["action_taken"] = "Promotion blocked, manual review required"
    
    return report

def main():
    parser = argparse.ArgumentParser(description='Create QA promotion report')
    parser.add_argument('--qa-evaluation', required=True, help='QA evaluation results file')
    parser.add_argument('--target', required=True, help='Target stage for promotion')
    parser.add_argument('--status', required=True, help='Promotion status (PASSED/FAILED)')
    
    args = parser.parse_args()
    
    # Ensure reports directory exists
    Path('reports').mkdir(exist_ok=True)
    
    # Create promotion report
    report = create_qa_promotion_report(args.qa_evaluation, args.target, args.status)
    
    # Save report
    report_file = 'reports/qa-promotion-report.json'
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print("📊 QA PROMOTION REPORT CREATED")
    print("="*40)
    print(f"🎯 Status: {args.status}")
    print(f"📂 Target Stage: {args.target}")
    print(f"📄 Report saved: {report_file}")
    
    if args.status == "PASSED":
        print("✅ Recommendation: APPROVED for promotion")
    else:
        print("❌ Recommendation: REJECTED - requires remediation")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
