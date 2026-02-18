import json
import os
import shutil

# def generate_bib_entry(manuscript_data, folder_id):
#     """
#     Creates a BibTeX entry. Prefers the registry_id from JSON, 
#     but falls back to folder name if JSON contains placeholders.
#     """
#     # Use the folder name as the source of truth if JSON is generic
#     full_id = manuscript_data.get("registry_id", "").strip("[]")
#     if full_id == "CKS-0-2026" and folder_id.startswith("CKS-"):
#         full_id = folder_id

#     long_title = manuscript_data.get("title", "Untitled CKS Paper")
#     parts = full_id.split('-')
    
#     # Pattern CKS-0-2026 (3 parts) -> _CKS
#     # Pattern CKS-MATH-0-2026 (4 parts) -> MATH
#     if len(parts) == 3:
#         topic_folder = "_CKS"
#         year = parts[2]
#     elif len(parts) >= 4:
#         topic_folder = parts[1]
#         year = parts[3]
#     else:
#         topic_folder = "UNKNOWN"
#         year = "2026"

#     github_url = f"https://github.com/ghowland/papers/tree/main/papers/{topic_folder}/{full_id}"
    
#     # BibTeX Mapping:
#     # 1. Double braces protect exact casing.
#     # 2. publisher contains the ID for the pass-through CSL.
#     entry = f"""@article{{{full_id},
#   author = {{Howland, Geoffrey}},
#   title = {{{{{long_title}}}}},
#   publisher = {{{{{full_id}}}}},
#   year = {{{year}}},
#   url = {{https://zenodo.org/record/YOUR_ID_HERE}},
#   note = {{Github: {github_url} }}
# }}
# """
#     return (full_id, entry)

def generate_bib_entry(manuscript_data, folder_id):
    # Use folder name to get the correct unique ID
    full_id = folder_id.strip("[]")
    long_title = manuscript_data.get("title", "Untitled CKS Paper")
    
    parts = full_id.split('-')
    if len(parts) == 3:
        topic_folder = "_CKS"
        year = parts[2]
    else:
        topic_folder = parts[1]
        year = parts[3]

    github_url = f"https://github.com/ghowland/papers/tree/main/papers/{topic_folder}/{full_id}"

    doi = manuscript_data.get('doi', '[DOI]')
    try:
      zenodo_record = doi.split('.')[2]
    except Exception as e:
      zenodo_record = '[DOI-MALFORMED]'

      # if topic_folder == "_CKS":
      print(f'    DOI Failed: {full_id}: {e}: {doi}')
      # print(f'    DOI Failed: {full_id}: {e}: {doi}: {manuscript_data}')

    # CRITICAL CHANGE:
    # 1. 'title' now contains ONLY the CKS-ID.
    # 2. 'note' now contains the Full Descriptive Title + Github link.
    # 3. Double-braces {{ }} prevent any capitalization changes.
    entry = f"""@article{{{full_id},
  author = {{Howland, Geoffrey}},
  title = {{{{{full_id}}}}},
  year = {{{year}}},
  url = {{https://zenodo.org/record/{zenodo_record}}},
  note = {{{{{long_title}. Github: {github_url} }}}}
}}
"""
    return (full_id, entry)

def main():
    root_papers_dir = "./papers"  
    master_entries = {}
    target_dirs = []

    if not os.path.exists(root_papers_dir):
        print(f"Error: {root_papers_dir} directory not found.")
        return

    print(f"Scanning for manifest.json files in {root_papers_dir}...")

    for root, dirs, files in os.walk(root_papers_dir):
        # We search for manifest.json OR manuscript.json based on your previous logs
        manifest_file = None
        if "manuscript.json" in files:
            manifest_file = "manuscript.json"

        if manifest_file:
            file_path = os.path.join(root, manifest_file)
            folder_name = os.path.basename(root)
            
            if 1:
            # try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    # Pass the folder name as a fallback ID
                    reg_id, entry = generate_bib_entry(data, folder_name)
                    
                    print(f"  Processed: {reg_id}:")
                    target_dirs.append(root)
                    master_entries[reg_id] = entry
                        
            # except Exception as e:
                # print(f"  Error reading {file_path}: {e}")

    if not master_entries:
        print("No valid entries found.")
        return

    # Write the Master Bibliography
    master_bib_name = "references.bib"
    sorted_ids = sorted(master_entries.keys())
    
    with open(master_bib_name, "w") as f:
        for rid in sorted_ids:
            f.write(master_entries[rid])
            f.write("\n")

    print(f"\nSuccess: Generated references.bib with {len(sorted_ids)} unique entries.")

    # Distribute
    for target in target_dirs:
        dest = os.path.join(target, master_bib_name)
        shutil.copy2(master_bib_name, dest)

    print("Global Bibliography Distribution Complete.")

if __name__ == "__main__":
    main()
