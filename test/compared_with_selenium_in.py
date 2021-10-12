import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
tag = soup.select(".gLFyf")

print(tag)
