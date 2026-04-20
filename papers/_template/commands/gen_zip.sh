#!/bin/bash

# 1. Get the current directory name (e.g., HOWL-MATH-1-2026)
DIR_NAME=$(basename "$PWD")

# 2. Define the ZIP filename
ZIP_NAME="${DIR_NAME}.zip"

# 3. Remove old zip if it exists to ensure a fresh build
rm -f "$ZIP_NAME"

# 4. Zip everything in the current directory recursively
# -r: recursive
# -q: quiet (optional, remove for more output)
zip -r "$ZIP_NAME" .

