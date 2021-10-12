import requests
# try error response
url = "http://www.google.com/404"
try:
    r = requests.get("http://www.google.com", timeout=3)
    r.raise_for_status()
except requests.exceptions.RequestException as ex1:
    print("http request error")
    print(ex1)
except requests.exceptions.HTTPError as ex2:
    print("http answer error")
    print(ex2)
except requests.exceptions.ConnectionError as ex3:
    print("net connect error")
    print(ex3)
except requests.exceptions.Timeout as ex4:
    print("timeout")
    print(ex4)
