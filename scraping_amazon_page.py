# Original amazon product page scraping

import pandas as pd
import requests
from bs4 import BeautifulSoup

obj = {}
arr = []

url = "https://www.amazon.com/dp/B08WVVBWCN"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
print(resp.status_code)

soup = BeautifulSoup(resp.text, "html.parser")

prod_name = soup.find("span",
                      {"class": "a-size-large product-title-word-break"})
obj["name"] = prod_name.text.strip()
prod_price = soup.find("span", {"class": "a-price-whole"})
obj["price"] = prod_price.text
prod_rating = soup.find("span", {"class": "a-icon-alt"})
obj["rating"] = prod_rating.text
arr.append(obj)
print(arr)

df = pd.DataFrame(arr)

df.to_csv("amazon_data.csv", index=False)

# df.to_csv(‘amazon_data.csv’, index=False, encoding=’utf-8')
