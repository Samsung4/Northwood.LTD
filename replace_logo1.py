import os
import sys

# The string to find (exactly as in the HTML)
old_tag = '<img src="../../Logo/WIP/Illustrator Output/SVG/NorthWoodLandscapingLogo.svg" alt="Northwood Landscaping" width="300" class="wbs-logo" loading="lazy"/>'

# The replacement string
new_tag = '<img src="../../Logo/NorthWoodLandscapingLogo.svg" alt="Northwood Landscaping" width="300" class="wbs-logo" loading="lazy"/>'

if len(sys.argv) < 2:
    print("Usage: python replace_logo_update.py <target_directory>")
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
