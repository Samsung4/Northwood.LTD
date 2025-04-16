import glob

# Define the exact old URL and the new URL to replace it with.
old_url = (
    "https://www.google.com/maps/place/Big+A+Landscaping/@32.753976,-97.23447,211385m/data="
    "!3m1!1e3!4m18!1m9!3m8!1s0x864e63db943d36f3:0xc084752027210316!"
    "2sBig+A+Landscaping!8m2!3d32.753976!4d-97.23447!9m1!1b1!16s%2Fg%2F11hkxhdxs2!"
    "3m7!1s0x864e63db943d36f3:0xc084752027210316!8m2!3d32.753976!4d-97.23447!"
    "9m1!1b1!16s%2Fg%2F11hkxhdxs2?entry=ttu&g_ep=EgoyMDI0MTAyNy4wIKXMDSoASAFQAw%3D%3D"
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
    for file in html_files:
        process_file(file)
    print("Processing complete.")

if __name__ == "__main__":
    main()
