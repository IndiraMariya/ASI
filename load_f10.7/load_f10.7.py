import requests
from bs4 import BeautifulSoup
import pandas as pd

urlHead = "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-5-flux-en.php?year="

csv_file_path = '/Users/indiram/ASI/f10.7/data/F10.7.csv'

for i in range(4, 24):
    if i < 10:
        year = "200" + str(i)
    else:
        year = "20" + str(i)
    url = urlHead + year
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tr_elements = soup.find_all('tr')
        data = []
        headers = []
        count = 0

        for tr in tr_elements:
            if count == 0:
                headers = [th.text for th in tr.find_all('th')]
                count += 1
                if year == "2004":
                    df = pd.DataFrame(columns=headers)
            else:
                row_data = [th.text for th in tr.find_all('th')]
                row_data = row_data + [td.text for td in tr.find_all('td')]
                data.append(row_data)

        data_dicts = []

        for row in data:
            data_dict = dict(zip(headers, row))
            data_dicts.append(data_dict)

        df = pd.DataFrame(data_dicts)

        # Append the DataFrame to the CSV file (mode='a' for append)
        if (year == "2004"):
            df.to_csv(csv_file_path, mode='a', index=False, header=True)
        else:
            df.to_csv(csv_file_path, mode='a', index=False, header=False)

        print(f"Data for {year} appended to {csv_file_path}")
    else:
        print(f"Failed to retrieve data for {year} from the website.")
