from bs4 import BeautifulSoup

with open('load.html', encoding='utf8') as rd:
    soup = BeautifulSoup(rd, 'lxml')

tag_div = soup.select('#q2')
first_li = tag_div[0].ul.li
print(first_li)
second_li = first_li.next_sibling.next_sibling   # find one sibling(after)
print(second_li)
third_li = second_li.find_next_sibling()
print(third_li)
print('-'*20)

for i in first_li.find_next_siblings():     # find all siblings(after)
    print(i.name, i.span.string)
print('-'*20)

tag_li = tag_div[0].ul.li
trd_li = tag_li.find_next_sibling().find_next_sibling()
print(trd_li)
sec_li = trd_li.previous_sibling.previous_sibling   # twice cause have NavigableString
print(second_li)
fst_li = sec_li.find_previous_sibling()
print(fst_li)
print('-'*20)

for i in trd_li.find_previous_siblings():   # find all siblings(before)
    print(i.name, i.span.string)
