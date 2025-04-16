import glob

# Define the exact old URL to be replaced.
old_url = (
    "Big%2bA%2bLandscaping/%4032.753976%2c-97.23447%2c10z/data%3d%214m6%213m5%211s0x864e63db943d36f3_0xc084752027/g/11hkxhdxs2ddbf.html?entry=ttu&amp;g_ep=EgoyMDI0MTAyNy4wIKXMDSoASAFQAw%3D%3D"
)
new_url = "https://maps.app.goo.gl/H5BuVokapx7pDL7n9"

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        print(f"Skipping {filepath}: cannot decode in utf-8.")
        return

    # Replace the old URL with the new URL
    new_content = content.replace(old_url, new_url)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Replaced URL in: {filepath}")

def main():
    # Recursively find all HTML files in the current directory and subdirectories.
    html_files = glob.glob("**/*.html", recursive=True)
    for filepath in html_files:
        process_file(filepath)
    print("Processing complete.")

if __name__ == "__main__":
    main()
