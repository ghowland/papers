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
    
    # Path
    fullpath = Path.cwd()
    path = fullpath.parts[-2:]

    # Update fields
    zenodo['title'] = title
    zenodo['description'] = abstract if abstract else '[Description to be added]'
    zenodo['version'] = '1.0'
    zenodo['publication_date'] = '2026-02'
    zenodo['related_identifiers'][0]['identifier'] = zenodo['related_identifiers'][0]['identifier'].replace('<<PATH>>', '/'.join(path))
    
    # Update notes with registry ID and dependencies
    deps = [d for d in paper['dependencies'] if d != 'CKS-0-2026']
    dep_str = ', '.join(deps) if deps else 'CKS foundation only'
    
    zenodo['notes'] = f"CKS FRAMEWORK PAPER - Registry ID: {rid}.\n\nDependencies: {dep_str}.\n\nThis is a constituent derivation of the Cymatic K-Space Mechanics (CKS) framework extending into {DOMAIN_NAMES.get(topic, topic)}. The paper is subject to the Global Falsification Protocol [CKS-TEST-1-2026]: if the 1/32 Hz substrate quantization is absent in relevant precision measurements, this derivation is invalidated."
    
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
    zenodo['method'] = f"Theoretical derivation from CKS axioms applied to {DOMAIN_NAMES.get(topic, topic)}.\n\nDependencies: {dep_str}.\n\nComputational validation and empirical comparison where applicable."
    
    return zenodo


def main():
    # Load data
    template = open('../../../_template/zenodo.json').read()
    
    # Process each paper
    paper = json.load(open('manuscript.json'))

    rid = paper['registry_id']
    topic = rid.split('-')[1]
    
    # Generate and write zenodo.json
    zenodo_data = generate_zenodo_json(paper, template)
    output_file = 'zenodo.json'
    
    with open(output_file, 'w') as f:
        json.dump(zenodo_data, f, indent=2)
    
    print(f'Generated: {output_file}')
    

if __name__ == '__main__':
    main()

