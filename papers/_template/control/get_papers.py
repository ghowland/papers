#!/usr/bin/env python3
# ./_template/control/get_papers.py
# Emits paper dir paths (SUBJECT/PAPER-ID) to stdout, one per line.
# Arg1: "stub" | "all" | <search text for title/subtitle>

import os
import sys

PROJECT_ROOT = os.getcwd()
PAPERS_DIR = os.path.join(PROJECT_ROOT, "papers")

STUB_DOI_LINE = "**DOI:** 10.5281/zenodo.zzz"


def print_usage():
    sys.stderr.write("Usage: ./_template/control/get_papers.py <stub|all|search_text>\n")
    sys.stderr.write("\n")
    sys.stderr.write("  stub         papers whose manuscript.md has '" + STUB_DOI_LINE + "'\n")
    sys.stderr.write("  all          all papers\n")
    sys.stderr.write("  <text>       case-insensitive substring match against first '# ' title\n")
    sys.stderr.write("               and first '## ' subtitle line in manuscript.md\n")
    sys.stderr.write("\n")
    sys.stderr.write("Output: SUBJECT/PAPER-ID lines to stdout.\n")


def list_all_papers():
    out = []
    if not os.path.isdir(PAPERS_DIR):
        sys.stderr.write("ERROR: papers dir not found: " + PAPERS_DIR + "\n")
        sys.exit(1)
    for subject in sorted(os.listdir(PAPERS_DIR)):
        subject_dir = os.path.join(PAPERS_DIR, subject)
        if not os.path.isdir(subject_dir):
            continue
        for paper_id in sorted(os.listdir(subject_dir)):
            paper_dir = os.path.join(subject_dir, paper_id)
            if not os.path.isdir(paper_dir):
                continue
            manuscript = os.path.join(paper_dir, "manuscript.md")
            if not os.path.isfile(manuscript):
                continue
            out.append((subject, paper_id, manuscript))
    return out


def read_manuscript(path):
    f = open(path, "r", encoding="utf-8", errors="replace")
    text = f.read()
    f.close()
    return text


def has_stub_doi(text):
    for line in text.splitlines():
        if line.strip() == STUB_DOI_LINE:
            return True
    return False


def extract_title_subtitle(text):
    title = ""
    subtitle = ""
    for line in text.splitlines():
        s = line.strip()
        if title == "" and s.startswith("# ") and not s.startswith("## "):
            title = s[2:].strip()
            continue
        if subtitle == "" and s.startswith("## "):
            subtitle = s[3:].strip()
        if title != "" and subtitle != "":
            break
    return title, subtitle


def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    arg = sys.argv[1]
    papers = list_all_papers()

    if arg == "all":
        for subject, paper_id, _manuscript in papers:
            print(subject + "/" + paper_id)
        return

    if arg == "stub":
        for subject, paper_id, manuscript in papers:
            text = read_manuscript(manuscript)
            if has_stub_doi(text):
                print(subject + "/" + paper_id)
        return

    needle = arg.lower()
    for subject, paper_id, manuscript in papers:
        text = read_manuscript(manuscript)
        title, subtitle = extract_title_subtitle(text)
        if needle in title.lower() or needle in subtitle.lower():
            print(subject + "/" + paper_id)


if __name__ == "__main__":
    main()

