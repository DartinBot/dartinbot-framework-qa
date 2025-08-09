#!/usr/bin/env python3
"""
QA Gate Status Checker
Checks the status of QA quality gates evaluation
"""

import json
import sys
import argparse
from pathlib import Path

def check_qa_gate_status(evaluation_file: str) -> str:
    """Check QA gate status from evaluation file"""
    
    if not Path(evaluation_file).exists():
        print(f"❌ Evaluation file not found: {evaluation_file}")
        return "FAILED"
    
    try:
        with open(evaluation_file, 'r') as f:
            evaluation_data = json.load(f)
        
        overall_status = evaluation_data.get('overall_status', 'FAILED')
        
        # Print detailed status
        print("📊 QA Quality Gate Status Check")
        print("="*40)
        
        if 'security' in evaluation_data:
            sec_status = "✅" if evaluation_data['security']['passed'] else "❌"
            print(f"{sec_status} Security: {evaluation_data['security'].get('security_score', 0):.1f}%")
        
        if 'compliance' in evaluation_data:
            comp_status = "✅" if evaluation_data['compliance']['passed'] else "❌"
            print(f"{comp_status} Compliance: {evaluation_data['compliance'].get('compliance_pass_rate', 0):.1f}%")
        
        if 'quality' in evaluation_data:
            qual_status = "✅" if evaluation_data['quality']['passed'] else "❌"
            print(f"{qual_status} Quality: {evaluation_data['quality'].get('quality_score', 0):.1f}%")
        
        if 'performance' in evaluation_data:
            perf_status = "✅" if evaluation_data['performance']['passed'] else "❌"
            print(f"{perf_status} Performance: {evaluation_data['performance'].get('performance_score', 0):.1f}%")
        
        print(f"\n🎯 Overall Status: {overall_status}")
        
        return overall_status
        
    except Exception as e:
        print(f"❌ Error reading evaluation file: {e}")
        return "FAILED"

def main():
    parser = argparse.ArgumentParser(description='Check QA gate status')
    parser.add_argument('--evaluation-file', required=True, help='QA evaluation results file')
    
    args = parser.parse_args()
    
    status = check_qa_gate_status(args.evaluation_file)
    print(status)  # Output for shell script capture
    
    # Exit with appropriate code
    sys.exit(0 if status == "PASSED" else 1)

if __name__ == "__main__":
    main()
