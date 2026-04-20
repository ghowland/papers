#!/usr/bin/env python3
# ./_template/control/run.py
# Master runner: executes a named shell script in each paper dir listed in working_papers.txt

import os
import sys
import subprocess

PROJECT_ROOT = os.getcwd()
WORKING_LIST = os.path.join(PROJECT_ROOT, "working_papers.txt")
COMMANDS_DIR = os.path.join(PROJECT_ROOT, "_template", "commands")
PAPERS_DIR = os.path.join(PROJECT_ROOT, "papers")


def list_available_commands():
    if not os.path.isdir(COMMANDS_DIR):
        return []
    out = []
    for name in sorted(os.listdir(COMMANDS_DIR)):
        if name.endswith(".sh"):
            out.append(name[:-3])
    return out


def print_usage():
    print("Usage: ./_template/control/run.py <command_name>")
    print("")
    print("Reads working_papers.txt from project root.")
    print("For each paper dir listed, cd into it and run:")
    print("  ./_template/commands/<command_name>.sh")
    print("")
    print("Available commands:")
    cmds = list_available_commands()
    if not cmds:
        print("  (none found in " + COMMANDS_DIR + ")")
    else:
        for c in cmds:
            print("  " + c)


def read_working_papers():
    if not os.path.isfile(WORKING_LIST):
        print("ERROR: working_papers.txt not found at " + WORKING_LIST)
        sys.exit(1)
    papers = []
    f = open(WORKING_LIST, "r")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("#"):
            continue
        papers.append(line)
    f.close()
    return papers


def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    command_name = sys.argv[1]
    script_path = os.path.join(COMMANDS_DIR, command_name + ".sh")

    if not os.path.isfile(script_path):
        print("ERROR: command script not found: " + script_path)
        print("")
        print_usage()
        sys.exit(1)

    papers = read_working_papers()
    if len(papers) == 0:
        print("ERROR: working_papers.txt is empty")
        sys.exit(1)

    print("Runner: command=" + command_name)
    print("Runner: script=" + script_path)
    print("Runner: papers=" + str(len(papers)))
    print("")

    count = 0
    for paper_rel in papers:
        count = count + 1
        paper_dir = os.path.join(PAPERS_DIR, paper_rel)

        print("[" + str(count) + "/" + str(len(papers)) + "] " + paper_rel)

        if not os.path.isdir(paper_dir):
            print("  ERROR: paper dir not found: " + paper_dir)
            sys.exit(1)

        print("  cd " + paper_dir)
        print("  exec " + script_path)

        result = subprocess.run([script_path], cwd=paper_dir)

        if result.returncode != 0:
            print("  ERROR: script failed with exit code " + str(result.returncode))
            sys.exit(result.returncode)

        print("  OK")
        print("")

    print("Runner: done, " + str(count) + " papers processed")


if __name__ == "__main__":
    main()
    
