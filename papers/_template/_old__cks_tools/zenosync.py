import os
import json
import hashlib
import requests
import time
from typing import List, Dict, Any, Optional
from pathlib import Path

CONFIG_PATH = "/mnt/c/Users/Geoff/.secure/zenodo.json"

class ZenodoSync:
    def __init__(self, manifest_path: str, config_path: str = CONFIG_PATH):
        self.config_path = Path(config_path).expanduser()
        self.manifest_path = Path(manifest_path)
        self.config = self._load_config()
        
        self.token = self.config["api_token"]
        self.sandbox = self.config.get("sandbox", True)
        self.base_url = (
            "https://sandbox.zenodo.org/api" 
            if self.sandbox 
            else "https://zenodo.org/api"
        )
        
        self.manifest = self._load_manifest()

    def get_draft(self, local_id: str) -> Dict[str, Any]:
        """Fetch current state of a deposition from Zenodo."""
        record = self.manifest["records"].get(local_id, {})
        depo_id = record.get("zenodo_id")
        if not depo_id:
            raise ValueError(f"No zenodo_id found for {local_id}")
        return self._request("GET", f"deposit/depositions/{depo_id}").json()


    def create_draft(self, metadata_list, limit=None):
        created = []
        for local_id, metadata in metadata_list:
            if limit is not None and len(created) >= limit:
                break
            
            # ensure prereserve_doi is requested
            post_metadata = dict(metadata)
            post_metadata["prereserve_doi"] = True
            
            res = self._request("POST", "deposit/depositions", json={"metadata": post_metadata})
            depo_data = res.json()
            depo_id = depo_data["id"]
            doi = depo_data.get("metadata", {}).get("prereserve_doi", {}).get("doi")
            
            self.manifest["records"][local_id] = {
                "zenodo_id": depo_id,
                "doi": doi,
                "status": "draft",
                "metadata_hash": self._get_metadata_hash(metadata),
                "files": {}
            }
            self._save_manifest()
            created.append(local_id)
            print(f"Created draft {depo_id} for {local_id} — DOI: {doi}")
        return created

    def update_metadata(self, local_id: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Update metadata on an existing draft."""
        record = self.manifest["records"].get(local_id, {})
        depo_id = record.get("zenodo_id")
        if not depo_id:
            raise ValueError(f"No zenodo_id found for {local_id}")
        res = self._request("PUT", f"deposit/depositions/{depo_id}", json={"metadata": metadata})
        self.manifest["records"][local_id]["metadata_hash"] = self._get_metadata_hash(metadata)
        self._save_manifest()
        return res.json()


    def attach_files(self, local_id: str, file_paths: List[str]) -> Dict[str, Any]:
        """Add files to an existing draft."""
        record = self.manifest["records"].get(local_id, {})
        depo_id = record.get("zenodo_id")
        if not depo_id:
            raise ValueError(f"No zenodo_id found for {local_id}")
        remote_info = self._request("GET", f"deposit/depositions/{depo_id}").json()
        bucket_url = remote_info["links"]["bucket"]
        for p in file_paths:
            path = Path(p)
            fname = path.name
            with open(path, "rb") as f:
                self._request("PUT", f"{bucket_url.split('/api/')[1]}/{fname}", data=f)
            self.manifest["records"][local_id]["files"][fname] = {
                "checksum": self._get_file_hash(p),
                "size": path.stat().st_size
            }
            print(f"Attached {fname} to {depo_id}")
        self._save_manifest()
        return self.manifest["records"][local_id]


    def publish(self, local_id: str) -> Dict[str, Any]:
        """Publish a single record."""
        record = self.manifest["records"].get(local_id, {})
        depo_id = record.get("zenodo_id")
        if not depo_id:
            raise ValueError(f"No zenodo_id found for {local_id}")

        res = self._request("POST", f"deposit/depositions/{depo_id}/actions/publish")
        data = res.json()

        submitted = data.get("submitted", False)
        state = data.get("state")

        if not submitted or state != "done":
            raise RuntimeError(
                f"Publish failed for {local_id} (depo_id={depo_id}). "
                f"submitted={submitted}, state={state}. "
                f"Full response: {json.dumps(data, indent=2)}"
            )

        self.manifest["records"][local_id]["status"] = "published"
        self.manifest["records"][local_id]["doi"] = data.get("doi")
        self._save_manifest()

        print(f"Published {depo_id} for {local_id} — DOI: {data.get('doi')}")
        return data

    def reserve_doi(self, local_id: str) -> str:
        """Request a prereserved DOI for an existing draft."""
        record = self.manifest["records"].get(local_id, {})
        depo_id = record.get("zenodo_id")
        if not depo_id:
            raise ValueError(f"No zenodo_id found for {local_id}")

        current = self._request("GET", f"deposit/depositions/{depo_id}").json()
        existing_doi = current.get("metadata", {}).get("prereserve_doi", {}).get("doi")
        if existing_doi:
            print(f"DOI already reserved for {local_id}: {existing_doi}")
            self.manifest["records"][local_id]["doi"] = existing_doi
            self._save_manifest()
            return existing_doi

        self._request("PUT", f"deposit/depositions/{depo_id}", json={
            "metadata": {"prereserve_doi": True}
        })

        updated = self._request("GET", f"deposit/depositions/{depo_id}").json()
        doi = updated.get("metadata", {}).get("prereserve_doi", {}).get("doi")
        if not doi:
            raise RuntimeError(f"prereserve_doi returned no DOI for {local_id}. Response: {updated}")

        self.manifest["records"][local_id]["doi"] = doi
        self._save_manifest()
        print(f"Reserved DOI for {local_id}: {doi}")
        return doi

    def _load_config(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config not found at {self.config_path}")
        with open(self.config_path, "r") as f:
            return json.load(f)

    def _load_manifest(self) -> Dict[str, Any]:
        if self.manifest_path.exists():
            with open(self.manifest_path, "r") as f:
                return json.load(f)
        return {"records": {}, "last_full_sync": None}

    def _save_manifest(self):
        temp_path = self.manifest_path.with_suffix(".tmp")
        with open(temp_path, "w") as f:
            json.dump(self.manifest, f, indent=2)
        temp_path.replace(self.manifest_path)

    def _get_file_hash(self, filepath: str) -> str:
        """MD5 hash to match Zenodo's internal checksums."""
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def _get_metadata_hash(self, metadata: Dict[str, Any]) -> str:
        """Deterministic hash of metadata dictionary."""
        encoded = json.dumps(metadata, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        # Use absolute URL if provided (pagination), else build from base
        url = endpoint if endpoint.startswith("http") else f"{self.base_url}/{endpoint.lstrip('/')}"
        
        headers = kwargs.get("headers", {})
        # Use Authorization Header instead of query params for production reliability
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Accept"] = "application/json"
        kwargs["headers"] = headers
        
        # Ensure we don't pass access_token in params twice
        params = kwargs.get("params", {})
        if "access_token" in params:
            del params["access_token"]
        kwargs["params"] = params

        response = requests.request(method, url, **kwargs)
        if response.status_code == 429:
            time.sleep(10)  # Rate limit backoff
            return self._request(method, endpoint, **kwargs)
        
        response.raise_for_status()
        return response

    def bootstrap_from_remote(self):
        """Initial sync: Pull all existing depositions into manifest."""
        print("Bootstrapping manifest from Zenodo...")
        url = "deposit/depositions"
        
        while url:
            res = self._request("GET", url)
            data = res.json()
            
            for item in data:
                depo_id = item["id"]
                full_item = self._request("GET", f"deposit/depositions/{depo_id}").json()
                
                local_key = f"remote_{depo_id}"
                
                self.manifest["records"][local_key] = {
                    "zenodo_id": depo_id,
                    "doi": full_item.get("doi") or full_item.get("metadata", {}).get("prereserve_doi", {}).get("doi"),
                    "status": full_item.get("state"),
                    "metadata_hash": self._get_metadata_hash(full_item.get("metadata", {})),
                    "files": {
                        f["filename"]: {"checksum": f["checksum"], "filesize": f["filesize"]}
                        for f in full_item.get("files", [])
                    }
                }
                print(f" Cached {depo_id}")
            
            # Check Link headers for next page
            url = res.links.get("next", {}).get("url")
        
        self.manifest["last_full_sync"] = time.strftime("%Y-%m-%dT%H:%M:%SZ")
        self._save_manifest()

    def sync_record(self, local_id: str, metadata: Dict[str, Any], file_paths: List[str], publish: bool = False):
        """Sync specific document metadata and files. Publish logic disabled for safety."""
        record = self.manifest["records"].get(local_id, {})
        depo_id = record.get("zenodo_id")
        meta_hash = self._get_metadata_hash(metadata)
        
        # 1. Ensure Deposition exists
        if not depo_id:
            res = self._request("POST", "deposit/depositions", json={"metadata": metadata})
            depo_data = res.json()
            depo_id = depo_data["id"]
            record = {
                "zenodo_id": depo_id,
                "doi": depo_data["metadata"].get("prereserve_doi", {}).get("doi"),
                "status": "draft",
                "files": {}
            }
        else:
            # 2. Update Metadata if drifted
            if record.get("metadata_hash") != meta_hash:
                self._request("PUT", f"deposit/depositions/{depo_id}", json={"metadata": metadata})
        
        record["metadata_hash"] = meta_hash
        
        # 3. Verify Attachments
        remote_info = self._request("GET", f"deposit/depositions/{depo_id}").json()
        bucket_url = remote_info["links"]["bucket"]
        remote_files = {f["filename"]: f for f in remote_info.get("files", [])}
        
        current_files_manifest = {}
        
        for p in file_paths:
            path = Path(p)
            fname = path.name
            local_hash = self._get_file_hash(p)
            
            needs_upload = False
            if fname not in remote_files:
                needs_upload = True
            elif remote_files[fname]["checksum"] != local_hash:
                file_id = remote_files[fname]["id"]
                self._request("DELETE", f"deposit/depositions/{depo_id}/files/{file_id}")
                needs_upload = True
            
            if needs_upload:
                with open(path, "rb") as f:
                    # Using the bucket API path suffix
                    self._request("PUT", f"{bucket_url.split('/api/')[1]}/{fname}", data=f)
                current_files_manifest[fname] = {"checksum": local_hash, "size": path.stat().st_size}
            else:
                current_files_manifest[fname] = {
                    "checksum": remote_files[fname]["checksum"],
                    "size": remote_files[fname]["filesize"]
                }

        record["files"] = current_files_manifest

        # 4. Optional Publish - DISABLED for safety as requested
        if publish:
             print(f"Warning: Publish requested for {local_id}, but publish functionality has been disabled.")

        self.manifest["records"][local_id] = record
        self._save_manifest()
        return record
    