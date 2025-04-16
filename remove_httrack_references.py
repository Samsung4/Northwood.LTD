import glob
import re

# List of text patterns to remove.
# You can add more patterns if you suspect other variations exist.
remove_patterns = [
    r'Mirrored from\s+www\.broadstonelandscape\.com/blog\s+by\s+HTTrack Website Copier',
    r'Mirrored from.*?by\s+HTTrack Website Copier',  # Generic pattern to catch variations
]

def remove_references(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Skipping {filepath}: unable to decode in utf-8.")
        return

    original_content = content

    # Remove each pattern found in the content
    for pattern in remove_patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned: {filepath}")

# Recursively find all HTML files in the current directory and subdirectories
html_files = glob.glob("**/*.html", recursive=True)

for file in html_files:
    remove_references(file)

print("Processing complete.")
