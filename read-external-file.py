## Read Extrenal File

# Create and activate a virtual environment:
# python3 -m venv venv
# source venv/bin/activate  (Mac/Linux)
# venv\Scripts\activate      (Windows)

# Install required dependencies:
# pip3 install requests

# Run the script:
# python3 read-external-file.py


import requests

url = "https://example-files.online-convert.com/document/txt/example.txt"

response = requests.get(url)
response.raise_for_status()

lines = response.text.splitlines()
print(f"Number of lines: {len(lines)}")