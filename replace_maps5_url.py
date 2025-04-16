#!/usr/bin/env python
import os
import sys

def replace_in_file(filepath, search_text, replacement_text):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        return False

    new_content = content.replace(search_text, replacement_text)
    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}")
            return True
        except Exception as e:
            print(f"Could not write {filepath}: {e}")
            return False
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python replace_maps_url.py \"C:\\Website Development Feb 2025\\WIP\\Northwood.LTD\"")
        sys.exit(1)

    target_dir = sys.argv[1]
    # The string to search for:
    search_text = "https://www.google.com/maps/place/CBD+Concrete+and+Excavation/@32.8009566,-97.3346608,10z/data=!3m1!4b1!4m6!3m5!1s0x864dd7654bf544a3:0x3635d70b53de970f!8m2!3d32.800813!4d-97.0043405!16s%2Fg%2F11h3btxdss?authuser=0&amp;hl=en&amp;entry=ttu&amp;g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D"
    # The string to replace with:
    replacement_text = "https://maps.app.goo.gl/H5BuVokapx7pDL7n9"

    # Define file extensions to check (adjust as needed)
    valid_extensions = ('.html', '.css', '.js')

    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            if filename.lower().endswith(valid_extensions):
                filepath = os.path.join(root, filename)
                replace_in_file(filepath, search_text, replacement_text)

if __name__ == '__main__':
    main()
