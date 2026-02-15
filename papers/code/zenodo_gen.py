#!/usr/bin/env python3
"""
CKS zenodo.json Generator
Populates template with paper metadata and generates zenodo.json for each paper
"""

import json
import re
from pathlib import Path

# Domain mapping
DOMAIN_NAMES = {
    'MATH': 'Mathematical Foundation',
    'QM': 'Quantum Mechanics',
    'SM': 'Standard Model',
    'GR': 'General Relativity',
    'COS': 'Cosmology',
    'BIO': 'Biology & Life Sciences',
    'BODY': 'Movement & Body Mechanics',
    'COG': 'Cognition & Consciousness',
    'NEURO': 'Neuroscience',
    'SENS': 'Sensory Systems',
    'MED': 'Medical Applications',
    'AI': 'Computing & AI',
    'DWDM': 'Telecommunications & Photonics',
    'MAT': 'Materials Science',
    'SEMI': 'Semiconductors',
    'ENG': 'Engineering & Mechanics',
    'FLOW': 'Fluid Dynamics',
    'ENV': 'Environment & Infrastructure',
    'SOC': 'Social Systems',
    'LANG': 'Language & Communication',
    'DATA': 'Data & Information Theory',
    'META': 'Meta-Analysis',
    'DISC': 'Discovery Process',
    'EDU': 'Education',
    'ART': 'Art & Aesthetics',
    'TEST': 'Experimental Falsification'
}


def clean_title(title):
    """Remove embedded registry IDs from titles"""
    return re.sub(r'\[CKS-[A-Z]+-\d+-\d+\]\s*', '', title)


def generate_zenodo_json(paper, template):
    """Generate zenodo.json for a single paper"""
    
    rid = paper['registry_id']
    topic = rid.split('-')[1]
    title = clean_title(paper['title'])
    abstract = paper.get('abstract', '')
    
    # Load template as dict
    zenodo = json.loads(template)
    
    # Update fields
    zenodo['title'] = title
    zenodo['description'] = abstract if abstract else '[Description to be added]'
    zenodo['version'] = '1.0'
    zenodo['publication_date'] = '2026-02'
    
    # Update notes with registry ID and dependencies
    deps = [d for d in paper['dependencies'] if d != 'CKS-0-2026']
    dep_str = ', '.join(deps) if deps else 'CKS foundation only'
    
    zenodo['notes'] = f"CKS FRAMEWORK PAPER - Registry ID: {rid}. Dependencies: {dep_str}. This is a constituent derivation of the Cymatic K-Space Mechanics (CKS) framework extending into {DOMAIN_NAMES.get(topic, topic)}. The paper is subject to the Global Falsification Protocol [CKS-TEST-1-2026]: if the 1/32 Hz substrate quantization is absent in relevant precision measurements, this derivation is invalidated."
    
    # Keywords - domain-specific (placeholder for now)
    zenodo['keywords'] = [
        'cymatic k-space mechanics',
        'CKS framework',
        'hexagonal lattice',
        'discrete spacetime',
        DOMAIN_NAMES.get(topic, topic).lower(),
        'zero free parameters',
        'falsifiable physics',
        'substrate mechanics'
    ]
    
    # Method
    zenodo['method'] = f"Theoretical derivation from CKS axioms applied to {DOMAIN_NAMES.get(topic, topic)}. Dependencies: {dep_str}. Computational validation and empirical comparison where applicable."
    
    return zenodo


def main():
    # Load data
    papers = json.load(open('papers.json'))
    template = open('_template/zenodo.json').read()
    
    # Process each paper
    count = 0
    for paper in papers:
        rid = paper['registry_id']
        topic = rid.split('-')[1]
        
        # Create output path
        output_dir = Path('papers') / topic / rid
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate and write zenodo.json
        zenodo_data = generate_zenodo_json(paper, template)
        output_file = output_dir / 'zenodo.json'
        
        with open(output_file, 'w') as f:
            json.dump(zenodo_data, f, indent=2)
        
        print(f'Generated: {output_file}')
        count += 1
    
    print(f'\nTotal: {count} zenodo.json files generated')


if __name__ == '__main__':
    main()

