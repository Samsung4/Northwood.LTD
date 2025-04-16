import os
import sys

# Define the old tag and the new tag.
old_tag = '<img src="../Logo/NorthWoodLandscapingLogo.svg" alt="Northwood Landscaping" width="300" class="wbs-logo" loadig="lazy"/>'
new_tag = '<img src="../../Logo/NorthWoodLandscapingLogo.svg" alt="Northwood Landscaping" width="300" class="wbs-logo" loadig="lazy"/>'

# Check for the target directory argument.
if len(sys.argv) < 2:
    print("Usage: python replace_logo_internal.py <target_directory>")
    sys.exit(1)

target_dir = sys.argv[1]

# Walk through all files in the target directory recursively.
for root, dirs, files in os.walk(target_dir):
    for file in files:
        # Only process .html files
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
