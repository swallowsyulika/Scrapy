from bs4 import BeautifulSoup
from bs4.element import NavigableString
with open('load.html', encoding='utf8') as rd:
    soup = BeautifulSoup(rd, 'lxml')

tag_html = soup.html
print(type(tag_html), tag_html.name)
tag_next = tag_html.next_element.next_element   # next tag
print(type(tag_next), tag_next.name)
tag_title = soup.title
print(type(tag_title), tag_title.name)
tag_previous = tag_title.previous_element.previous_element  # previous tag
print(type(tag_previous), tag_previous.name)
print('-'*20)

tag_div = soup.find(id="emails")    # find all tags after id=emails
for i in tag_div.next_elements:
    if not isinstance(i, NavigableString):
        print(i.name)
print('-'*20)

tag_div = soup.find(id='q1')        # find all tags before id=q1
for i in tag_div.previous_elements:
    if not isinstance(i, NavigableString):
        print(i.name)
