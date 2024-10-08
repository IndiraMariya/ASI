from bs4 import BeautifulSoup
import requests
import os
# import sys

# DOWNLOAD PATH
localdir = '/media/ubuntu/T7 Shield/data'


def find_jpg_file(html_content, target_file_name):
    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all 'a' tags with 'href' containing the target file name
    file_links = soup.find_all('a', href=lambda href: href and target_file_name in href)

    # Extract the file names from the links
    file_names = [link.get('href') for link in file_links]

    return file_names

def get_save_image (url, file_name, file_path):
    FILE_PATH = os.path.join(file_path, file_name)
    print(FILE_PATH)
    # Download the file
    response = requests.get(url)
    if response.status_code == 200:
        with open(FILE_PATH, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {FILE_PATH}")
    else:
        print(f"Failed to download: {url}")


def get_images_index (index_url):
    #https://sdo.gsfc.nasa.gov/assets/img/browse/2021/01/01/20210101_000014_512_0335.jpg
    response = requests.get(index_url)

    html_content = ""
    if response.status_code == 200:
        html_content = response.text

    return html_content

def download_images (base_url, html_content, channels, resolutions, file_path):

    target_file_name = "{:}_{:}.jpg".format(resolutions, channels)
    print(target_file_name)
    result = find_jpg_file(html_content, target_file_name)
    for file_name in result:
        file_name_url = "{:}/{:}".format(base_url, file_name)
        print(file_name_url)
        get_save_image (file_name_url, file_name, file_path)

base_url = "https://sdo.gsfc.nasa.gov/assets/img/browse"
channels = ["0335"]
#, "HMIB", "HMII", "HMID", "HMIBC", "HMIIF", "HMIIC"
resolutions = ["512"]

days = list(range(1, 32))
months = list(range(1, 13))
years = [2021]
path = ""


for y1 in years:
    year = "{:04d}".format(y1)
    year_path = os.path.join(localdir, str(year))
    try:
        os.mkdir(year_path) 
    except:
        print("Directory Already Exists")
    for m1 in months:
        month  = "{:02d}".format(m1)
        month_path = os.path.join(year_path, str(month))
        try:
            os.mkdir(month_path) 
        except:
            print("Directory Already Exists")
        for d1 in days:
            day  = "{:02d}".format(d1)
            day_path = os.path.join(month_path, str(day))
            try:
                os.mkdir(day_path) 
            except:
                print("Directory Already Exists")
            image_list_url = "{:}/{:}/{:}/{:}/".format(base_url, year, month, day)
            html_content = get_images_index (image_list_url)
            for channel in channels:
                if html_content != None:
                    download_images (image_list_url, html_content, channel, "512", day_path)
