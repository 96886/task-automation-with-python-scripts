import os
import shutil
import requests

# List of URLs to download
urls = [
    'https://example.com/file1.pdf',
    'https://example.com/image1.jpg',
    'https://example.com/archive1.zip'
]

# Create a folder to store downloads
download_folder = 'downloads'
os.makedirs(download_folder, exist_ok=True)

# Download and save each file
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        filepath = os.path.join(download_folder, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}")

# Organize files by extension
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    ext = os.path.splitext(filename)[1][1:]  # Get extension without dot
    ext_folder = os.path.join(download_folder, ext)
    os.makedirs(ext_folder, exist_ok=True)
    shutil.move(file_path, os.path.join(ext_folder, filename))

print("Download and organization complete!")
