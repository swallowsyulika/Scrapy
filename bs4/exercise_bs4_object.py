from bs4 import BeautifulSoup

html_str = "<div id='msg' class='body strikeout'>Hello World!</div>"
# make object, name as div, have two attributes 'id' & 'class',
# and class have multiple attributes 'body' & 'strikeout'
# the navigablestring is "Hello World!"
soup = BeautifulSoup(html_str, 'lxml')
tag = soup.div      # make tag
print(type(tag))    # <class 'bs4.element.Tag'>
print(tag.name)     # div
print(tag['id'])        # msg
print(tag['class'])     # ['body', 'strikeout']
print(tag.attrs)    # {'id': 'msg', 'class': ['body', 'strikeout']}

print('-'*20)
print(tag.string)       # Hello World!
print(type(tag.string))     # <class 'bs4.element.NavigableString'>

print('-'*20)
html_str_compared = "<div id='msg'>Hello World!<p>Final Test</p></div>"
soup_compared = BeautifulSoup(html_str_compared, 'lxml')
tag_compared = soup_compared.div
print(tag_compared.string)      # None
print(tag_compared.text)        # Hello World!Final Test
print(type(tag_compared.text))  # <class 'str'>
print(tag_compared.get_text())                  # Hello World!Final Test
print(tag_compared.get_text('-'))               # Hello World!-Final Test
print(tag_compared.get_text('-', strip=True))   # no space
