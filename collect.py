from bs4 import BeautifulSoup
import pandas as pd
import os
d = {"Title": [], "Price": [], "Rating": [], "no_of_ratings": [], "Link": [],"ImageURL":[],}

# Function to convert rating and number of ratings to numeric values
def convert_count(text):
        text = text.upper().replace(",", "")
        if "K" in text:
            return int(float(text.replace("K", "")) * 1000)
        elif "M" in text:
            return int(float(text.replace("M", "")) * 1000000)
        else:
            return int(text) if text.isdigit() else 0



for file in os.listdir("output"):
    with open(f"output/{file}", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    t = soup.find("h2")
    p = soup.find("span",class_="a-offscreen")
    r = soup.find("span",class_="a-size-small")
    n = soup.find("span",class_="a-size-mini")
    #l  = soup.find("div", {"data-csa-c-id": "gbm112-6ai1j7-r96dlv-y9k733"})
    l = soup.find("a", class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal", href=True)
    i = soup.find("img", class_="s-image")


    title = t.get_text()
    price = p.get_text() if p else "No price"
    rating = r.get_text() if r else "No rating"
    ratings = n.get_text().replace("(","").replace(")","") if n else "No ratings"
    no_of_ratings = convert_count(ratings) if ratings != "No ratings" else 0
    link = "https://www.amazon.in" + l["href"] if l else "No link"
    image_url = i['src'] if i else "No image"
    
    d["Title"].append(title)
    d["Price"].append(price)
    d["Rating"].append(rating)
    d["no_of_ratings"].append(no_of_ratings)
    d["Link"].append(link)
    d["ImageURL"].append(image_url)
    '''
    print("----- ITEM -----")
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Number of Ratings: {no_of_ratings}")
    print(f"Link: {link}")
    print(f"Image URL: {image_url}")
    print("---------------")
    break
    '''
df = pd.DataFrame(d)
df.to_csv("data/amazon_handcraft_items.csv") 
    
    
    
    #print(soup.prettify()) #[:500])  # Print first 500 characters of prettified HTML