import os
import sys

# The HTML tag to find (exactly as it appears)
old_tag = '<img loading="lazy" src="../../cdn.prod.website-files.com/671a91ee07626cd6dad29988/671c7fa484628304be63f73a_primary%201%20(1).svg" alt="" class="image-1588"/>'

# The replacement tag
new_tag = '<img src="../../Logo/NorthWoodLandscapingLogo.svg" alt="Northwood Landscaping" width="300" class="wbs-logo" loadig="lazy"/>'

if len(sys.argv) < 2:
    print("Usage: python replace_logo2.py <target_directory>")
    sys.exit(1)

target_dir = sys.argv[1]

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.lower().endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if old_tag in content:
                new_content = content.replace(old_tag, new_tag)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filepath}")
