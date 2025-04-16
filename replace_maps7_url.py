#!/usr/bin/env python3
import os
import sys

def replace_in_file(filepath, search_text, replacement_text):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    new_content = content.replace(search_text, replacement_text)
    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated: {filepath}")
        except Exception as e:
            print(f"Error writing {filepath}: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python replace_maps_url.py \"C:\\Website Development Feb 2025\\WIP\\Northwood.LTD\"")
        sys.exit(1)

    target_dir = sys.argv[1]
    # The string to search for:
    search_text = "../www.google.com/maps/place/https://maps.app.goo.gl/H5BuVokapx7pDL7n9"
    # The replacement string:
    replacement_text = "https://maps.app.goo.gl/H5BuVokapx7pDL7n9"

    # Specify file extensions to process (adjust as needed)
    valid_extensions = ('.html', '.css', '.js')

    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            if filename.lower().endswith(valid_extensions):
                filepath = os.path.join(root, filename)
                replace_in_file(filepath, search_text, replacement_text)

if __name__ == '__main__':
    main()
