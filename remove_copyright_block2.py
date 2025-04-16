import os
import sys

def remove_text_in_file(file_path, target_text):
    # Read the file content (using UTF-8 encoding)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace the target text with an empty string
    new_content = content.replace(target_text, "")
    # If changes were made, write the new content back to the file
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Modified:", file_path)

def main(root_dir, target_text):
    # Walk through the directory recursively
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Process only HTML files (adjust the condition if needed)
            if filename.lower().endswith('.html'):
                file_path = os.path.join(dirpath, filename)
                remove_text_in_file(file_path, target_text)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python remove_copyright_block.py <root_directory>")
        sys.exit(1)
    root_directory = sys.argv[1]
    # Define the exact text to remove.
    target_text = ('<div class="copyright-content"><div class="copyright-content-copy">'
                   '<div class="copyright-text">© 2024 Northwood Landscaping. All Rights Reserved.</div>'
                   '<div class="div-block-293"><div class="copyright-text">')
    main(root_directory, target_text)
