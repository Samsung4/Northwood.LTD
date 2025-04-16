#!/usr/bin/env python3


import os
import sys

# The exact text block to be deleted (all on one line):
TARGET_BLOCK = (
    '<div class="copyright-content"><div class="copyright-content-copy">'
    '<div class="copyright-text">© 2024 Northwood Landscaping. All Rights Reserved.</div>'
    '<div class="div-block-293"><div class="copyright-text">'
    '<a href="../../www.betheanomaly.io/index.html" target="_blank" class="link-22">Privacy Policy</a>'
    '</div><div class="copyright-text">'
    '<a href="../../www.betheanomaly.io/index.html" target="_blank" class="link-22">Terms &amp; Conditions</a>'
    '</div></div></div>'
    '<div class="copyright-text">'
    '<a href="../../www.betheanomaly.io/index.html" target="_blank" class="link-22">Design &amp; Developed by <span class="text-span-9">Northwood</span></a>'
    '</div></div></div></div></div>'
)

# List the file extensions to check.
FILE_EXTENSIONS = ('.html', '.htm', '.css', '.js', '.php', '.txt')

def remove_block_from_file(file_path, block_text):
    """If the file contains block_text, remove it and overwrite the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    if block_text in content:
        new_content = content.replace(block_text, '')
        if new_content != content:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {file_path}")
                return True
            except Exception as e:
                print(f"Error writing {file_path}: {e}")
                return False
    return False

def process_directory(target_dir, block_text):
    """Recursively process all files in target_dir with matching extensions."""
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith(FILE_EXTENSIONS):
                file_path = os.path.join(root, file)
                remove_block_from_file(file_path, block_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_copyright_block.py \"<target_directory>\"")
        sys.exit(1)

    target_directory = sys.argv[1]
    process_directory(target_directory, TARGET_BLOCK)
