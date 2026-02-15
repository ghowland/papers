#!/usr/bin/env python3
"""
CKS description.txt Generator
Populates template with paper metadata and generates description.txt for each paper
"""

import json
import re
from pathlib import Path

# Domain mapping for cleaner output
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


def extract_title_subtitle(title):
    """Get first part of title (before colon if exists)"""
    clean = clean_title(title)
    if ':' in clean:
        return clean.split(':')[0].strip()
    return clean


def format_prerequisites(deps):
    """Format dependency list for description"""
    filtered = [d for d in deps if d != 'CKS-0-2026']
    if not filtered:
        return 'None (foundation paper)'
    return ', '.join(filtered)


def generate_description(paper, template):
    """Generate description.txt for a single paper"""
    
    rid = paper['registry_id']
    topic = rid.split('-')[1]
    title = clean_title(paper['title'])
    subtitle = extract_title_subtitle(paper['title'])
    
    # Basic replacements
    desc = template
    desc = desc.replace('<<TITLE>>', title)
    desc = desc.replace('<<TITLE_SUBTITLE>>', subtitle)
    desc = desc.replace('<<DOMAIN>>', DOMAIN_NAMES.get(topic, topic))
    desc = desc.replace('<<PREREQUISITES>>', format_prerequisites(paper['dependencies']))
    
    # LLM placeholders - leave for manual population
    desc = desc.replace('<<DOMAIN_FOCUS_STATEMENT>>', '[domain focus to be extracted]')
    desc = desc.replace('<<KEY_RESULTS>>', '[key results to be extracted from manuscript]')
    desc = desc.replace('<<DOMAIN_CONNECTION>>', '[domain connection to be extracted]')
    
    return desc


def main():
    # Load data
    papers = json.load(open('papers.json'))
    template = open('_template/description.txt').read()
    
    # Process each paper
    count = 0
    for paper in papers:
        rid = paper['registry_id']
        topic = rid.split('-')[1]
        
        # Create output path
        output_dir = Path('papers') / topic / rid
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate and write description
        description = generate_description(paper, template)
        output_file = output_dir / 'description.txt'
        output_file.write_text(description)
        
        print(f'Generated: {output_file}')
        count += 1
    
    print(f'\nTotal: {count} description.txt files generated')


if __name__ == '__main__':
    main()
