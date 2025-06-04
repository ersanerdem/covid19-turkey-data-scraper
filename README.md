# COVID-19 Turkey Data Scraper 🇹🇷

This project contains a Python-based web scraping tool developed to automatically collect daily COVID-19 statistics from the official website of the Turkish Ministry of Health.

## 🔍 Features

- Fetches daily COVID-19 data (cases, recoveries, deaths, etc.)
- Parses JavaScript-embedded JSON data from the HTML
- Saves the extracted data into a structured Excel file
- Uses Python's requests, BeautifulSoup, pandas, and regex libraries

## 📂 Project Structure

```
covid19-turkey-data-scraper/
├── scripts/
│   └── scraper.py
├── data/
│   └── covid19_turkey_data.xlsx
├── README.md
```

## ⚙️ Requirements

- Python 3.x
- requests
- beautifulsoup4
- pandas
- openpyxl

## 🧠 Motivation

This script was created out of necessity when manual data entry became unsustainable. It was written in one night to automate the process of collecting real data for a mathematical modeling project based on the SEIRDP model.

## 📈 Use Case

This data can be directly fed into epidemiological models for academic research, particularly compartmental models like SEIR, SEIRD, and SEIRDP.

## ✍️ Author

Developed by **Ersan Erdem**  
M.Sc. in Applied Mathematics | Python Developer | LaTeX Specialist
