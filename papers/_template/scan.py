#!/usr/bin/python3

import os
import re
import json

class CKSRegistryScanner:
    def __init__(self, directory="."):
        self.directory = directory
        # Regex to find Registry IDs like [CKS-MATH-1-2026]
        self.id_pattern = re.compile(r"\[CKS-[A-Z0-9.-]+-202[0-9]\]")
        
    def scan_file(self, filename):
        filepath = os.path.join(self.directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract basic metadata
        # Look for the first H1 for the title
        title_match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
        title = title_match.group(1) if title_match else filename

        # Extract the specific Registry ID for this file
        registry_match = re.search(r"Registry:\*\*?\s+(\[CKS-[A-Z0-9.-]+-202[0-9]\])", content)
        self_id = registry_match.group(1) if registry_match else None

        if self_id is None:
            self_id = 'CKS-0-2026'


        # Extract Series Path
        path_match = re.search(r"Series Path:\*\*?\s+(.*)", content)
        series_path = path_match.group(1) if path_match else ""

        # Extract DOI
        path_match = re.search(r"DOI:\*\*?\s+(.*)", content)
        doi = path_match.group(1) if path_match else ""

        # --- ABSTRACT EXTRACTION ---
        # Matches content starting after ## ABSTRACT until Keywords, a horizontal rule, or next H2
        abstract_pattern = re.compile(
            r"##\s+ABSTRACT\s+(.*?)(?=\*\*Keywords:\*\*|---|##)", 
            re.DOTALL | re.IGNORECASE
        )
        abstract_match = abstract_pattern.search(content)
        abstract = abstract_match.group(1).strip() if abstract_match else ""

        # Find ALL [CKS-...] references for dependency mapping
        all_refs = set(self.id_pattern.findall(content))
        
        # Remove self from dependencies if found
        if self_id in all_refs:
            all_refs.remove(self_id)

        data = {
            "file_name": filename,
            "title": title,
            "registry_id": self_id,
            "series_path": series_path,
            "doi": doi,
            "abstract": abstract,
            "dependencies": sorted(list(all_refs)),
            "raw_content_preview": content[:200].replace("\n", " ") + "..."
        }
        
        return data

    def run(self):
        # Scan for .md files
        files = [f for f in os.listdir(self.directory) if f.endswith('.md')]
        print(f"Scanning {len(files)} files in '{self.directory}'...")

        for file in files:
            # We onyly want manuscript.md, skip everything else
            if (file != 'manuscript.md'): continue

            try:
                metadata = self.scan_file(file)
                # Save to name.json
                json_name = os.path.splitext(file)[0] + ".json"
                with open(os.path.join(self.directory, json_name), 'w', encoding='utf-8') as jf:
                    json.dump(metadata, jf, indent=4)
                print(f"Successfully processed: {file} -> {json_name}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    scanner = CKSRegistryScanner()
    scanner.run()
    