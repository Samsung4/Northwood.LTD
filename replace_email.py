#!/usr/bin/env python3
import os
import sys

old_email = "info@northwood.ltd"
new_email = "info@northwood.ltd"

def process_file(file_path):
    try:
        # Open the file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Skip binary or non-text files
        print(f"Skipping non-text file: {file_path}")
        return

    new_content = content.replace(old_email, new_email)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Uncomment the following line if you want to limit changes to only .html files:
            # if not file.lower().endswith(".html"):
            #     continue
            file_path = os.path.join(root, file)
            process_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_email.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    process_directory(target_directory)
