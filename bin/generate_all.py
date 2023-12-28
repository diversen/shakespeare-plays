import os

print("Fetching HTML files")
os.system("python bin/fetch_html.py")
print("Generating CSV files")
os.system("python bin/generate_csv.py")
print("Generating MD files")
os.system("python bin/generate_md.py")
print("Generating HTML files")
os.system("python bin/generate_html.py")
