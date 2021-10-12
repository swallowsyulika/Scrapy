import requests
from bs4 import BeautifulSoup

url = "https://lol.garena.tw/game/item"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
tags = soup.find_all("div", class_="itemlist-item__desc")
for i in tags:
    print(i.string.strip())
print("There have", len(tags), "items in League of Legends.")
