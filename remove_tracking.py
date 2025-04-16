import glob
import re
import os

# List of patterns for tracking references (add or remove as needed)
tracking_patterns = [
    r"google-analytics\.com",
    r"googletagmanager\.com",
    r"adsbygoogle\.js",
    r"facebook\.net",
    r"doubleclick\.net",
    # Add more patterns if needed
]

def remove_tracking_scripts(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Skipping {filepath}: unable to decode in utf-8.")
        return

    original_content = content

    # Remove entire <script> tags that reference any of the tracking domains
    for pattern in tracking_patterns:
        content = re.sub(
            r'<script[^>]*src=["\'][^"\']*' + pattern + r'[^"\']*["\'][^>]*>.*?</script>',
            '',
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned: {filepath}")

# Recursively find all HTML files in the current directory and subdirectories
html_files = glob.glob("**/*.html", recursive=True)

for file in html_files:
    remove_tracking_scripts(file)

print("Processing complete.")
