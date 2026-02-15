import os
import json
import zipfile
import requests
import sys

# --- CONFIGURATION ---
# Replace with your actual token or set as an environment variable
ZENODO_ACCESS_TOKEN = "wOBU4Qs2mpVpleTuibCHDl0IQ6vihuT9OjKwILUGaymO3cw2Xi5quqjgHyGg" 
ZENODO_API_URL = "https://zenodo.org/api/deposit/depositions"

def zip_folder(folder_path, output_path):
    """Zips all files in a folder into a single archive."""
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Do not zip the output zip itself if it's in the same folder
                if file == os.path.basename(output_path):
                    continue
                file_path = os.path.join(root, file)
                # Create arcname to keep the zip contents relative to the folder
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"✅ Created archive: {output_path}")

def upload_to_zenodo(folder_path):
    # 1. Validation
    json_path = os.path.join(folder_path, "zenodo.json")
    if not os.path.exists(json_path):
        print(f"❌ Error: zenodo.json not found in {folder_path}")
        return

    # 2. Prepare Data
    with open(json_path, 'r') as f:
        metadata = json.load(f)

    folder_name = os.path.basename(os.path.normpath(folder_path))
    zip_name = f"{folder_name}.zip"
    zip_path = os.path.join(os.path.dirname(folder_path), zip_name)

    # 3. Create ZIP
    zip_folder(folder_path, zip_path)

    # 4. Create New Deposition (Draft)
    params = {'access_token': ZENODO_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    
    # We send an empty dict first to create the ID
    r = requests.post(ZENODO_API_URL, params=params, json={}, headers=headers)
    
    if r.status_code != 201:
        print(f"❌ Failed to create deposition: {r.text}")
        return
    
    deposition_data = r.json()
    dep_id = deposition_data['id']
    bucket_url = deposition_data['links']['bucket']
    print(f"✅ Created Draft Deposition ID: {dep_id}")

    # 5. Upload Metadata
    # Zenodo requires metadata to be wrapped in a "metadata" key
    payload = {"metadata": metadata}
    # Some fields in your JSON might need to be removed for the API 
    # (e.g., communities or subjects if not strictly following Zenodo schema)
    # The script attempts to send as-is.
    
    r = requests.put(f"{ZENODO_API_URL}/{dep_id}", 
                     params=params, 
                     data=json.dumps(payload), 
                     headers=headers)
    
    if r.status_code != 200:
        print(f"⚠ Metadata warning (continuing to file upload): {r.text}")
    else:
        print("✅ Metadata synced.")

    # 6. Upload the ZIP file
    print(f"🚀 Uploading {zip_name}...")
    with open(zip_path, "rb") as fp:
        r = requests.put(
            f"{bucket_url}/{zip_name}",
            data=fp,
            params=params,
        )
    
    # Success
    if r.status_code >= 200 and r.status_code < 300:
        print("\n" + "="*50)
        print("SUCCESS: PAPER UPLOADED AS DRAFT")
        print(f"Review and Publish here: https://zenodo.org/deposit/{dep_id}")
        print("="*50)

    else:
        print(f"❌ File upload failed: {r.text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cks_zenodo_uploader.py <path_to_paper_folder>")
    else:
        target_path = sys.argv[1]
        if os.path.isdir(target_path):
            upload_to_zenodo(target_path)
        else:
            print(f"❌ {target_path} is not a valid directory.")

