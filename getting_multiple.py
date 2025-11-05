from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import time

# Fix Unicode printing issue (especially on Windows)
sys.stdout.reconfigure(encoding='utf-8')
driver = webdriver.Chrome()
query = "handcraft"
pages = 7
file = 0

for i in range(1, pages + 1):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=349J41UZKK17D&sprefix=handcraft%2Caps%2C132&ref=&ref=sr_pg_{i}")

    items = driver.find_elements(By.CLASS_NAME, 'puis-card-container')
    print(f"{len(items) } items found.")
    for item in items:
        d = item.get_attribute('outerHTML')
        with open(f"output/multiple_items_page_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1



    time.sleep(2)

driver.close()
