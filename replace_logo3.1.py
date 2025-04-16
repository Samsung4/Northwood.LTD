import os
import sys

# Old tag to be replaced:
old_tag = '<img src="../../Logo/NorthWoodLandscapingLogo.svg" alt="Northwood Landscaping" width="300" class="wbs-logo" loadig="lazy"/>'

# New tag to replace with:
new_tag = '<img src="../Logo/NorthWoodLandscapingLogo.svg" alt="Northwood Landscaping" width="300" class="wbs-logo" loadig="lazy"/>'

if len(sys.argv) < 2:
    print("Usage: python replace_logo4.py <target_directory>")
    sys.exit(1)

target_dir = sys.argv[1]

# Walk through all files in the target directory recursively.
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.lower().endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            if old_tag in content:
                new_content = content.replace(old_tag, new_tag)
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error writing {file_path}: {e}")
