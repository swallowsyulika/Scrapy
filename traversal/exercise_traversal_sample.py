from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("load.html", encoding="utf8") as rd:
    soup = BeautifulSoup(rd, 'lxml')

tag_div = soup.select("#q2")
tag_ul = tag_div[0].ul
for i in tag_ul.children:
    print(type(i))          # find useless 'bs4.element.NavigableString'

print('-'*20)

for i in tag_ul.children:
    if not isinstance(i, NavigableString):
        print(i.name)    # find li
