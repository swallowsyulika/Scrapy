import requests

r = requests.get("http://www.google.com")
print(r.headers['Content-Type'])
print(r.headers['Content-Length'])
print(r.headers['Date'])
print(r.headers['Server'])
# all can code like r.headers.get('xxx')
