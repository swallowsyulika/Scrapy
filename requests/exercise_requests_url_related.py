import requests

url_params = {'name': '夜草', 'score': '100'}
ur = requests.get('http://httpbin.org/get', params=url_params)  # params like type: dict
print(ur.url)   # get url
print(ur.text)  # get text
print(ur.encoding)  # get encoding
ur.encoding = 'utf-8'   # set encoding to utf-8
print(ur.encoding)
print('-'*20)
print(ur.content)   # get content have \n
print('-'*20)
urt = requests.get('http://httpbin.org/get', params=url_params, stream=True)    # stream temp didn't know
print(urt.raw)      # get HTTPResponse
print(urt.raw.read(15))     # get 15 words
print('-'*20)

post_data = {'name': '夜草', 'score': '100'}
pr = requests.post('http://httpbin.org/post', params=post_data)     # post
print(pr.text)
