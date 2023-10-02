import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace with the URL of the website containing the data
url = "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-5-flux-en.php"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <tr> elements in the page
    tr_elements = soup.find_all('tr')

    # Initialize empty lists to store the data and headers
    data = []
    headers = []
    count = 0
    header = []
    # Iterate through the <tr> elements
    for tr in tr_elements:
        if (count ==0):
            headers = [th.text for th in tr.find_all('th')]
            df = pd.DataFrame(data, columns=headers)
            count +=1
        else:
            row_data = [th.text for th in tr.find_all('th')]
            row_data = row_data + [td.text for td in tr.find_all('td')]
            data.append(row_data)
        

    data_dicts = []
    # Convert data lists to dictionaries and store them in the data_dicts list
    for row in data:
        data_dict = dict(zip(headers, row))
        data_dicts.append(data_dict)

    df = pd.DataFrame(data_dicts)
    csv_file_path = 'f10.7flux.csv'
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"DataFrame saved to {csv_file_path}")

else:
    print("Failed to retrieve data from the website.")
