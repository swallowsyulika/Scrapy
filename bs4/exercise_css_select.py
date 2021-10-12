from bs4 import BeautifulSoup

with open("load.html", encoding="utf8") as rd:
    soup = BeautifulSoup(rd, 'lxml')

# the selector find "#q1 > ul > li:nth-child(1) > span", but we need to change nth-child to nth-of-type
tag_item = soup.select("#q1 > ul > li:nth-child(1) > span")     # fix! this version can use nth-child()
# select the path of selector and return as "list"
print(tag_item[0].string)
tag_title = soup.select("title")    # find tag <title>
print(tag_title[0].string)
# cause q3 is under <div>, so find the first <div> to in order to find q3
tag_first_div = soup.find("div")    # find first tag <div>
tag_div = tag_first_div.select("div:nth-of-type(3)")  # father: find // find third tag <div> under father <div>
print(tag_div[0])
print('-'*20)

tag_title = soup.select("html head title")  # find <html> to <head> to <div>
print(tag_title[0].string)
tag_a = soup.select("body div a")
print(tag_a)
print('-'*20)

tag_a = soup.select("p > a")    # find <p>'s son tag <a>
print(tag_a)
tag_li = soup.select("ul > li:nth-of-type(2)")  # find under <ul> and second tag <li>
print(tag_li)
tag_span = soup.select("div > #email")  # find under <div> and id = email
print(tag_span)
print('-'*20)

tag_div = soup.find(id="q1")
print(tag_div.p.a.string)
print('----------')
tag_div = soup.select("#q1 ~ .survey")      # find brother of id=q1 and their class have to be survey
for i in tag_div:
    print(i.p.a.string)
print('----------')
tag_div = soup.select("#q1 + .survey")      # only find first brother
for i in tag_div:
    print(i.p.a.string)
print('-'*20)

tag_div = soup.select("#q1")
print(tag_div[0].p.a.string)
tag_span = soup.select("span#email")    # find <span id="email">
print(tag_span[0].string)
tag_div = soup.select("#q1, #q2")  # find id= q1 and q2
for i in tag_div:
    print(i.p.a.string)
tag_div = soup.find("div")    # only first
tag_p = tag_div.select(".question")
for i in tag_p:
    print(i.a["href"])
tag_li = soup.select("[class ~= selected]")  # find all tags have attribute class and class have selected
for i in tag_li:
    print(i)
print('-'*20)

tag_a = soup.select("a[href]")
print(tag_a)
tag_a = soup.select("a[href='http://example.com/q2']")
print(tag_a)
tag_a = soup.select("a[href^='http://example.com/']")   # first=
print(tag_a)
tag_a = soup.select("a[href$='q3']")    # end=
print(tag_a)
tag_a = soup.select("a[href*='q']")     # include
print(tag_a)
print('-'*20)

tag_a = soup.select_one("a[href]")   # find one and not list
print(tag_a)
