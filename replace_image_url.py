import os
import sys

def replace_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        # If the file isn't UTF-8 encoded, skip it.
        return False
    if old_text in content:
        new_content = content.replace(old_text, new_text)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def main(root_dir, old_text, new_text):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if replace_in_file(file_path, old_text, new_text):
                print(f"Updated: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python replace_image_url.py <target_directory>")
        sys.exit(1)
    target_directory = sys.argv[1]
    old_text = "https://www.northwood.ltd/Logo/Northwood%20Logo.png"
    new_text = "https://www.northwood.ltd/Logo/Northwood%20Logo.png"
    main(target_directory, old_text, new_text)
