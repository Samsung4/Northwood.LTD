#!/usr/bin/env python3
import os
import re

# Pattern to find any href/src/etc. that starts with "/www.northwood.ltd/"
PATTERN = re.compile(r'(["\'\(\s])\/www\.northwood\.ltd\/', re.IGNORECASE)

def fix_in_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        contents = f.read()

    # Replace "/www.northwood.ltd/" with "/"
    new_contents, count = PATTERN.subn(r'\1/', contents)
    if count:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_contents)
    return count

def main():
    total_fixes = 0
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if filename.lower().endswith(('.html', '.htm', '.css', '.js')):
                fullpath = os.path.join(dirpath, filename)
                fixes = fix_in_file(fullpath)
                if fixes:
                    print(f"[{fixes:3d}] replacements in {fullpath}")
                    total_fixes += fixes
    print(f"\nDone: {total_fixes} total replacements")

if __name__ == '__main__':
    main()
