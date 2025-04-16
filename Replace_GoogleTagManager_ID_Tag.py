import os
import sys

def replace_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {file_path}: {e}")
        return

    new_content = content.replace(old_text, new_text)
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Modified: {file_path}")

def main(root_dir, old_text, new_text):
    # Define a set of file extensions to process
    allowed_ext = ('.html', '.htm', '.css', '.js', '.txt', '.json', '.xml', '.svg')
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(allowed_ext):
                file_path = os.path.join(dirpath, filename)
                replace_in_file(file_path, old_text, new_text)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python replace_gtm.py <root_directory>")
        sys.exit(1)
    root_directory = sys.argv[1]
    old_text = "GTM-PL98PJ2N"
    new_text = "Placeholder"
    main(root_directory, old_text, new_text)
