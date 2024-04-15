# failed attempt

import requests
from bs4 import BeautifulSoup

proper_list = []
obj = {}

url = "https://twitter.com/scrapingdog"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
print(resp.status_code)

soup = BeautifulSoup(resp.text, 'html.parser')

try:
  # obj["profile_name"] = soup.find_all("span",{"class":"css-1qaijid r-bcqeeo r-qvutc0 r-poiln3"})

  for elmnt in soup.find_all(
      "span", {"class": "css-1qaijid r-bcqeeo r-qvutc0 r-poiln3"}):
    print(elmnt)
except Exception as e:
  print(e)

# proper_list.append(obj)

# print(proper_list)
