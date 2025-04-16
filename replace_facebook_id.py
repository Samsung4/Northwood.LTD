#!/usr/bin/env python3
import os
import sys

# The exact string we want to replace in the HTML files:
old_link = 'href="https://www.facebook.com/profile.php?id=100085269202944"'

# New string with the id replaced by zeros
new_link = 'href="https://www.facebook.com/profile.php?id=000000000000000"'

def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        # Skip non-text files
        print(f"Skipping non-text file: {file_path}")
        return

    new_content = content.replace(old_link, new_link)
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated file: {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Process only .html files
            if file.lower().endswith(".html"):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_facebook_id.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    process_directory(target_directory)
