from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("load.html", encoding="utf8") as rd:
    soup = BeautifulSoup(rd, "lxml")

tag_div = soup.select("#q2")
tag_ul = tag_div[0].ul

for i in tag_ul.contents:
    if not isinstance(i, NavigableString):
        print(i.span.string)
print('-'*20)

for i in tag_ul.children:
    if not isinstance(i, NavigableString):
        print(i.name)       # if not NavigableString
        for tag in i:       # search down tag
            print(type(tag))
            if not isinstance(tag, NavigableString):
                print(tag.name, tag.string)    # print Tag object name and string
            else:
                print(tag.replace('\n', ''))   # print NavigableString object and replace '\n'
print('-'*20)

for i in tag_ul.descendants:
    if not isinstance(i, NavigableString):
        print(i.name)
print('-'*20)

for i in tag_ul.strings:
    print(i.replace('\n', ''))
