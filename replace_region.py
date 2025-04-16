#!/usr/bin/env python3
import os
import sys

old_string = "Greater Vancouver"
new_string = "Greater Vancouver"

def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Skipping non-text file: {file_path}")
        return

    new_content = content.replace(old_string, new_string)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_region.py <directory>")
        sys.exit(1)
    process_directory(sys.argv[1])
