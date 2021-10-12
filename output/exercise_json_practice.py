import requests
import json

url = "https://www.googleapis.com/books/v1/volumes?maxResults=5&q=Python&projection=lite"
jsonfile = "Excise.json"
r = requests.get(url)
r.encoding = "utf8"
json_data = json.loads(r.text)
with open(jsonfile, "w") as wt:
    json.dump(json_data, wt)
