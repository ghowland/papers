#!/usr/bin/env python3

"""
Control System for safely handling large counts of Zenodo papers
"""

import argparse
import sys
import os
import json
import pprint
import subprocess
import shutil

import template
from paper_topics import TOPICS
import zenosync

# Commands
COMMANDS = ['list', 'show', 'build', 'scan', 'gen', 'backup', 'cleanup', 'sync']

# Creds
ZENODO_CRED_PATH = "/mnt/c/Users/Geoff/.secure/zenodo.json"
OUTPUT_JSON_PATH = "zenodo_master_manifest.json"

# Working
WORKING_DIR = '/mnt/c/Users/Geoff/work/papers/papers'

# Data
ZENODO_SET = '_template/cks_tools/zenodo_master_manifest.json'
PAPER_SET = 'papers.json'
PAPER_ZENODO_SET = 'papers_zenodo.json'

# Scripts
GEN_PDF = './_template/_old/gen_pdf.sh'
SCAN = '../../../_template/_old/scan.py'
GEN_BIBS = './_template/_old/create_bibs.py'
README = '../../../_template/_old/readme_gen.py'

# Site
README_SITE = "_template/data/README_site.md"
README_SITE_OUT = "README_site.md"


def execute_command(command, shell=True):
    """
    Executes a shell command and returns the return code, stdout, and stderr.
    
    Args:
        command (list or str): The command to run. Pass as a list if shell=False.
        shell (bool): Whether to execute through the shell. Use False for security.
        
    Returns:
        tuple: (return_code, stdout, stderr)
    """
    try:
        # We use capture_output=True to grab stdout and stderr
        # text=True returns strings instead of raw bytes
        result = subprocess.run(
            command,
            shell=shell,
            capture_output=True,
            text=True,
            check=False  # Don't raise exception on non-zero exit code
        )
        
        return result.returncode, result.stdout.strip(), result.stderr.strip()
        
    except FileNotFoundError:
        return 1, "", f"Error: Command '{command}' not found."
    except Exception as e:
        return 1, "", str(e)


def List(args):
  print("List everything")
  # print(args.work_list)
  for item in args.papers:
    if item['doi']['is_stub']:
      print(item['file_path'])
      # print(item['subject'])
      # pprint.pprint(item)
      # print(item.keys())


def Build(args):

  print(f"Build papers")

  for item in args.papers:
    # Only do stubbed
    if True:#item['doi']['is_stub'] and not item['skip']:
      directory = os.path.dirname(item['file_path'])
      cmd = f'{GEN_PDF} {directory}' 
      print(cmd)

    #   if item['paper_id'] != 'HOWL-0-2026': continue # Skip test
 
      (status, output, error) = execute_command(cmd)
      print(f'  Result: {status}  Output: {output[:40]}')
  

def Scan(args):
  original_dir = os.getcwd()

  print("Scan papers:")
  for item in args.papers:
    os.chdir(original_dir)

    # Only do stubbed
    if True:#item['doi']['is_stub']:
      directory = os.path.dirname(item['file_path'])
      os.chdir(directory)

      # Scan
      (status, output, error) = execute_command(SCAN)
      print(f'  Result: {status}  Output: {output[:40]}')

      # Gen README
      (status, output, error) = execute_command(README)
      print(f'  Result: {status}  Output: {output[:40]}')
  
  # Back to original dir
  os.chdir(original_dir)


def Gen(args):
  print("Generate Site README.md")
  readme_site = open(README_SITE).read()

  # Flatten the list
  topic_data = []
  for topic in TOPICS:
    for key, item in topic.items():
      item['topic'] = key

      # Add papers to the topic
      item['papers'] = []
      for paper in args.papers:
        # Skip?
        if paper['skip']:
          continue

        # print(f"Sub: {paper['subject']} Top: {topic}")
        if paper['subject'] == key:
          # print(f'Added paper: {topic}: {paper}')
          if paper['key_result'] == None:
            # Take from 
            if paper['subtitle'] != None:
              paper['key_result'] = paper['subtitle']
            elif paper['abstract'] != None:
              paper['key_result'] = paper['abstract'].split('. ')[0].strip()

          item['papers'].append(paper)

      topic_data.append(item)

  # Provide topics
  data = {'topics': topic_data}

  template.render_template(README_SITE_OUT, readme_site, data)


def Backup(args):
  print("Backup manuscript.md -> manuscript_orig.md, stub only")

  for item in args.papers:
    # print(f"Backup: {item['paper_id']} - {item['doi']['is_stub']} - {item['doi']['zenodo_id']}")
    # continue #Skip

    # Only do stubbed
    # if True:
    if item['doi']['is_stub']:
      backup = item['file_path'].replace('.md', '_orig.md')
      print(f'Backup: {item["file_path"]} -> {backup}')
      shutil.copy2(item['file_path'], backup)


def Cleanup(args):
  print("Cleanup stub manuscript.md from manuscript_orig.md, setting the Registry, Series Path, DOI")

  max_count = 3
  cur_count = 0

  for item in args.papers:

    # Only do stubbed
    if True:#item['doi']['is_stub']:
      if item['skip']: continue

      print(f'Cleanup: {item["file_path"]}')

      # Get lines
      backup = item['file_path'].replace('.md', '_orig.md')
      lines = open(backup).read().split('\n')

      # Fix the special lines
      for count in range(0, len(lines)):
        line = lines[count]
        if line.startswith('# HOWL-') and item['title'] in line:
          end_line = line.split(':', 1)[1].strip()
          lines[count] = f'# {end_line}'
        
        # Registry
        if line.startswith('**Registry:**'):
          lines[count] = f'**Registry:** [@{item["paper_id"]}]'
        
        # Series Path
        if line.startswith('**Series Path:**'):
          topic_name = item["paper_id"].split('-')[1]
          for topic_dict in TOPICS:
            if list(topic_dict.keys())[0] == topic_name:
              topic = topic_dict[topic_name]
              print(f'TOPIC: {topic}')

          # Format series path
          series_path = topic['path']

          paper_id = int(item["paper_id"].split('-')[2])
          if paper_id == 1:
            series_path = series_path.replace('{{registry_last}}', f'') #TODO: Verify number, reduce and put the last item
          else:
            parts = item["paper_id"].split('-')
            previous = f" → [@{parts[0]}-{parts[1]}-{paper_id - 1}-{parts[3]}]"
            series_path = series_path.replace('{{registry_last}}', previous)
          
          # Final Series path
          series_path = series_path.replace('{{registry}}', f'[@{item["paper_id"]}]')
          lines[count] = f'**Series Path:** {series_path}'
        
        # DOI
        if line.startswith('**DOI:**'):
          # topic = item["paper_id"].split('-')[1]
          if item["paper_id"] in args.papers_zenodo:
            zenodo_data = args.papers_zenodo[item["paper_id"]]
            lines[count] = f"**DOI:** {zenodo_data['doi']['raw']}"


      # Write the file out again
      output = '\n'.join(lines)
      with open(item['file_path'], 'w') as fp:
        fp.write(output)

      # # Limit
      # cur_count += 1
      # if cur_count >= max_count:
      #   break


def Sync(args):
  print("Sync")

  max_count = 1
  cur_count = 0

  for item in args.papers:

    # Only do stubbed
    # if item['doi']['is_stub'] and not item['skip']:
    if not item['skip']:
      topic_name = item["paper_id"].split('-')[1]
      paper_id = int(item["paper_id"].split('-')[2])

      print(f'Sync: {item["file_path"]}: {topic_name}: {paper_id}')

      # Limit
      cur_count += 1
      if cur_count >= max_count:
        break


def Show(args):
  print("Show something")


def Main(args):
  os.chdir(WORKING_DIR)

  args.work_list = []
  with open(ZENODO_SET, "r", encoding="utf-8") as fp:
    args.zenodo = json.load(fp)

  with open(PAPER_SET, "r", encoding="utf-8") as fp:
    args.papers = json.load(fp)

  with open(PAPER_ZENODO_SET, "r", encoding="utf-8") as fp:
    args.papers_zenodo = json.load(fp)

  # print(f'Papers: {args.papers}')
  # print(WORKING_DIR)
  # print(PAPER_SET)
  # return

  if args.verbose:
    print(f"Verbosity is enabled.")
  
  if args.command not in COMMANDS:
    print(f'Unknown command: {args.command}')
    print('\nCommands: %s\n' % ', '.join(COMMANDS))
    exit(1)
  
  # Commands
  if args.command == 'list':
    List(args)
  elif args.command == 'show':
    Show(args)
  elif args.command == 'build':
    Build(args)
  elif args.command == 'scan':
    Scan(args)
  elif args.command == 'gen':
    Gen(args)
  elif args.command == 'backup':
    Backup(args)
  elif args.command == 'cleanup':
    Cleanup(args)
  elif args.command == 'sync':
    Sync(args)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Control System for safely handling large counts of Zenodo papers")

  parser.add_argument("command", help="Action to perform: %s" % ', '.join(COMMANDS) )
  parser.add_argument("-n", "--name", type=str, default="User", help="The name to greet (default: User)")
  parser.add_argument("-c", "--count", type=int, default=1, help="A numeric repeat count (default: 1)")
  parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
  args = parser.parse_args()
  Main(args)


