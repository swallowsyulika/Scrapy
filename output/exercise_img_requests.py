import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/165px-Python-logo-notext.svg.png"
file = "Python(rq).png"
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(file, "wb") as wt:
        for chunk in response:
            wt.write(chunk)
    print("done")
else:
    print("fail")
