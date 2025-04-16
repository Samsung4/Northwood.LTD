import os
import sys

def remove_text_in_file(file_path, target_text):
    # Read the file content (assuming UTF-8 encoding)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove all occurrences of the target text
    new_content = content.replace(target_text, "")
    # If changes were made, overwrite the file
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Modified: {file_path}")

def main(root_dir, target_text):
    # Walk through the directory recursively
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Process only HTML files; remove or adjust this filter if needed
            if filename.lower().endswith('.html'):
                file_path = os.path.join(dirpath, filename)
                remove_text_in_file(file_path, target_text)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python remove_privacy_terms.py <root_directory>")
        sys.exit(1)
    root_directory = sys.argv[1]
    # The text block to be removed (must match exactly)
    target_text = (
        '<a href="../www.betheanomaly.io/index.html" target="_blank" class="link-22">Privacy Policy</a>'
        '</div><div class="copyright-text"><a href="../www.betheanomaly.io/index.html" target="_blank" class="link-22">'
        'Terms &amp; Conditions</a>'
    )
    main(root_directory, target_text)
