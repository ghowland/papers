#!/usr/bin/env python3
"""
Howland Archive README.md Generator
Generalized for all series and registry formats.
"""

import json
import re
from pathlib import Path

# Domain mapping for cleaner output (Shared across the Archive)
DOMAIN_NAMES = {
    'COMP': 'Computation',
    'INFO': 'Information',
    'SOPH': 'Philosophy',
}


def clean_title(title):
    """Remove bracketed registry IDs [ANY-ID-000] from titles"""
    return re.sub(r'\[[A-Z]+-[A-Z]+-\d+-\d+\]\s*', '', title)


def format_prerequisites(deps, registry_id):
    """Format dependency list, removing self-referential or root foundations"""
    # Split the ID to find the prefix (e.g., 'CKS' or 'HOWL')
    prefix = registry_id.split('-')[0]
    root_id = f"{prefix}-0-2026"
    
    filtered = [d for d in deps if d != root_id]
    if not filtered:
        return 'None (foundation paper)'

    return ', '.join(filtered)


def generate_readme(paper, template):
    """Generate README.md for a single paper"""
    
    rid = paper['registry_id']
    # Supports CKS-MATH-... or HOWL-PHYS-...
    parts = rid.split('-')
    topic = parts[1] if len(parts) > 1 else "GENERAL"
    
    title = clean_title(paper['title'])
    abstract = paper.get('abstract', '[Abstract not available]')
    
    # Load stable repo contents if file exists
    try:
        repo_contents = open('repo_contents.md').read()
    except FileNotFoundError:
        repo_contents = "File `repo_contents.md` not found."

    doi = paper.get('doi', '[DOI]')
    zenodo_doi = '[DOI:UNKNOWN]'
    
    if doi != '[DOI]' and '.' in doi:
        try:
            # Extract suffix from DOI string
            zenodo_doi = doi.split('.')[-1]
        except Exception:
            print(f'DOI Suffix Extraction Failed: {rid}')
          
    # Replacement Mapping
    replacements = {
        '<<TITLE>>': title,
        '<<REGISTRY_ID>>': rid,
        '<<SERIES_PATH>>': paper.get('series_path', ''),
        '<<DOI_LINK>>': doi,
        '<<DOMAIN>>': DOMAIN_NAMES.get(topic, topic),
        '<<DOMAIN_FOCUS>>': DOMAIN_NAMES.get(topic, topic),
        '<<PREREQUISITES>>': format_prerequisites(paper['dependencies'], rid),
        '<<BIB_KEY>>': rid, # Keep key same as ID for consistency
        '<<LLM_ABSTRACT>>': abstract,
        '<<DOI>>': doi,
        '<<ZENODO_DOI>>': zenodo_doi,
        '<<REPO_CONTENTS>>': repo_contents,
        '<<LLM_DOMAIN_RESULTS>>': '[To be extracted from manuscript.md]',
        '<<LLM_INDUSTRIAL_APP>>': '[To be extracted from manuscript.md]',
        '<<FAQS>>': ''
    }

    readme = template
    for key, value in replacements.items():
        readme = readme.replace(key, str(value))
    
    return readme


def single():
    # Relative path to template remains standard in the archive structure
    template_path = Path('../../../_template/README.md')
    if not template_path.exists():
        print(f"Error: Template not found at {template_path}")
        return

    template = template_path.read_text()

    if not Path('manuscript.json').exists():
        print("Error: manuscript.json not found in current directory.")
        return

    with open('manuscript.json') as f:
        paper = json.load(f)

    # Generate and write README
    readme = generate_readme(paper, template)
    with open('README.md', 'w') as fp:
        fp.write(readme)
    
    print(f"Updated README.md for {paper['registry_id']}")


if __name__ == '__main__':
    single()
