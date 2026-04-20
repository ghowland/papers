import sys
import json
from pathlib import Path
from zenosync import ZenodoSync

ZENODO_CRED_PATH = "/mnt/c/Users/Geoff/.secure/zenodo.json"
PAPERS_ZENODO_PATH = "papers_zenodo.json"
MANIFEST_PATH = "zenodo_master_manifest.json"


def load_zenodo_papers(path=PAPERS_ZENODO_PATH):
    with open(path, "r") as f:
        return json.load(f)


def publish_all(limit=None, papers_path=PAPERS_ZENODO_PATH, config_path=ZENODO_CRED_PATH):
    papers = load_zenodo_papers(papers_path)
    zn = ZenodoSync(manifest_path=MANIFEST_PATH, config_path=config_path)

    all_papers = list(papers.values())
    to_process = all_papers if limit is None else all_papers[:limit]

    print("Total papers: " + str(len(all_papers)))
    print("Will process: " + str(len(to_process)))
    print("-" * 40)

    results = {"ok": [], "skip": [], "fail": []}

    for paper in to_process:
        paper_id = paper["paper_id"]
        doi_info = paper.get("doi", {})
        zenodo_id = doi_info.get("zenodo_id")

        if not zenodo_id:
            msg = "no zenodo_id"
            results["skip"].append((paper_id, msg))
            print("SKIP " + paper_id + ": " + msg)
            continue

        if doi_info.get("status") == "published":
            msg = "already published"
            results["skip"].append((paper_id, msg))
            print("SKIP " + paper_id + ": " + msg)
            continue

        try:
            zn.publish(paper_id)
            results["ok"].append((paper_id, doi_info.get("raw", "")))
        except Exception as e:
            results["fail"].append((paper_id, str(e)))
            print("FAIL " + paper_id + ": " + str(e))

    print("-" * 40)
    print("Done.")
    print("Published: " + str(len(results["ok"])))
    print("Skipped:   " + str(len(results["skip"])))
    print("Failed:    " + str(len(results["fail"])))

    if results["fail"]:
        print("\nFailures:")
        for paper_id, err in results["fail"]:
            print("  " + paper_id + ": " + err)

    return results


def main():
    args = sys.argv[1:]
    limit = None

    if "--limit" in args:
        idx = args.index("--limit")
        try:
            limit = int(args[idx + 1])
        except (IndexError, ValueError):
            print("Error: --limit requires an integer argument")
            sys.exit(1)

    publish_all(limit=limit)


if __name__ == "__main__":
    main()
    