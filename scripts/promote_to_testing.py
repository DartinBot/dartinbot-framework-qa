#!/usr/bin/env python3
"""
Template Promotion to Testing Stage
Promotes validated templates from QA to Testing repository
"""

import json
import os
import shutil
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class TestingPromoter:
    def __init__(self):
        self.promotion_metadata = {
            'promotion_timestamp': datetime.now().isoformat(),
            'source_stage': 'qa',
            'target_stage': 'testing',
            'promoted_templates': [],
            'qa_validation_summary': {}
        }
    
    def copy_template_with_metadata(self, source_path: Path, target_path: Path, qa_results: Dict[str, Any]) -> bool:
        """Copy template file and enhance metadata with QA results"""
        try:
            # Ensure target directory exists
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy the template file
            shutil.copy2(source_path, target_path)
            
            # Create/update metadata file
            metadata_file = target_path.with_suffix('.json')
            metadata = {
                'template_name': source_path.stem,
                'original_file': str(source_path),
                'promoted_from': 'qa',
                'promotion_timestamp': self.promotion_metadata['promotion_timestamp'],
                'qa_validation': {
                    'security_score': qa_results.get('security', {}).get('security_score', 0),
                    'compliance_pass_rate': qa_results.get('compliance', {}).get('compliance_pass_rate', 0),
                    'quality_score': qa_results.get('quality', {}).get('quality_score', 0),
                    'performance_score': qa_results.get('performance', {}).get('performance_score', 0),
                    'overall_status': qa_results.get('overall_status', 'UNKNOWN')
                },
                'testing_stage_requirements': {
                    'ultra_strict_validation': True,
                    'accuracy_threshold': 99.9999,
                    'comprehensive_testing': True,
                    'performance_benchmarking': True
                }
            }
            
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"❌ Error copying template {source_path}: {e}")
            return False
    
    def promote_templates(self, source_dir: str, target_dir: str, qa_results_file: str) -> bool:
        """Promote all validated templates to testing stage"""
        source_path = Path(source_dir)
        target_path = Path(target_dir)
        
        # Load QA results
        try:
            with open(qa_results_file, 'r') as f:
                qa_results = json.load(f)
        except Exception as e:
            print(f"❌ Error loading QA results: {e}")
            return False
        
        # Only promote if QA validation passed
        if qa_results.get('overall_status') != 'PASSED':
            print(f"❌ Cannot promote: QA validation status is {qa_results.get('overall_status')}")
            return False
        
        print(f"🚀 Promoting templates from QA to Testing...")
        print(f"📂 Source: {source_dir}")
        print(f"📂 Target: {target_dir}")
        
        # Find all template files
        template_files = list(source_path.glob("**/*.md"))
        
        if not template_files:
            print("⚠️ No template files found in source directory")
            return False
        
        promoted_count = 0
        for template_file in template_files:
            # Calculate relative path to preserve directory structure
            rel_path = template_file.relative_to(source_path)
            target_file = target_path / rel_path
            
            if self.copy_template_with_metadata(template_file, target_file, qa_results):
                promoted_count += 1
                self.promotion_metadata['promoted_templates'].append({
                    'name': template_file.stem,
                    'source_path': str(template_file),
                    'target_path': str(target_file),
                    'size_bytes': template_file.stat().st_size
                })
                print(f"✅ Promoted: {template_file.name}")
            else:
                print(f"❌ Failed to promote: {template_file.name}")
        
        # Save promotion summary
        self.promotion_metadata['qa_validation_summary'] = qa_results
        self.promotion_metadata['total_templates'] = len(template_files)
        self.promotion_metadata['successfully_promoted'] = promoted_count
        
        summary_file = target_path / "promotion_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(self.promotion_metadata, f, indent=2)
        
        print(f"\n📊 Promotion Summary:")
        print(f"   Total templates: {len(template_files)}")
        print(f"   Successfully promoted: {promoted_count}")
        print(f"   Success rate: {(promoted_count/len(template_files)*100):.1f}%")
        print(f"   Promotion summary saved: {summary_file}")
        
        return promoted_count == len(template_files)
    
    def create_testing_readme(self, target_dir: str):
        """Create README for testing stage"""
        readme_content = f"""# DartinBot Templates - Testing Stage

## Promotion Information
- **Promoted from**: QA Stage
- **Promotion date**: {self.promotion_metadata['promotion_timestamp']}
- **Templates promoted**: {self.promotion_metadata.get('successfully_promoted', 0)}

## Testing Stage Requirements
- ✅ QA validation passed
- 🎯 Ultra-strict validation (99.9999% accuracy)
- 🧪 Comprehensive testing required
- 📊 Performance benchmarking active
- 🔒 Security validation completed

## Next Stage
Upon successful testing validation, templates will be promoted to:
- **Pre-Production Stage** for final staging validation

## Validation Status
All templates in this directory have passed QA validation with the following scores:
- Security: {self.promotion_metadata.get('qa_validation_summary', {}).get('security', {}).get('security_score', 'N/A')}%
- Compliance: {self.promotion_metadata.get('qa_validation_summary', {}).get('compliance', {}).get('compliance_pass_rate', 'N/A')}%
- Quality: {self.promotion_metadata.get('qa_validation_summary', {}).get('quality', {}).get('quality_score', 'N/A')}%
- Performance: {self.promotion_metadata.get('qa_validation_summary', {}).get('performance', {}).get('performance_score', 'N/A')}%

## Directory Structure
```
testing-templates/
├── promotion_summary.json    # Promotion metadata
├── README.md                # This file
└── [template-files]         # Promoted templates with metadata
```
"""
        
        readme_path = Path(target_dir) / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        print(f"📝 Testing stage README created: {readme_path}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Promote templates from QA to Testing')
    parser.add_argument('--source-dir', required=True, help='QA templates directory')
    parser.add_argument('--target-dir', required=True, help='Testing templates directory')
    parser.add_argument('--qa-results', required=True, help='QA evaluation results file')
    
    args = parser.parse_args()
    
    promoter = TestingPromoter()
    
    # Promote templates
    success = promoter.promote_templates(args.source_dir, args.target_dir, args.qa_results)
    
    if success:
        # Create testing stage README
        promoter.create_testing_readme(args.target_dir)
        print("🎉 All templates successfully promoted to Testing stage!")
        sys.exit(0)
    else:
        print("❌ Template promotion failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
