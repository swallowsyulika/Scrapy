import urllib.request

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/165px-Python-logo-notext.svg.png"
response = urllib.request.urlopen(url)
wt = open("Python(ub).png", "wb")
size = 0
while True:
    info = response.read(10000)
    if len(info) < 1:
        break
    size += len(info)
    wt.write(info)
print(size, "chrs are downloaded.")
wt.close()
response.close()
