#!/usr/bin/env python3
"""
CKS README.md Generator

Populates template with paper metadata and generates README.md for each paper

Tag         	    Strategy

<<LLM_ABSTRACT>>	LLM	Prompt: "Summarize the [MANUSCRIPT.md] in 3 paragraphs for a physicist."
<<LLM_DOMAIN_RESULTS>>	LLM	Prompt: "Extract the 3 most significant math results from [MANUSCRIPT.md]."
<<LLM_INDUSTRIAL_APP>>	LLM	Prompt: "How does the 2.0Hz sync specifically improve [DOMAIN] industry?"
<<TITLE>>	Python Scan	Extracted from H1 of the .md file.
<<REGISTRY_ID>>	Python Scan	Extracted from **Registry:** field.
<<PREREQUISITES>>	Python Scan	Extracted from dependencies in your JSON scan.
<<BIB_KEY>>	Python Scan	cks_ + domain + reg_id slug.
<<FAQS>> Frequeuntly Asked Questions
<<REPO_CONTENTS>> Load from `repo_contents.md` and insert so it stays stable
<<DOI>> DOI
<<ZENODO_DOI>> Zenedo DOI
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


def make_bib_key(registry_id):
    """Create bibtex key from registry ID"""
    # CKS-MATH-1-2026 -> cks_math_1_2026
    # return registry_id.replace('-', '_').lower()

    # Keep it the same
    return registry_id



def format_prerequisites(deps):
    """Format dependency list for README"""
    # Remove CKS-0-2026 from prerequisites (always implicit)
    filtered = [d for d in deps if d != 'CKS-0-2026']
    if not filtered:
        return 'None (foundation paper)'


    return ', '.join(filtered)


def generate_readme(paper, template):
    """Generate README.md for a single paper"""
    
    rid = paper['registry_id']
    topic = rid.split('-')[1]
    title = clean_title(paper['title'])
    abstract = paper.get('abstract', '[Abstract not available]')
    
    try:
        repo_contents = open('repo_contents.md').read()
    except Exception as e:
        raise e

    doi = paper.get('doi', '[DOI]')
    if doi != '[DOI]':
      try:
        zenodo_doi = doi.split('.')[2]
      except Exception as e:
        print(f'DOI Malformed: {paper["registry_id"]}')
        zenodo_doi = '[DOI:MALFORMED]'
    else:
        zenodo_doi = '[DOI:UNKNOWN]'
          
    

    # Basic replacements
    readme = template
    readme = readme.replace('<<TITLE>>', title)
    readme = readme.replace('<<REGISTRY_ID>>', rid)
    readme = readme.replace('<<SERIES_PATH>>', paper.get('series_path', ''))
    readme = readme.replace('<<DOI_LINK>>', doi)
    readme = readme.replace('<<DOMAIN>>', DOMAIN_NAMES.get(topic, topic))
    readme = readme.replace('<<DOMAIN_FOCUS>>', DOMAIN_NAMES.get(topic, topic))
    readme = readme.replace('<<PREREQUISITES>>', format_prerequisites(paper['dependencies']))
    readme = readme.replace('<<BIB_KEY>>', make_bib_key(rid))
    readme = readme.replace('<<LLM_ABSTRACT>>', abstract.replace('[@CKS-', '[CKS-'))
    readme = readme.replace('<<DOI>>', doi)
    readme = readme.replace('<<ZENODO_DOI>>', zenodo_doi)
    
    # LLM placeholders - leave for manual population
    readme = readme.replace('<<LLM_DOMAIN_RESULTS>>', '[To be extracted from manuscript.md]')
    readme = readme.replace('<<LLM_INDUSTRIAL_APP>>', '[To be extracted from manuscript.md]')
    readme = readme.replace('<<FAQS>>', '')
    readme = readme.replace('<<REPO_CONTENTS>>', repo_contents)
    
    
    return readme


def single():
    template = open('../../../_template/README.md').read()

    paper = json.load(open('manuscript.json'))
    rid = paper['registry_id']
    topic = rid.split('-')[1]

    # Generate and write README
    readme = generate_readme(paper, template)
    with open('README.md', 'w') as fp:
        fp.write(readme)
    
    print('Updated README.md')


if __name__ == '__main__':
    single()
    