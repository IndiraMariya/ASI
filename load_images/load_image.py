import requests
import os
import sys

# SDO WEBSITE URL
latest_url = "https://sdo.gsfc.nasa.gov/assets/img/latest"

# DOWNLOAD PATH
localdir = '/home/ubuntu/ASI/images'

channels = ["0335", "HMIB", "HMIBC"]
resolutions = ["512"]

for channel in channels:
    for resolution in resolutions:
        FILENAME = f"latest_{resolution}_{channel}.jpg"
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
