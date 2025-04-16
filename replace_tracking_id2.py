#!/usr/bin/env python
import os
import sys

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
            replace_in_file(filepath, old_text, new_text)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python replace_tracking_id.py <target_directory>")
        sys.exit(1)
    target_directory = sys.argv[1]
    replace_in_directory(target_directory, "1234567890", "1234567890")
