import os
import sys

# The exact tag to search for:
old_tag = '<img src="../cdn.prod.website-files.com/671a91ee07626cd6dad29988/671a97f55941485a40965baf_green%20logo.svg" loading="lazy" alt=""/>'

# The new tag to replace it with:
new_tag = '<img src="../Logo/NorthWoodLandscapingLogo.svg" loading="lazy" alt=""/>'

if len(sys.argv) < 2:
    print("Usage: python replace_green_logo.py <target_directory>")
    sys.exit(1)

target_dir = sys.argv[1]

# Walk through all files in the target directory recursively
for root, dirs, files in os.walk(target_dir):
    for file in files:
        # Only process HTML files
        if file.lower().endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            # If the old tag is found, perform the replacement
            if old_tag in content:
                new_content = content.replace(old_tag, new_tag)
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error writing {file_path}: {e}")
