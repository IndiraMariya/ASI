import requests
import re
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://sdo.gsfc.nasa.gov/assets/img/browse/"
years = [
    # "2010/",
    # "2011/",
    # "2012/",
    # "2013/",
    # "2014/",
    # "2015/",
    # "2016/",
    # "2017/",
    # "2018/",
    # "2019/",
    # "2020/",
    "2021/",
    # "2022/",
    # "2023/"
]
resoltion = "512"
filters = ["0335", "HMIB", "HMIIC"]

def getMonths(base_url, year):
    url = base_url+year
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all the directory links (DIR) in the HTML
        directory_links = soup.find_all('a')
        # Initialize an empty list to store the directory names
        directory_names = []
        # Loop through the directory links and extract the directory names
        for link in directory_links:
            directory_name = link.get_text()
            directory_names.append(directory_name)
        # Print the list of directory names
        directory_names = directory_names[5:]
        directory_names = directory_names[:12]
        return directory_names
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

def getDay(base_url, year, month):
    url = base_url+year+month
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all the directory links (DIR) in the HTML
        directory_links = soup.find_all('a')
        # Initialize an empty list to store the directory names
        days = []
        # Loop through the directory links and extract the directory names
        for link in directory_links:
            day = link.get_text()
            days.append(day)
        # Print the list of directory names
        days = days[5:]
        # dates = []
        # for day in days:
        #     dates.append(year[:-1] + month[:-1] + day[:-1])
        return days
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

def get_matching_files(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    file_links = soup.find_all('a', href=re.compile(r'._512_0335\.jpg$'))

    if not file_links:
        print("No matching files found on this page.")
        return []

    matching_files = [link.get('href') for link in file_links]
    return matching_files

def get_filepaths():
    paths = []
    file_path = "files.txt"
    for year in years:
        months = getMonths(url, year)
        for month in months:
            days = getDay(url, year, month)
            for day in days:
                day_url = url+year+month+day
                # paths.append(f"{date}_{time}_{resoltion}_0335.jpg")
                paths = get_matching_files(day_url)
                with open(file_path, 'a') as file:
                    for path in paths:
                        file.write(path + "\n")  # Each item on a new line

                # print(paths)
    
    return paths

if __name__ == "__main__":
    get_filepaths()

