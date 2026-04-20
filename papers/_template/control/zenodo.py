#!/usr/bin/env python3
# ./_template/control/zenodo.py
# Per-paper Zenodo operations. Run from a paper directory (CWD).

import os
import sys
import json
import time
import hashlib
import requests

ZENODO_CRED_PATH = "/mnt/c/Users/Geoff/.secure/zenodo.json"

MANUSCRIPT_JSON = "manuscript.json"
ZENODO_JSON = "zenodo.json"
DESCRIPTION_TXT = "description.txt"
ZENODO_OUT_JSON = "zenodo_out.json"
MANUSCRIPT_PDF = "!manuscript.pdf"


# ---------- helpers ----------

def load_json(path):
    f = open(path, "r")
    data = json.load(f)
    f.close()
    return data


def save_json(path, data):
    tmp = path + ".tmp"
    f = open(tmp, "w")
    json.dump(data, f, indent=2)
    f.close()
    os.replace(tmp, path)


def load_creds():
    if not os.path.isfile(ZENODO_CRED_PATH):
        print("ERROR: credentials not found at " + ZENODO_CRED_PATH)
        sys.exit(1)
    cfg = load_json(ZENODO_CRED_PATH)
    token = cfg["api_token"]
    sandbox = cfg.get("sandbox", True)
    if sandbox:
        base_url = "https://sandbox.zenodo.org/api"
    else:
        base_url = "https://zenodo.org/api"
    print("Zenodo: " + ("SANDBOX" if sandbox else "PRODUCTION") + " (" + base_url + ")")
    return token, base_url


def api_request(method, url, token, **kwargs):
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = "Bearer " + token
    headers["Accept"] = "application/json"
    response = requests.request(method, url, headers=headers, **kwargs)
    if response.status_code == 429:
        print("  Rate limited, sleeping 10s...")
        time.sleep(10)
        return api_request(method, url, token, headers=headers, **kwargs)
    response.raise_for_status()
    return response


def get_file_md5(path):
    h = hashlib.md5()
    f = open(path, "rb")
    while True:
        chunk = f.read(4096)
        if not chunk:
            break
        h.update(chunk)
    f.close()
    return h.hexdigest()


def read_deposition_id_from_manuscript():
    if not os.path.isfile(MANUSCRIPT_JSON):
        print("ERROR: " + MANUSCRIPT_JSON + " not found in CWD")
        sys.exit(1)
    ms = load_json(MANUSCRIPT_JSON)
    doi = ms.get("doi", "")
    if not doi:
        print("ERROR: manuscript.json has no doi field")
        sys.exit(1)
    prefix = "10.5281/zenodo."
    if prefix not in doi:
        print("ERROR: doi does not look like a Zenodo DOI: " + doi)
        sys.exit(1)
    dep_id = doi.split(prefix, 1)[1].strip()
    if not dep_id.isdigit():
        print("ERROR: could not parse numeric deposition id from doi: " + doi)
        sys.exit(1)
    print("Deposition id from manuscript.json: " + dep_id)
    return dep_id


def paper_name_from_cwd():
    return os.path.basename(os.getcwd())


def build_metadata_payload():
    # Metadata from zenodo.json; description replaced by description.txt
    if not os.path.isfile(ZENODO_JSON):
        print("ERROR: " + ZENODO_JSON + " not found in CWD")
        sys.exit(1)
    if not os.path.isfile(DESCRIPTION_TXT):
        print("ERROR: " + DESCRIPTION_TXT + " not found in CWD")
        sys.exit(1)
    meta = load_json(ZENODO_JSON)
    f = open(DESCRIPTION_TXT, "r")
    description = f.read()
    f.close()
    meta["description"] = description
    return {"metadata": meta}


# ---------- commands ----------

def cmd_get():
    print("Command: get")
    token, base_url = load_creds()
    dep_id = read_deposition_id_from_manuscript()

    url = base_url + "/deposit/depositions/" + dep_id
    print("GET " + url)
    res = api_request("GET", url, token)
    data = res.json()

    save_json(ZENODO_OUT_JSON, data)
    print("Wrote " + ZENODO_OUT_JSON)


def cmd_update():
    print("Command: update")
    token, base_url = load_creds()
    dep_id = read_deposition_id_from_manuscript()
    payload = build_metadata_payload()

    url = base_url + "/deposit/depositions/" + dep_id
    print("PUT " + url)
    res = api_request("PUT", url, token, json=payload)
    data = res.json()

    save_json(ZENODO_OUT_JSON, data)
    print("Wrote " + ZENODO_OUT_JSON)


def cmd_upload():
    print("Command: upload")
    token, base_url = load_creds()
    dep_id = read_deposition_id_from_manuscript()

    paper_name = paper_name_from_cwd()
    zip_name = paper_name + ".zip"

    files_to_upload = [MANUSCRIPT_PDF, zip_name]
    for fname in files_to_upload:
        if not os.path.isfile(fname):
            print("ERROR: file not found in CWD: " + fname)
            sys.exit(1)

    # Fetch deposition to get bucket url
    dep_url = base_url + "/deposit/depositions/" + dep_id
    print("GET " + dep_url)
    dep_res = api_request("GET", dep_url, token)
    dep = dep_res.json()

    bucket_url = dep.get("links", {}).get("bucket")
    if not bucket_url:
        print("ERROR: deposition has no bucket url (may be published/immutable)")
        sys.exit(1)
    print("Bucket: " + bucket_url)

    for fname in files_to_upload:
        size = os.path.getsize(fname)
        md5 = get_file_md5(fname)
        print("Uploading " + fname + " (" + str(size) + " bytes, md5=" + md5 + ")")
        url = bucket_url + "/" + fname
        fh = open(fname, "rb")
        api_request("PUT", url, token, data=fh)
        fh.close()
        print("  OK")

    # Refresh deposition state
    print("GET " + dep_url)
    res = api_request("GET", dep_url, token)
    save_json(ZENODO_OUT_JSON, res.json())
    print("Wrote " + ZENODO_OUT_JSON)


def cmd_create():
    print("Command: create")
    if os.path.isfile(ZENODO_OUT_JSON):
        print("ERROR: " + ZENODO_OUT_JSON + " already exists; refusing to create")
        sys.exit(1)

    token, base_url = load_creds()
    payload = build_metadata_payload()

    url = base_url + "/deposit/depositions"
    print("POST " + url)
    res = api_request("POST", url, token, json=payload)
    data = res.json()

    save_json(ZENODO_OUT_JSON, data)
    print("Wrote " + ZENODO_OUT_JSON)
    print("New deposition id: " + str(data.get("id")))
    print("New DOI: " + str(data.get("metadata", {}).get("prereserve_doi", {}).get("doi")))


def cmd_new_doi():
    print("Command: new_doi")
    if not os.path.isfile(ZENODO_OUT_JSON):
        print("ERROR: " + ZENODO_OUT_JSON + " does not exist; cannot create new version")
        sys.exit(1)

    token, base_url = load_creds()
    dep_id = read_deposition_id_from_manuscript()

    url = base_url + "/deposit/depositions/" + dep_id + "/actions/newversion"
    print("POST " + url)
    res = api_request("POST", url, token)
    data = res.json()

    # The newversion action returns the parent; the new draft is at links.latest_draft
    latest_draft_url = data.get("links", {}).get("latest_draft")
    if not latest_draft_url:
        print("ERROR: response had no latest_draft link")
        sys.exit(1)

    print("GET " + latest_draft_url)
    draft_res = api_request("GET", latest_draft_url, token)
    draft = draft_res.json()

    save_json(ZENODO_OUT_JSON, draft)
    print("Wrote " + ZENODO_OUT_JSON)
    print("New draft deposition id: " + str(draft.get("id")))
    print("New DOI: " + str(draft.get("metadata", {}).get("prereserve_doi", {}).get("doi")))


def cmd_publish():
    print("Command: publish")
    token, base_url = load_creds()
    dep_id = read_deposition_id_from_manuscript()

    print("About to PUBLISH deposition " + dep_id + ".")
    print("Type exactly 'Yes!' (case sensitive) to confirm, anything else aborts.")
    sys.stdout.write("> ")
    sys.stdout.flush()
    answer = sys.stdin.readline()
    # Strip only newline, preserve any other whitespace exactness
    if answer.endswith("\n"):
        answer = answer[:-1]
    if answer.endswith("\r"):
        answer = answer[:-1]

    if answer != "Yes!":
        print("Aborted.")
        sys.exit(1)

    url = base_url + "/deposit/depositions/" + dep_id + "/actions/publish"
    print("POST " + url)
    res = api_request("POST", url, token)
    data = res.json()

    save_json(ZENODO_OUT_JSON, data)
    print("Wrote " + ZENODO_OUT_JSON)
    print("Published. DOI: " + str(data.get("doi")))


# ---------- dispatch ----------

COMMANDS = ["get", "update", "upload", "create", "new_doi", "publish"]


def print_usage():
    print("Usage: ./_template/control/zenodo.py <command>")
    print("")
    print("Run from within a paper directory (CWD).")
    print("")
    print("Commands:")
    print("  get       fetch current Zenodo record -> zenodo_out.json")
    print("  update    PUT metadata (zenodo.json + description.txt) to existing DOI")
    print("  upload    upload !manuscript.pdf and <paper>.zip to existing DOI (replaces)")
    print("  create    POST new deposition; fails if zenodo_out.json exists")
    print("  new_doi   new version of existing deposition; fails if zenodo_out.json missing")
    print("  publish   publish deposition (requires typing 'Yes!' exactly)")


def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "get":
        cmd_get()
    elif cmd == "update":
        cmd_update()
    elif cmd == "upload":
        cmd_upload()
    elif cmd == "create":
        cmd_create()
    elif cmd == "new_doi":
        cmd_new_doi()
    elif cmd == "publish":
        cmd_publish()
    else:
        print("ERROR: unknown command: " + cmd)
        print("")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()

