import requests

url = "http://httpbin.org/cookies"
cookies = dict(name="Yulike")   # make dict

r = requests.get(url, cookies=cookies)  # set cookies
print(r.text)
