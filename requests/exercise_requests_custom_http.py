import requests

url = "http://httpbin.org/user-agent"
r = requests.get(url)   # sample
print(r.text)
print('-'*20)

url_headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
r = requests.get(url, headers=url_headers)      # make custom headers
print(r.text)
