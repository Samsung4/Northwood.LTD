#!/usr/bin/env python3
import os
import sys

# Only process files with these text-based extensions
ALLOWED_EXTENSIONS = {'.html', '.htm', '.css', '.js', '.txt', '.php', '.json', '.xml', '.md'}

def is_text_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def replace_in_file(filepath, old_text, new_text):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {filepath} (read error: {e})")
        return

    if old_text in content:
        new_content = content.replace(old_text, new_text)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}")
        except Exception as e:
            print(f"Error writing {filepath}: {e}")

def replace_in_directory(directory, old_text, new_text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            if is_text_file(filepath):
                replace_in_file(filepath, old_text, new_text)
            else:
                print(f"Skipping {filepath} (non-text file)")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python replace_logo.py <target_directory>")
        sys.exit(1)
    target_directory = sys.argv[1]
    replace_in_directory(
        target_directory,
        "../cdn.prod.website-files.com/671a91ee07626cd6dad29988/671a97f521e8900cec0048d5_white%20logo.svg",
        "../Logo/NorthWoodLandscapingLogo.svg"
    )
