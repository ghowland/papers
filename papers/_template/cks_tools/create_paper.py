import sys
import re
import json
from pathlib import Path
from zenosync import ZenodoSync

ZENODO_CRED_PATH = "/mnt/c/Users/Geoff/.secure/zenodo.json"
PAPERS_JSON_PATH = "papers.json"


def load_papers(papers_path):
    with open(papers_path, "r") as f:
        return json.load(f)


def find_paper(papers, paper_id):
    for paper in papers:
        if paper["paper_id"] == paper_id:
            return paper
    return None


def markdown_to_html(text):
    if not text:
        return ""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return text


REPO_CONFIG = {
    "framework_name": "HOWL Archive",
    "framework_short": "HOWL",
    "framework_intro": (
        "This paper is part of the HOWL research archive"
        "—a collection of physics papers exploring integer fraction derivations"
        " across multiple domains using exact arithmetic and automated comparison."
    ),
    "falsification_heading": "Falsification Criteria",
    "falsification_body": (
        "All papers in this archive are subject to falsification through direct comparison"
        " to published experimental measurements. Each derived value is tested against"
        " independent data with explicit PASS/FAIL criteria. Any derived value that fails"
        " its comparison is documented and published alongside the successes."
    ),
    "learning_heading": "Research Context",
    "learning_body": (
        "This archive documents an ongoing research program in integer fraction physics."
        " The methodology is: derive values from gauge group integers using exact fraction"
        " arithmetic, compare to published measurements, and document all results including"
        " failures. The archive spans multiple physics domains connected through the soliton"
        " boundary framework described in the constituent papers."
    ),
    "contents_heading": "Package Contents",
    "contents_manuscript": "The complete derivation and supporting analysis.",
    "contents_readme": "Navigation, dependencies, and citation",
    "default_motto": "Derive. Compare. Publish.",
    "default_status": "Active. Results documented.",
}

def build_description(paper, config=REPO_CONFIG):
    parts = []

    title = paper["title"]
    subtitle = paper.get("subtitle", "")
    if subtitle:
        parts.append("<h2>" + title + ": " + subtitle + "</h2>")
    else:
        parts.append("<h2>" + title + "</h2>")

    parts.append("<p>" + config["framework_intro"] + "</p>")

    abstract = markdown_to_html(paper.get("abstract") or "")
    if abstract:
        parts.append("<h3>Abstract</h3>")
        parts.append("<p>" + abstract + "</p>")

    parts.append("<h3>" + config["falsification_heading"] + "</h3>")
    parts.append("<p>" + config["falsification_body"] + "</p>")

    parts.append("<h3>" + config["learning_heading"] + "</h3>")
    parts.append("<p>" + config["learning_body"] + "</p>")

    parts.append("<h3>" + config["contents_heading"] + "</h3>")
    parts.append("<ul>")
    paper_id = paper.get("paper_id", "")
    parts.append("<li><code>manuscript.md</code>: " + config["contents_manuscript"] + "</li>")
    parts.append("<li><code>README.md</code>: " + config["contents_readme"] + " (Registry: " + paper_id + ").</li>")
    parts.append("</ul>")

    deps = paper.get("dependencies", [])
    if deps:
        parts.append("<p><strong>Dependencies:</strong> " + ", ".join(deps) + "</p>")

    frontmatter = paper.get("frontmatter", {})
    motto = frontmatter.get("Motto", config["default_motto"])
    status = frontmatter.get("Status", config["default_status"])
    parts.append("<p><strong>Motto:</strong> " + motto + "<br><strong>Status:</strong> " + status + "</p>")

    return "\n".join(parts)

def build_metadata(paper):
    title = paper["title"]
    if paper.get("subtitle"):
        title = title + ": " + paper["subtitle"]

    description = build_description(paper)

    publication_date = "2026-02"
    raw_date = paper.get("frontmatter", {}).get("Date", "")
    if raw_date:
        months = {
            "January": "01", "February": "02", "March": "03", "April": "04",
            "May": "05", "June": "06", "July": "07", "August": "08",
            "September": "09", "October": "10", "November": "11", "December": "12"
        }
        parts = raw_date.split()
        if len(parts) == 2 and parts[0] in months:
            publication_date = parts[1] + "-" + months[parts[0]]

    github_path = paper.get("file_path", "")

    metadata = {
        "title": title,
        "upload_type": "publication",
        "publication_type": "article",
        "description": description,
        "version": "1.0",
        "publication_date": publication_date,
        "access_right": "open",
        "license": "CC-BY-4.0",
        "keywords": [
            "python"
        ],
        "related_identifiers": [
            {
                "scheme": "url",
                "identifier": "https://github.com/ghowland/papers/blob/main/" + github_path,
                "relation": "isSupplementedBy",
                "resource_type": "software"
            }
        ],
        "creators": [
            {
                "name": "Howland, Geoffrey",
                "affiliation": "Independent Researcher",
                "orcid": "0009-0009-7752-341X"
            }
        ],
        "contributors": [
            {
                "name": "Howland, Geoffrey",
                "type": "ContactPerson",
                "affiliation": "Independent Researcher"
            },
            {
                "name": "Claude Opus 4.6",
                "type": "Researcher",
                "affiliation": "Anthropic PBC"
            }
        ],
        "communities": [
            {"identifier": "zenodo"},
            {"identifier": "cks"}
        ],
        "subjects": [
            {
                "term": "Physics",
                "identifier": "https://id.loc.gov/authorities/subjects/sh85101653",
                "scheme": "url"
            }
        ],
        "language": "eng"
    }

    return metadata


def create_paper(paper_id, papers_path=PAPERS_JSON_PATH, config_path=ZENODO_CRED_PATH):
    papers = load_papers(papers_path)

    paper = find_paper(papers, paper_id)
    if paper is None:
        raise ValueError("paper_id not found in papers.json: " + paper_id)

    metadata = build_metadata(paper)

    manifest_path = "zenodo_master_manifest.json"
    zn = ZenodoSync(manifest_path=manifest_path, config_path=config_path)

    created = zn.create_draft([(paper_id, metadata)], limit=1)
    if not created:
        raise RuntimeError("create_draft returned empty result for: " + paper_id)

    doi = zn.reserve_doi(paper_id)
    zenodo_id = zn.manifest["records"][paper_id].get("zenodo_id")

    output_paper = {}
    for k, v in paper.items():
        output_paper[k] = v

    output_paper["doi"] = {
        "raw": doi or "10.5281/zenodo.zzz",
        "is_stub": doi is None,
        "zenodo_id": zenodo_id,
        "status": "draft"
    }

    output_path = Path("paper_" + paper_id + ".json")
    temp_path = output_path.with_suffix(".tmp")
    with open(temp_path, "w") as f:
        json.dump(output_paper, f, indent=2)
    temp_path.replace(output_path)

    print("Created draft for: " + paper_id)
    print("Zenodo ID: " + str(zenodo_id))
    print("DOI: " + str(doi))
    print("Written to: " + str(output_path))

    return output_paper


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_paper.py <paper_id>")
        print("Example: python create_paper.py HOWL-MATH-11-2026")
        sys.exit(1)

    paper_id = sys.argv[1]

    try:
        result = create_paper(paper_id)
    except Exception as e:
        print("Error: " + str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
