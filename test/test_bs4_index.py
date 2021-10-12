from bs4 import BeautifulSoup
import re

with open('index.html', encoding='utf8') as rd:
    soup = BeautifulSoup(rd, 'lxml')

tag_list = soup.find_all(class_="nav-item")  # find all class = "nav-item"
print(tag_list)
print('-'*20)
tag_li = soup.select("[class='nav-item']")
print(tag_li)
print(tag_list == tag_li)
'''
tag_list = soup.find_all("a")   # if you search, all tag <a> are have "href"
for i in tag_list:
    print(i)            # print <a>
    print(i["href"])    # print attribute href's value
print('-'*20)

regexp = re.compile("^http")    # regexp
tag_list = soup.find_all(href=regexp)   # find all http in href **
print(tag_list)
'''
