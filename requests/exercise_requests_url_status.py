import requests

r = requests.get("http://www.google.com")
if r.status_code == 200:    # if it exist
    print('yes')
else:
    print('no')
print(r.status_code == requests.codes.ok)   # test if it exist
print(r.status_code == requests.codes.all_good)     # same above
print('-'*20)
false_test = requests.get("http://www.google.com/404")  # test nonexistent
print(false_test.status_code)       # >>> 404
print(false_test == requests.codes.ok)      # False
# print(false_test.raise_for_status())     # 404 Client Error: Not Found for url
print('-'*20)



