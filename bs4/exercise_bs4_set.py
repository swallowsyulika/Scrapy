import requests
from bs4 import BeautifulSoup

r = requests.get("http://hueyanchen.myweb.hinet.net")
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, "lxml")
print(soup)
# Let web's html turns to BeautifulSoup
''' To let a txt-file or net-html turns to html-file
    ~~~ soup.prettify() '''
