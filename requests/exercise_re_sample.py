import re
from bs4 import BeautifulSoup

with open("load.html", encoding='utf8') as rd:
    soup = BeautifulSoup(rd, 'lxml')

''' with regexp '''
regexp = re.compile("男-")   # re , regexp
tag_str = soup.find(text=regexp)
print(tag_str)
regexp = re.compile("\w+-")     # \w any word, + at least one, - end= '-'
tag_list = soup.find_all(text=regexp)
print(tag_list)
print('-'*20)

''' find email '''
email_regexp = re.compile("\w+@\w+\.\w+")   # xxx @xxx .xxx
tag_str = soup.find(text=email_regexp)
print(tag_str)
tag_list = soup.find_all(text=email_regexp)
print(tag_list)
print('-'*20)

''' find url '''
url_regexp = re.compile("^http:")       # http:
tag_href = soup.find(href=url_regexp)
print(tag_href)
tag_list = soup.find_all(href=url_regexp)
print(tag_list)
