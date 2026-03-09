#!/usr/bin/env python3
"""
Extract base64 images from tab fragment files into src/images/.

For each base64 data URI found in src/tabs/*.html:
1. Saves the full data URI string to src/images/{name}.b64
2. Replaces it in the tab file with a placeholder token {{IMG_{NAME}}}
3. Generates src/images/manifest.json mapping placeholders to files

The build.py script reads the manifest and re-injects the data URIs
during build, producing byte-identical HTML output.
"""

import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(SCRIPT_DIR, "src")
TABS_DIR = os.path.join(SRC_DIR, "tabs")
IMAGES_DIR = os.path.join(SRC_DIR, "images")

# Pattern: src="data:image/TYPE;base64,DATA"
# We capture the full data URI (everything inside the quotes)
DATA_URI_PATTERN = re.compile(r'src="(data:image/[^"]+)"')


def make_image_name(tab_filename, index):
    """
    Generate a meaningful image filename from the tab file and index.
    e.g., '01-overview.html' index 0 -> 'overview-0'
    """
    base = tab_filename.replace(".html", "")
    # Strip the leading number prefix for cleaner names
    # '01-overview' -> 'overview', '10-extended-family' -> 'extended-family'
    parts = base.split("-", 1)
    if len(parts) > 1 and parts[0].isdigit():
        name = parts[1]
    else:
        name = base
    return f"{name}-{index}"


def extract_images():
    os.makedirs(IMAGES_DIR, exist_ok=True)

    manifest = {}  # placeholder_token -> relative file path
    total_extracted = 0
    total_bytes_saved = 0

    tab_files = sorted(f for f in os.listdir(TABS_DIR) if f.endswith(".html"))

    for tab_file in tab_files:
        tab_path = os.path.join(TABS_DIR, tab_file)

        with open(tab_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_size = len(content)
        matches = list(DATA_URI_PATTERN.finditer(content))

        if not matches:
            continue

        print(f"\n{tab_file}: {len(matches)} images")

        # Process matches in reverse order so string positions remain valid
        for i, match in enumerate(matches):
            data_uri = match.group(1)
            img_name = make_image_name(tab_file, i)
            placeholder = "IMG_" + img_name.upper().replace("-", "_")
            b64_filename = f"{img_name}.b64"
            b64_path = os.path.join(IMAGES_DIR, b64_filename)

            # Save the data URI to file
            with open(b64_path, "w", encoding="utf-8") as f:
                f.write(data_uri)

            size_kb = len(data_uri) / 1024
            print(f"  [{i}] {placeholder} -> {b64_filename} ({size_kb:.0f} KB)")

            manifest[placeholder] = f"images/{b64_filename}"
            total_extracted += 1
            total_bytes_saved += len(data_uri)

        # Now replace all data URIs with placeholders in the tab file
        # Process in reverse order to preserve positions
        new_content = content
        for i, match in reversed(list(enumerate(matches))):
            img_name = make_image_name(tab_file, i)
            placeholder = "IMG_" + img_name.upper().replace("-", "_")
            token = "{{" + placeholder + "}}"

            # Replace the data URI inside the src attribute
            # match.group(0) is src="data:image/..."
            # We want to replace just the data URI part (group 1)
            start = match.start(1)
            end = match.end(1)
            new_content = new_content[:start] + token + new_content[end:]

        # Write the updated tab file
        with open(tab_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        new_size = len(new_content)
        saved = original_size - new_size
        print(f"  Tab file: {original_size/1024:.0f} KB -> {new_size/1024:.0f} KB (saved {saved/1024:.0f} KB)")

    # Write manifest
    manifest_path = os.path.join(IMAGES_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, sort_keys=True)

    print(f"\n{'='*50}")
    print(f"Extracted {total_extracted} images")
    print(f"Total image data: {total_bytes_saved/1024/1024:.1f} MB")
    print(f"Manifest: {manifest_path}")
    print(f"Image files: {IMAGES_DIR}/")


if __name__ == "__main__":
    extract_images()
