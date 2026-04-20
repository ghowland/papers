import os
import json
import sys
import time
import hashlib
import requests
from pathlib import Path

ZENODO_CRED_PATH = "/mnt/c/Users/Geoff/.secure/zenodo.json"
OUTPUT_JSON_PATH = "zenodo_master_manifest.json"

def load_config(config_path: Path) -> dict:
    with open(config_path, "r") as f:
        return json.load(f)

def get_file_hash(filepath: str) -> str:
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_metadata_hash(metadata: dict) -> str:
    encoded = json.dumps(metadata, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()

def request(method: str, url: str, token: str, **kwargs) -> requests.Response:
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Bearer {token}"
    headers["Accept"] = "application/json"
    response = requests.request(method, url, headers=headers, **kwargs)
    if response.status_code == 429:
        print("  Rate limited, sleeping 10s...")
        time.sleep(10)
        return request(method, url, token, **kwargs)
    response.raise_for_status()
    return response

def main():
    config_path = Path(ZENODO_CRED_PATH).expanduser()
    manifest_path = Path(OUTPUT_JSON_PATH)

    if not config_path.exists():
        print(f"Error: Credentials file not found at {config_path}")
        sys.exit(1)

    config = load_config(config_path)
    token = config["api_token"]
    sandbox = config.get("sandbox", True)
    base_url = "https://sandbox.zenodo.org/api" if sandbox else "https://zenodo.org/api"

    print(f"Using {'SANDBOX' if sandbox else 'PRODUCTION'} Zenodo")
    print(f"Fetching depositions with pagination (2s between pages)...")
    print("-" * 40)

    records = {}
    page = 1
    total_fetched = 0

    while True:
        print(f"Fetching page {page}...")
        res = request("GET", f"{base_url}/deposit/depositions", token, params={"page": page, "size": 25})
        data = res.json()

        if not data:
            print(f"  Empty page, done.")
            break

        print(f"  Got {len(data)} depositions on page {page}, fetching details...")

        for item in data:
            depo_id = item["id"]
            print(f"    Fetching details for deposition {depo_id}...")
            full_item = request("GET", f"{base_url}/deposit/depositions/{depo_id}", token).json()

            local_key = f"remote_{depo_id}"
            records[local_key] = {
                "zenodo_id": depo_id,
                "doi": full_item.get("doi") or full_item.get("metadata", {}).get("prereserve_doi", {}).get("doi"),
                "status": full_item.get("state"),
                "metadata_hash": get_metadata_hash(full_item.get("metadata", {})),
                "files": {
                    f["filename"]: {"checksum": f["checksum"], "filesize": f["filesize"]}
                    for f in full_item.get("files", [])
                }
            }
            total_fetched += 1

        print(f"  Page {page} done. Total so far: {total_fetched}")

        if len(data) < 25:
            print("  Last page reached (fewer than 25 results).")
            break

        page += 1
        print(f"  Sleeping 2s before next page...")
        time.sleep(2)

    manifest = {
        "records": records,
        "last_full_sync": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }

    temp_path = manifest_path.with_suffix(".tmp")
    with open(temp_path, "w") as f:
        json.dump(manifest, f, indent=2)
    temp_path.replace(manifest_path)

    print("-" * 40)
    print(f"SUCCESS: {total_fetched} records saved to {manifest_path.absolute()}")
    print(f"Sync timestamp: {manifest['last_full_sync']}")

if __name__ == "__main__":
    main()
    