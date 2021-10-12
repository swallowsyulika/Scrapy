import requests

r = requests.get('http://httpbin.org/user-agent')
print(r.text)           # test
print(type(r.text))     # str
print('-'*20)
print(r.json())         # js
print(type(r.json()))   # dict
