import sys
import json
from pathlib import Path

OUTPUT_PATH = "papers_zenodo.json"


def collect_zenodo_papers(search_dir="."):
    search_path = Path(search_dir)
    files = sorted(search_path.glob("paper_*.json"))

    papers = {}
    failed = []

    for filepath in files:
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            paper_id = data.get("paper_id")
            if not paper_id:
                failed.append((str(filepath), "missing paper_id"))
                continue
            papers[paper_id] = data
        except Exception as e:
            failed.append((str(filepath), str(e)))

    return papers, failed


def save_zenodo_papers(papers, output_path=OUTPUT_PATH):
    path = Path(output_path)
    temp_path = path.with_suffix(".tmp")
    with open(temp_path, "w") as f:
        json.dump(papers, f, indent=2)
    temp_path.replace(path)


def load_zenodo_papers(output_path=OUTPUT_PATH):
    with open(output_path, "r") as f:
        return json.load(f)


def main():
    print("Collecting paper_*.json files...")
    papers, failed = collect_zenodo_papers()

    print("Found: " + str(len(papers)))
    if failed:
        print("Failed to load " + str(len(failed)) + ":")
        for filepath, err in failed:
            print("  " + filepath + ": " + err)

    save_zenodo_papers(papers)
    print("Written to: " + OUTPUT_PATH)


if __name__ == "__main__":
    main()

    