import requests
from lxml import html

url = "https://www.flag.com.tw/books/school_code_n_algo"
r = requests.get(url)
tree = html.fromstring(r.text)
print(tree)

for element in tree.getchildren():
    print(element)
print('-'*20)

# book's img   /html/body/section[2]/table/tr[2]/td[1]/a/img
# book's name  /html/body/section[2]/table/tr[2]/td[1]/a/p
tag_img = tree.xpath("/html/body/section[2]/table/tr[2]/td[1]/a/img")[0]
# xpath() return list
print(tag_img)
print(tag_img.tag)
print(tag_img.attrib["src"])    # !

tag_name = tree.xpath("/html/body/section[2]/table/tr[2]/td[1]/a/p")[0]
print(tag_name)
print(tag_name.tag)
print(tag_name.text_content())

print('-'*20)

print(tag_img.tag)                  # traversal
print(tag_img.getparent().tag)
print(tag_img.getnext().tag)
print(tag_name.tag)
print(tag_name.getprevious().tag)
print('-'*20)

for element in tag_img.getparent().getchildren():   # sibling
    print(element.tag)
