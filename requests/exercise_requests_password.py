import requests

url = "https://api.github.com/user"

r = requests.get(url, auth=('swallowsyulika', 'swallowsyulika0210'))  # set auth to login
if r.status_code == requests.codes.ok:
    print(r.headers['Content-Type'])
    print(r.json())
else:
    print('false http request')
