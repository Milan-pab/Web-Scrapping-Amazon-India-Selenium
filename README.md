# Amazon India Product Scraper

This project allows you to scrape product data from **Amazon India** using **Selenium**, **BeautifulSoup**, and **pandas**.
It extracts product details such as title, price, rating, number of ratings, product link, and image URL, and saves the data into a CSV file.

## Features

- Scrape multiple pages of Amazon search results (configurable).
- Extract product details:
  - Title
  - Price (including currency)
  - Rating
  - Number of ratings (converts K/M to integers)
  - Product link
  - Image URL
- Easy to change the search keyword to scrape different products.
- Save all results to a CSV file for analysis or further processing.

## Requirements

- Python 3.8+
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (matching your Chrome version)

Install dependencies:

```bash
pip install selenium beautifulsoup4 pandas
