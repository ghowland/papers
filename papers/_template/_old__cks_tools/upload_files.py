import sys
import json
from pathlib import Path
from zenosync import ZenodoSync
import time

ZENODO_CRED_PATH = "/mnt/c/Users/Geoff/.secure/zenodo.json"
PAPERS_ZENODO_PATH = "papers_zenodo.json"
MANIFEST_PATH = "zenodo_master_manifest.json"


def load_zenodo_papers(path=PAPERS_ZENODO_PATH):
    with open(path, "r") as f:
        return json.load(f)


def get_file_paths(paper):
    file_path = paper.get("file_path", "")
    paper_id = paper["paper_id"]

    folder = Path(file_path).parent
    pdf = folder / "!manuscript.pdf"
    zip_file = folder / (paper_id + ".zip")

    return pdf, zip_file


def upload_paper_files(zn, paper, dry_run=False):
    paper_id = paper["paper_id"]
    doi_info = paper.get("doi", {})
    zenodo_id = doi_info.get("zenodo_id")

    if not zenodo_id:
        return "skip", "no zenodo_id"

    if doi_info.get("status") == "published":
        return "skip", "already published"

    pdf, zip_file = get_file_paths(paper)

    missing = []
    if not pdf.exists():
        missing.append(str(pdf))
    if not zip_file.exists():
        missing.append(str(zip_file))

    if missing:
        return "fail", "missing files: " + ", ".join(missing)

    if dry_run:
        return "dry_run", str(pdf) + " + " + str(zip_file)

    try:
        zn.attach_files(paper_id, [str(pdf), str(zip_file)])
        return "ok", str(pdf) + " + " + str(zip_file)
    except Exception as e:
        return "fail", str(e)


def upload_all_files(limit=None, dry_run=False, papers_path=PAPERS_ZENODO_PATH, config_path=ZENODO_CRED_PATH):
    papers = load_zenodo_papers(papers_path)
    zn = ZenodoSync(manifest_path=MANIFEST_PATH, config_path=config_path)

    all_papers = list(papers.values())
    to_process = all_papers if limit is None else all_papers[:limit]

    print("Total papers: " + str(len(all_papers)))
    print("Will process: " + str(len(to_process)))
    if dry_run:
        print("DRY RUN - no uploads will happen")
    print("-" * 40)

    results = {"ok": [], "skip": [], "fail": [], "dry_run": []}

    for paper in to_process:
        paper_id = paper["paper_id"]
        status, msg = upload_paper_files(zn, paper, dry_run=dry_run)
        results[status].append((paper_id, msg))
        print(status.upper() + " " + paper_id + ": " + msg)

        time.sleep(0.7)

    print("-" * 40)
    print("Done.")
    print("Uploaded: " + str(len(results["ok"])))
    print("Skipped:  " + str(len(results["skip"])))
    print("Failed:   " + str(len(results["fail"])))
    if dry_run:
        print("Dry run:  " + str(len(results["dry_run"])))

    if results["fail"]:
        print("\nFailures:")
        for paper_id, err in results["fail"]:
            print("  " + paper_id + ": " + err)

    return results


def main():
    args = sys.argv[1:]
    limit = None
    dry_run = False

    if "--dry-run" in args:
        dry_run = True
        args = [a for a in args if a != "--dry-run"]

    if "--limit" in args:
        idx = args.index("--limit")
        try:
            limit = int(args[idx + 1])
        except (IndexError, ValueError):
            print("Error: --limit requires an integer argument")
            sys.exit(1)

    upload_all_files(limit=limit, dry_run=dry_run)
    # upload_all_files(limit=1, dry_run=dry_run)


if __name__ == "__main__":
    main()
