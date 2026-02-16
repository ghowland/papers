#!/usr/bin/env python3
"""
Howland Archive zenodo.json Generator
Generalized for all series and registry formats.
"""

import json
import re
from pathlib import Path

# Domain mapping for cleaner output
DOMAIN_NAMES = {
    'COMP': 'Computation',
    'INFO': 'Information',
    'SOPH': 'Philosophy',
}


def clean_title(title):
    """Remove bracketed registry IDs [ANY-ID-0-0] from titles"""
    return re.sub(r'\[[A-Z]+-[A-Z]+-\d+-\d+\]\s*', '', title)


def generate_zenodo_json(paper, template_str):
    """Generate zenodo.json for a single paper"""
    
    rid = paper['registry_id']
    parts = rid.split('-')
    prefix = parts[0]
    topic_code = parts[1] if len(parts) > 1 else "GEN"
    domain_name = DOMAIN_NAMES.get(topic_code, topic_code)
    
    title = clean_title(paper['title'])
    abstract = paper.get('abstract', '')
    
    # Load template as dict
    zenodo = json.loads(template_str)
    
    # Determine Archive Path for related identifiers
    fullpath = Path.cwd()
    path_segments = fullpath.parts[-2:] # e.g., ('MATH', '001-Logic')
    
    # Update Core Metadata
    zenodo['title'] = title
    zenodo['description'] = abstract if abstract else '[Description to be added]'
    zenodo['version'] = '1.0'
    zenodo['publication_date'] = '2026-02'
    
    # Update related identifiers (GitHub pathing)
    if 'related_identifiers' in zenodo and len(zenodo['related_identifiers']) > 0:
        rel = zenodo['related_identifiers'][0]
        rel['identifier'] = rel['identifier'].replace('<<PATH>>', '/'.join(path_segments))
    
    # Handle Dependencies logic
    root_id = f"{prefix}-0-2026"
    deps = [d for d in paper.get('dependencies', []) if d != root_id]
    dep_str = ', '.join(deps) if deps else f"{prefix} Foundation Only"
    
    # Generate Archive-specific notes
    zenodo['notes'] = (
        f"{prefix} ARCHIVE PAPER - Registry ID: {rid}.\n\n"
        f"Dependencies: {dep_str}.\n\n"
        f"This is a constituent derivation of the {prefix} framework extending into {domain_name}. "
        f"The paper is subject to the Global Falsification Protocol: if the substrate quantization "
        f"is absent in relevant precision measurements, this derivation is invalidated."
    )
    
    # Keywords - Generalized
    zenodo['keywords'] = [
        f'{prefix} framework',
        'howland archive',
        'discrete spacetime',
        domain_name.lower(),
        'zero free parameters',
        'falsifiable physics',
        'theoretical derivation'
    ]
    
    # Method
    zenodo['method'] = (
        f"Theoretical derivation from {prefix} axioms applied to {domain_name}.\n\n"
        f"Dependencies: {dep_str}.\n\n"
        f"Computational validation and empirical comparison where applicable."
    )
    
    return zenodo


def main():
    template_path = Path('../../../_template/zenodo.json')
    manuscript_path = Path('manuscript.json')

    if not template_path.exists() or not manuscript_path.exists():
        print("Error: Missing template or manuscript.json")
        return

    # Load data
    template_str = template_path.read_text()
    with open(manuscript_path) as f:
        paper = json.load(f)
    
    # Generate and write
    zenodo_data = generate_zenodo_json(paper, template_str)
    
    with open('zenodo.json', 'w') as f:
        json.dump(zenodo_data, f, indent=2)
    
    print(f"Generated zenodo.json for {paper['registry_id']}")
    

if __name__ == '__main__':
    main()
