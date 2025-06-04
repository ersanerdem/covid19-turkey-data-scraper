
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime
import os 


# This script scrapes COVID-19 data from the Turkish Ministry of Health's website and saves it to an Excel file.



def fetch_html(url): 
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_covid_data(html):
    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all("script")
    if not scripts:
        return []

    raw_data = scripts[-1].string
    if not raw_data:
        return []

    raw_parts = raw_data.split("},{")
    headers = raw_parts[1].split('","')
    data_list = []

    # Extract first data point
    first_segment = raw_parts[0].split('\r\n//<![CDATA[\r\nvar geneldurumjson = [{')[-1]
    first_entry = dict()
    for item in headers:
        key_value = item.split(":")
        if len(key_value) == 2:
            key = re.sub(r'["]+', '', key_value[0]).strip()
            val = re.sub(r'["]+', '', key_value[1]).strip()
            first_entry[key] = val
    data_list.append(first_entry)

    # Remaining entries
    for i in range(1, len(raw_parts)-1):
        entry = {}
        for item in raw_parts[i].split('","'):
            key_value = item.split(":")
            if len(key_value) == 2:
                key = re.sub(r'["]+', '', key_value[0]).strip()
                val = re.sub(r'["]+', '', key_value[1]).strip()
                entry[key] = val
        data_list.append(entry)

    return data_list
 
def save_to_excel(data, filename=os.path.normpath(os.path.join('C:\\Users\\Ersan ERDEM\\Desktop\\Covid19_Turkey_Analysis', 'covid19_turkey_data.xlsx'))):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data successfully saved to {filename}")

def main():
    url = "https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html"
    html = fetch_html(url)
    if html:
        covid_data = parse_covid_data(html)
        if covid_data:
            save_to_excel(covid_data)
        else:
            print("Failed to parse COVID-19 data.")
    else:
        print("No HTML content to parse.")

if __name__ == "__main__":
    main()
