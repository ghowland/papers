#!/usr/bin/env python3
"""
audit_papers.py - HOWL Paper Repository Auditor

Scans papers/ directory, extracts metadata from manuscript.md files,
generates papers.json and report.md.

Usage:
    python3 audit_papers.py [--papers-dir PATH]
"""

import json
import re
import os
import shutil
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict


class PaperMetadata:
    """Extract metadata from single manuscript.md"""
    
    def __init__(self, manuscript_path):
        self.path = manuscript_path
        self.raw_content = manuscript_path.read_text(encoding='utf-8')
        
        # Parse path first (ground truth)
        self.path_info = self._parse_path()
        
        # Extract content metadata
        self.frontmatter = self._extract_frontmatter()
        self.title = self._extract_title()
        self.key_result = self._extract_keyresult()
        self.skip = self._extract_skip()
        self.subtitle = self._extract_subtitle()
        self.doi_info = self._extract_doi()
        self.abstract = self._extract_abstract()
        self.dependencies = self._extract_dependencies()
        self.validation = self._validate()
    
    def _parse_path(self):
        """Extract metadata from path: papers/SUBJECT/HOWL-SUBJECT-NUMBER-YEAR/manuscript.md"""
        parts = self.path.parts
        
        # Find papers/ index
        papers_idx = -1
        for i, part in enumerate(parts):
            if part == 'papers':
                papers_idx = i
                break
        
        if papers_idx == -1:
            return {'error': 'Path does not contain papers/ directory'}
        
        # Extract components
        if papers_idx + 2 >= len(parts):
            return {'error': 'Path too short'}
        
        paper_dir = parts[papers_idx + 2]  # HOWL-SUBJECT-NUMBER-YEAR
        subject_dir = parts[papers_idx + 1]  # SUBJECT
        
        # Parse paper_dir: HOWL-{SUBJECT}-{NUMBER}-{YEAR}
        match = re.match(r'HOWL-([A-Z]+)-([\dX]+)-(\d{4})', paper_dir)
        
        if not match:
            return {
                'error': 'Invalid paper directory format: {}'.format(paper_dir),
                'paper_id': paper_dir,
                'subject_dir': subject_dir
            }
        
        subject_id = match.group(1)
        number_str = match.group(2)
        year = int(match.group(3))
        
        # Check if number is placeholder
        is_placeholder = 'X' in number_str
        number = None if is_placeholder else int(number_str)
        
        return {
            'paper_id': paper_dir,
            'subject': subject_id,
            'number': number,
            'year': year,
            'is_placeholder': is_placeholder,
            'subject_dir': subject_dir
        }
    
    def _extract_frontmatter(self):
        """Extract all **Field:** value pairs before first ---"""
        frontmatter = {}
        
        lines = self.raw_content.split('\n')
        frontmatter_lines = []
        
        in_frontmatter = False
        for line in lines:
            # Start after title/subtitle headers
            if line.startswith('# ') or line.startswith('## ') or line.startswith('### '):
                in_frontmatter = True
                continue
            
            if in_frontmatter:
                if line.strip() == '---':
                    break
                frontmatter_lines.append(line)
        
        frontmatter_text = '\n'.join(frontmatter_lines)
        
        # Extract **Field:** value patterns
        pattern = r'\*\*([^:]+):\*\*\s*(.+?)(?=\n\*\*|\n\n|\Z)'
        
        for match in re.finditer(pattern, frontmatter_text, re.DOTALL):
            field = match.group(1).strip()
            value = match.group(2).strip()
            frontmatter[field] = value
        
        return frontmatter
    
    def _extract_title(self):
        """Extract first H1 line"""
        match = re.search(r'^#\s+(.+)$', self.raw_content, re.MULTILINE)
        return match.group(1).strip() if match else None
    
    def _extract_skip(self):
        """Extract first H1 line"""
        match = re.search(r'^\*\*Skip:\*\*\s+(.+)$', self.raw_content, re.MULTILINE)
        return match.group(1).strip() if match != None else False
    
    def _extract_keyresult(self):
        """Extract first H1 line"""
        match = re.search(r'^\*\*Key Result:\*\*\s+(.+)$', self.raw_content, re.MULTILINE)
        value = match.group(1).strip() if match else None

        if value == None:
            match = re.search(r'^\*\*Revolutionary claim:\*\*\s+(.+)$', self.raw_content, re.MULTILINE)
            value = match.group(1).strip() if match else None

        return value
    
    def _extract_subtitle(self):
        """Extract H2 immediately after H1"""
        lines = self.raw_content.split('\n')
        found_h1 = False
        
        for line in lines:
            if line.startswith('# '):
                found_h1 = True
                continue
            
            if found_h1:
                if line.startswith('## '):
                    return line[3:].strip()
                elif line.strip():
                    return None
        
        return None
    
    def _extract_doi(self):
        """Parse DOI field and detect stub"""
        doi_raw = self.frontmatter.get('DOI', '').strip()
        
        if not doi_raw:
            return {
                'raw': '',
                'is_stub': True,
                'zenodo_id': None,
                'status': 'missing'
            }
        
        # Check for .zzz stub
        if '.zzz' in doi_raw.lower():
            return {
                'raw': doi_raw,
                'is_stub': True,
                'zenodo_id': None,
                'status': 'draft'
            }
        
        # Extract Zenodo ID: 10.5281/zenodo.NNNNNN
        match = re.search(r'10\.5281/zenodo\.(\d+)', doi_raw)
        if match:
            return {
                'raw': doi_raw,
                'is_stub': False,
                'zenodo_id': match.group(1),
                'status': 'published'
            }
        
        # Unknown DOI format
        return {
            'raw': doi_raw,
            'is_stub': False,
            'zenodo_id': None,
            'status': 'unknown'
        }
    
    def _extract_abstract(self):
        """Try multiple abstract patterns (case-insensitive)"""
        patterns = [
            r'##\s+executive\s+abstract',
            r'##\s+executive\s+summary',
            r'##\s+abstract',
            r'##\s+summary',
            # r'##\s+operational\s+declaration',
        ]
        
        for pattern in patterns:
            match = re.search(
                r'{}\s+(.*?)(?=\n##|\Z)'.format(pattern),
                self.raw_content,
                re.DOTALL | re.IGNORECASE
            )
            if match:
                abstract_text = match.group(1).strip()
                abstract_text = re.sub(r'^-+\s*', '', abstract_text)
                abstract_text = re.sub(r'\s*-+$', '', abstract_text)
                return abstract_text.strip()
        
        return None
    
    def _extract_dependencies(self):
        """Extract all [@HOWL-...] citations from content, excluding self"""
        citations = set()
        pattern = r'\[@(HOWL-[A-Z]+-[\dX]+-\d{4})\]'
        
        for match in re.finditer(pattern, self.raw_content):
            cited_id = match.group(1)
            if cited_id != self.path_info.get('paper_id'):
                citations.add(cited_id)
        
        return sorted(list(citations))
    
    def _validate(self):
        """Validate content against path and check required fields"""
        errors = []
        warnings = []
        
        # Check path parsing
        if 'error' in self.path_info:
            errors.append(self.path_info['error'])
        
        # Check required fields
        if not self.title:
            errors.append('Missing title (H1)')
        
        if not self.frontmatter.get('Registry'):
            errors.append('Missing Registry field in frontmatter')
        
        # Validate registry ID matches path
        registry_raw = self.frontmatter.get('Registry', '')
        registry_match = re.search(r'\[@(HOWL-[A-Z]+-[\dX]+-\d{4})\]', registry_raw)
        
        if registry_match:
            registry_id = registry_match.group(1)
            if registry_id != self.path_info.get('paper_id'):
                warnings.append(
                    'Registry mismatch: path={}, content={}'.format(
                        self.path_info.get('paper_id'),
                        registry_id
                    )
                )
            
            if 'X' in registry_id:
                warnings.append('Registry ID is placeholder (contains X)')
        
        # Check for DOI stub
        if self.doi_info['is_stub']:
            if self.doi_info['status'] == 'draft':
                warnings.append('DOI is stub (.zzz)')
            elif self.doi_info['status'] == 'missing':
                warnings.append('DOI is missing')
        
        # Check for References section
        if not re.search(r'##\s+references', self.raw_content, re.IGNORECASE):
            warnings.append('Missing ## References section')
        
        # Check for bibliography delimiter
        if '::: {#refs}' not in self.raw_content:
            warnings.append('Missing ::: {#refs} ::: delimiter')
        
        # Check abstract
        if not self.abstract:
            warnings.append('No abstract section found')
        
        return {
            'is_valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        try:
            relative_path = str(self.path.relative_to(Path.cwd()))
        except ValueError:
            relative_path = str(self.path)
        
        return {
            'file_path': relative_path,
            'paper_id': self.path_info.get('paper_id'),
            'subject': self.path_info.get('subject'),
            'number': self.path_info.get('number'),
            'year': self.path_info.get('year'),
            'title': self.title,
            'key_result': self.key_result,
            'skip': self.skip,
            'subtitle': self.subtitle,
            'doi': self.doi_info,
            'frontmatter': self.frontmatter,
            'abstract': self.abstract,
            'dependencies': self.dependencies,
            'validation': self.validation,
            'extracted_at': datetime.now(timezone.utc).isoformat()
        }


class PapersAuditor:
    """Scan papers/ directory and generate outputs"""
    
    def __init__(self, papers_dir):
        self.papers_dir = Path(papers_dir)
        self.papers = []
        self.stats = defaultdict(int)
    
    def scan(self):
        """Scan all manuscript.md files in papers/ directory"""
        print('Scanning {}/ for papers...'.format(self.papers_dir))
        
        manuscript_files = sorted(self.papers_dir.rglob('manuscript.md'))
        
        for manuscript_path in manuscript_files:
            # try:
            if 1:
                paper = PaperMetadata(manuscript_path)
                self.papers.append(paper)

                self.stats['total'] += 1
                
                if paper.validation['is_valid']:
                    self.stats['valid'] += 1
                else:
                    self.stats['invalid'] += 1
                
                self.stats['errors'] += len(paper.validation['errors'])
                self.stats['warnings'] += len(paper.validation['warnings'])
                
                # Count by subject
                subject = paper.path_info.get('subject', 'UNKNOWN')
                self.stats['subject_{}'.format(subject)] += 1
                
                # Count by status
                if paper.doi_info['is_stub']:
                    self.stats['draft'] += 1
    
                    manuscript_path_original = str(manuscript_path).replace('.md', '_orig.md')
                    if (not os.path.exists(manuscript_path_original)):
                        print(f'Manu Path Stub Original Missing: {manuscript_path_original}')
                        shutil.copy2(str(manuscript_path), manuscript_path_original)
                        
                else:
                    self.stats['published'] += 1
                
            # except Exception as e:
            #     print('ERROR processing {}: {}'.format(manuscript_path, e))
            #     self.stats['scan_errors'] += 1
        
        print('Found {} papers'.format(self.stats['total']))
        print('  Valid: {}, Invalid: {}'.format(self.stats['valid'], self.stats['invalid']))
        print('  Errors: {}, Warnings: {}'.format(self.stats['errors'], self.stats['warnings']))
    
    def write_json(self, output_path):
        """Write papers.json (destructive)"""
        papers_data = [paper.to_dict() for paper in self.papers]
        
        with open(str(output_path), 'w', encoding='utf-8') as f:
            json.dump(papers_data, f, indent=2, ensure_ascii=False)
        
        print('\nWrote {} ({} papers)'.format(output_path, len(papers_data)))
    
    def write_report(self, output_path):
        """Write report.md with statistics"""
        lines = [
            '# HOWL Papers Audit Report',
            '',
            '**Generated:** {}'.format(datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')),
            '',
            '## Summary',
            '',
            '- **Total Papers:** {}'.format(self.stats['total']),
            '- **Valid:** {}'.format(self.stats['valid']),
            '- **Invalid:** {}'.format(self.stats['invalid']),
            '- **Total Errors:** {}'.format(self.stats['errors']),
            '- **Total Warnings:** {}'.format(self.stats['warnings']),
            '',
            '## By Subject',
            ''
        ]
        
        # Subject breakdown
        subjects = sorted([k.replace('subject_', '') for k in self.stats.keys() if k.startswith('subject_')])
        for subject in subjects:
            count = self.stats['subject_{}'.format(subject)]
            lines.append('- **{}:** {} papers'.format(subject, count))
        
        lines.extend([
            '',
            '## By Status',
            '',
            '- **Published (has DOI):** {}'.format(self.stats['published']),
            '- **Draft (stub .zzz):** {}'.format(self.stats['draft']),
            '',
            '## Validation Issues',
            ''
        ])
        
        # List papers with errors
        papers_with_errors = [p for p in self.papers if not p.validation['is_valid']]
        if papers_with_errors:
            lines.append('### Papers with Errors')
            lines.append('')
            for paper in papers_with_errors:
                lines.append('**{}**'.format(paper.path_info.get('paper_id')))
                for error in paper.validation['errors']:
                    lines.append('  - ❌ {}'.format(error))
                lines.append('')
        else:
            lines.append('✓ No papers with errors')
        
        # List papers with warnings (limit output)
        papers_with_warnings = [p for p in self.papers if p.validation['warnings']]
        if papers_with_warnings:
            lines.append('')
            lines.append('### Papers with Warnings ({} total)'.format(len(papers_with_warnings)))
            lines.append('')
            
            # Show first 10 papers with warnings
            for paper in papers_with_warnings[:10]:
                lines.append('**{}**'.format(paper.path_info.get('paper_id')))
                for warning in paper.validation['warnings'][:3]:
                    lines.append('  - ⚠️  {}'.format(warning))
                if len(paper.validation['warnings']) > 3:
                    lines.append('  - ... and {} more'.format(len(paper.validation['warnings']) - 3))
                lines.append('')
            
            if len(papers_with_warnings) > 10:
                lines.append('... and {} more papers with warnings'.format(len(papers_with_warnings) - 10))
        
        report_text = '\n'.join(lines)
        
        with open(str(output_path), 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        print('Wrote {}'.format(output_path))


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Audit HOWL papers repository')
    parser.add_argument('--papers-dir', type=str, default='papers',
                        help='Path to papers/ directory (default: ./papers)')
    
    args = parser.parse_args()
    
    auditor = PapersAuditor(args.papers_dir)
    auditor.scan()
    auditor.write_json(Path('papers.json'))
    auditor.write_report(Path('report.md'))
    
    print('\n✓ Audit complete')


if __name__ == '__main__':
    main()
