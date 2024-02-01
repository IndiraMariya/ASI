import requests
import os
import time
# import sys

# COMMANDLINE ARGUMENTS
# download_path = sys.argv[1]

# SDO WEBSITE URL
latest_url = "https://sdo.gsfc.nasa.gov/assets/img/browse/2021"

# DOWNLOAD PATH
localdir = '/home/ubuntu/ASI/src/data/mk-2021_images'
filesdir = '/home/ubuntu/ASI/src/load_images/2021_file_paths.txt'

file = open(filesdir, "r")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

files = file.readlines()
delay_seconds = 30

for file_line in files:
    FILENAME = file_line
    path = file_line[4:6] + "/" + file_line[6:8]
    URL = f"{latest_url}/{path}/{FILENAME}"
    FILE_PATH = os.path.join(localdir, FILENAME)

    print(URL)
    # Download the file
    response = requests.get(URL, headers=headers)
    try:
        print (response)
        if response.status_code == 200:
            with open(FILE_PATH, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {FILE_PATH}")
        else:
            print(f"Failed to download: {URL}")
    except:
        pass
    time.sleep(delay_seconds)

file.close()