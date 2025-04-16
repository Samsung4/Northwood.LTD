#!/usr/bin/env python3
import os
import sys
import re

# Compile regex patterns for both phone numbers.
# The patterns allow for optional whitespace between the parts.
pattern1 = re.compile(r"\(817\)\s*242-7484")
pattern2 = re.compile(r"\(817\)\s*242-9530")
new_phone = "(672) 963-8642"

def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        # Skip non-text files
        print(f"Skipping non-text file: {file_path}")
        return

    new_content = pattern1.sub(new_phone, content)
    new_content = pattern2.sub(new_phone, new_content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated file: {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Process only .html files (adjust extension if needed)
            if file.lower().endswith(".html"):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_phone.py <directory>")
        sys.exit(1)
    target_directory = sys.argv[1]
    process_directory(target_directory)
