import requests
import os
import sys

# COMMANDLINE ARGUMENTS
download_path = sys.argv[1]

# SDO WEBSITE URL
latest_url = "https://sdo.gsfc.nasa.gov/assets/img/latest"

# DOWNLOAD PATH
localdir = download_path

channels = ["0094", "0131", "0171", "0193", "0211", "0304", "0335", "1600", "1700", "HMIB", "HMII", "HMID", "HMIBC", "HMIIF", "HMIIC"]
resolutions = ["4096", "2048", "1024", "512"]

for channel in channels:
    for resoltion in resolutions:
        FILENAME = f"latest_{resoltion}_{channel}.jpg"
        URL = f"{latest_url}/{FILENAME}"
        FILE_PATH = os.path.join(localdir, FILENAME)

        # Download the file
        response = requests.get(URL)
        if response.status_code == 200:
            with open(FILE_PATH, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {FILE_PATH}")
        else:
            print(f"Failed to download: {URL}")
