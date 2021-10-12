from bs4 import BeautifulSoup

html_str = "<div id='msg'>Hello World!</div>"
soup = BeautifulSoup(html_str, 'lxml')
tag = soup.div
print(soup.name)    # [document]
print(type(soup))   # <class 'bs4.BeautifulSoup'>
print('-'*20)

html_str = "<p><!-- 註解文字 --></p>"
soup = BeautifulSoup(html_str, 'lxml')
comment = soup.p.string
print(comment)          # 註解文字
print(type(comment))    # <class 'bs4.element.Comment'>
