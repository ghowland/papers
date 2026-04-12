import json
import time
import sys
from pathlib import Path
from zenosync import ZenodoSync

# --- CONFIGURATION ---
PAPERS_JSON = Path("../../papers.json")
MANIFEST_JSON = Path("zenodo_master_manifest.json")
PAPERS_ROOT = Path("../../")
SLEEP_INTERVAL = 5 
LIMIT = 1  # <--- SET TO 1 FOR INITIAL TEST. Set to None for all papers.

def map_cks_to_zenodo(paper):
    """Maps papers.json fields to Zenodo-compliant metadata."""
    # Build a rich description using abstract and frontmatter
    description = f"<p><b>Abstract:</b> {paper['abstract']}</p>"
    description += "<h4>Document Details</h4><ul>"
    for key, value in paper.get("frontmatter", {}).items():
        description += f"<li><b>{key}:</b> {value}</li>"
    description += "</ul>"
    
    return {
        "title": paper["title"],
        "upload_type": "publication",
        "publication_type": "article",
        "description": description,
        "creators": [{"name": "HOWL Archive", "affiliation": "HOWL Research"}],
        "notes": f"Paper ID: {paper['paper_id']}",
        "access_right": "open"
    }

def main():
    # 1. Initialize with stable API
    zn = ZenodoSync(manifest_path=str(MANIFEST_JSON))
    
    # 2. Load the papers registry
    if not PAPERS_JSON.exists():
        print(f"Error: {PAPERS_JSON} not found.")
        return

    with open(PAPERS_JSON, "r") as f:
        papers_worklist = json.load(f)

    # 3. Identify how many we are processing
    total_available = len(papers_worklist)
    to_process = papers_worklist[:LIMIT] if LIMIT else papers_worklist
    
    print(f"Starting sync. Limit set to: {LIMIT if LIMIT else 'All'}")
    print(f"Total available papers: {total_available}")
    print("-" * 30)

    count = 0
    for paper in to_process:
        paper_id = paper["paper_id"]
        count += 1
        
        print(f"[{count}/{len(to_process)}] Processing: {paper_id}")

        # Path Logic: Resolve directory containing manuscript
        # e.g., cks/papers/ADHM/HOWL-ADHM-1-2026/
        dir_path = PAPERS_ROOT / Path(paper["file_path"]).parent
        
        # Define the specific files we want to sync
        # 1. The Manuscript PDF
        # 2. The Zip bundle
        files_to_sync = []
        manuscript_pdf = dir_path / "!manuscript.pdf"
        zip_bundle = dir_path / f"{paper_id}.zip"

        if manuscript_pdf.exists():
            files_to_sync.append(str(manuscript_pdf))
        if zip_bundle.exists():
            files_to_sync.append(str(zip_bundle))

        if not files_to_sync:
            print(f"  !! No files found in {dir_path}. Skipping.")
            continue

        # Prepare Metadata
        metadata = map_cks_to_zenodo(paper)

        try:
            # Sync to Zenodo (Publishing is disabled inside the Lib)
            result = zn.sync_record(
                local_id=paper_id,
                metadata=metadata,
                file_paths=files_to_sync,
                publish=False
            )
            print(f"  [OK] Draft Synced. Zenodo ID: {result['zenodo_id']}")
            
        except Exception as e:
            print(f"  [FAIL] Error syncing {paper_id}: {e}")
            sys.exit(1) # Stop immediately on error for safety

        # Rate limiting
        if count < len(to_process):
            print(f"Waiting {SLEEP_INTERVAL}s...")
            time.sleep(SLEEP_INTERVAL)

    print("-" * 30)
    print("Sync Session Complete.")
    if LIMIT and LIMIT < total_available:
        print(f"NOTE: Only {LIMIT} paper was processed. Review it on Zenodo before removing the LIMIT.")

if __name__ == "__main__":
    main()
