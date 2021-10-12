from bs4 import BeautifulSoup

with open('load.html', encoding="utf8") as rd:
    soup = BeautifulSoup(rd, 'lxml')

# print(soup)
''' find() , find(name, attribute, recursive, text, **kwargs)'''
''' with tag '''
tag_a = soup.find('a')      # find tag at <a>
print(tag_a.string)

''' with tag's father '''
tag_p = soup.find('p')
print(tag_p.a.string)       # find tag at <p> and p is the father of <a>
print('-'*20)

''' with id '''
tag_div = soup.find(id='q2')    # find id name q2
tag_a = tag_div.find('a')       # find <a> under id
print(tag_a.string)
print('-'*20)

''' with class in attrs '''
tag_li = soup.find(attrs={'class': 'response'})     # find class 'response'
tag_span = tag_li.find("span")      # find <span> under class
print(tag_span.string)
print('-'*20)

''' with class in class_ '''
tag_li = tag_div.find(class_="response")     # tag_div = soup.find(id='q2')
tag_span = tag_li.find("span")
print(tag_span.string)          # use "class_" to find class under id
print('-'*20)

''' with data-custom in attrs '''
tag_div = soup.find(attrs={"data-custom": "important"})
print(tag_div.string)       # find data-
print('-'*20)

''' with text '''
tag_str = soup.find(text="請問你的性別?")     # find text
print(tag_str)          # 請問你的性別?
tag_str = soup.find(text="10")
print(tag_str)
print(type(tag_str))            # <class 'bs4.element.NavigableString'>
print(tag_str.parent.name)      # find father tag >>> span
tag_str = soup.find(text="男")      # if didn't find, return None
print(tag_str)
print('-'*20)

''' with multiple attrs '''
tag_div = soup.find("div", class_="question")   # find tag <div class="question"> to </div>
print(tag_div)
tag_p = soup.find("p", class_="question")
print(tag_p)
print('-'*20)

''' with function '''
def is_secondary_q(tag):
    return tag.has_attr('href') and tag.get('href') == "http://example.com/q2"

tag_a = soup.find(is_secondary_q)   # didn't need ()
print(tag_a)
print('-'*20)

''' find_all , find_all(name, attribute, recursive, text, limit, **kwargs)
        find() is find_all(limit=1) '''
''' with find_all '''
tag_list = soup.find_all("p", class_="question")
print(tag_list)         # all compliant elements are make a list
print(type(tag_list))   # <class 'bs4.element.ResultSet'>
for i in tag_list:
    print(i.a.string)   # string in <a> and under the <p>
# add  limit=2  will search first two elements
print('-'*20)

''' find all tag '''
tag_div = soup.find("div", id="q2")
tag_all = tag_div.find_all(True)    # find all tag under <div id="q2">
print(tag_all)          # list
print('-'*20)

''' find all text '''
tag_div = soup.find("div", id="q2")
tag_str_list = tag_div.find_all(text=True)  # search all text
print(tag_str_list)
tag_str_list = tag_div.find_all(text=['20', '40'])  # search text only 20 and 40
print(tag_str_list)
print('-'*20)

''' find custom data '''
tag_div = soup.find("div", id="q2")
tag_list = tag_div.find_all(['p', 'span'])  # or
print(tag_list)
tag_list = tag_div.find_all(class_=["question", "selected"])
print(tag_list)
print('-'*20)

''' without recursive '''
tag_div = soup.find("div", id="q2")
tag_list = tag_div.find_all('li')       # find all <li>
print(tag_list)
tag_list = tag_div.find_all('li', recursive=False)  # not recursive
print(tag_list)     # []  cause <div>'s kids are <p> <ul> not <li>, <li> is under <ul>


