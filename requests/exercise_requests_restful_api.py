import requests

url = "https://www.googleapis.com/books/v1/volumes"  # find books
                  
url_params = {"q": "Python", "maxResults": 5, "projection": "lite"}  # params

r = requests.get(url, params=url_params)
print(r.json())
