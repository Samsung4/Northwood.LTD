import os
import sys

# Define the exact strings to be replaced:
old_tag = '<img loading="lazy" src="../cdn.prod.website-files.com/671a91ee07626cd6dad29988/671c7fa484628304be63f73a_primary%201%20(1).svg" alt="" class="image-1588"/>'
new_tag = '<img loading="lazy" src="../Logo/NorthWoodLandscapingLogo.svg" alt="" class="image-1588"/>'

# Check for target directory argument
if len(sys.argv) < 2:
    print("Usage: python replace_image_1588.py <target_directory>")
    sys.exit(1)

target_dir = sys.argv[1]

# Walk recursively in the target directory
for root, dirs, files in os.walk(target_dir):
    for file in files:
        # Process only HTML files
        if file.lower().endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            # Replace the old image tag with the new one if present
            if old_tag in content:
                new_content = content.replace(old_tag, new_tag)
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error writing {file_path}: {e}")
