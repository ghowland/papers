import sys
import json
import time
from pathlib import Path
from create_paper import load_papers, create_paper

PAPERS_JSON_PATH = "papers.json"
ZENODO_CRED_PATH = "/mnt/c/Users/Geoff/.secure/zenodo.json"

# Create Paper Delay, so they dont ban us
DELAY = 0.5

#NOTE: If NO_OP_MODE == True, then we wont make any papers, just print the messaegs
# NO_OP_MODE = False
NO_OP_MODE = True

def get_stub_papers(papers):
    stubs = []
    for paper in papers:
        if paper.get("skip"):
            continue
        doi = paper.get("doi", {})
        if doi.get("is_stub") is True:
            stubs.append(paper)
    return stubs


def create_all_drafts(limit=None, papers_path=PAPERS_JSON_PATH, config_path=ZENODO_CRED_PATH):
    papers = load_papers(papers_path)
    stubs = get_stub_papers(papers)

    total = len(stubs)
    to_process = stubs if limit is None else stubs[:limit]

    print("Stub papers found: " + str(total))
    print("Will process: " + str(len(to_process)))
    if limit is not None:
        print("Limit set to: " + str(limit))
    print("-" * 40)

    created = []
    failed = []

    for paper in to_process:
        paper_id = paper["paper_id"]
        try:
            if not NO_OP_MODE:
                print("Processing: " + paper_id)
                result = create_paper(paper_id, papers_path=papers_path, config_path=config_path)
            else:
                print("Processing - NO-OP: " + paper_id)
            created.append(paper_id)
        except Exception as e:
            print("  FAILED: " + str(e))
            failed.append((paper_id, str(e)))

        time.sleep(0.7)


    print("-" * 40)
    print("Done.")
    print("Created: " + str(len(created)))
    print("Failed:  " + str(len(failed)))
    if failed:
        print("Failures:")
        for paper_id, err in failed:
            print("  " + paper_id + ": " + err)

    return created, failed


def main():
    limit = None

    args = sys.argv[1:]
    if "--limit" in args:
        idx = args.index("--limit")
        try:
            limit = int(args[idx + 1])
        except (IndexError, ValueError):
            print("Error: --limit requires an integer argument")
            sys.exit(1)

    # create_all_drafts(limit=2)
    create_all_drafts(limit=limit)


if __name__ == "__main__":
    main()
