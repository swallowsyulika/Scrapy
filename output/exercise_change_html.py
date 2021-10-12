from bs4 import BeautifulSoup

soup = BeautifulSoup("<b class='score'>Joe</b>", 'lxml')
tag = soup.b
tag.name = "p"                  # change
tag["class"] = "question"
tag["id"] = "name"
print(tag)
del tag["class"]
print(tag)
print('-'*20)

soup = BeautifulSoup("<p><b>One</b></p>", 'lxml')
tag = soup.b
new_tag = soup.new_tag("i")     # generate a new tag
new_tag.string = "Two"          # generate a new string
tag.replace_with(new_tag)       # change tag
print(soup.p)

