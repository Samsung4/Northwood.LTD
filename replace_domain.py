#!/usr/bin/env python3
import os
import sys

# Define the target strings
old_domain = "www.northwood.ltd"
new_domain = "www.northwood.ltd"

def process_file(file_path):
    """Read a file, replace the domain, and write back if changes were made."""
    try:
        # Try reading the file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # If decoding fails, skip this file (likely binary)
        print(f"Skipping non-text file: {file_path}")
        return

    # Replace occurrences of the old domain with the new one
    new_content = content.replace(old_domain, new_domain)

    # If a change was made, overwrite the file
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

def process_directory(directory):
    """Recursively process all files in the given directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_domain.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    process_directory(target_directory)
