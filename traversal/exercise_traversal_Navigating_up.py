from bs4 import BeautifulSoup

with open('load.html', encoding='utf8') as rd:
    soup = BeautifulSoup(rd, 'lxml')

tag_div = soup.select('#q2')
tag_ul = tag_div[0].ul
print(tag_ul.parent.name)       # find one parent
print(tag_ul.find_parent().name)
print('-'*20)

for i in tag_ul.parents:        # find all parents
    print(i.name)
for i in tag_ul.find_parents():
    print(i.name)
