from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import time

# Fix Unicode printing issue (especially on Windows)
sys.stdout.reconfigure(encoding='utf-8')
driver = webdriver.Chrome()
query = "handcraft"
driver.get(f"https://www.amazon.in/s?k={query}&crid=349J41UZKK17D&sprefix=handcraft%2Caps%2C132&ref=nb_sb_noss_1")

item = driver.find_element(By.CLASS_NAME, 'puis-card-container')



## Print the text of the first item found (raw from Amazon page)
#print(item.text)
#print(item.outerHTML)


#driver.close()
