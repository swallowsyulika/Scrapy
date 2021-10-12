import re
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
file = "Google.png"
r = requests.get(url, stream=True)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag = soup.find(id="hplogo")
print(tag)      # (/[^/#?]+)+\.(?:jpg|gif|png)
match = re.search(r"(/[^/#?]+)+\.(?:jpg|gif|png)", str(tag))
# re.search 掃描整個字符串找到匹配樣式的第一個位置，並返回一個相應的匹配對象。
print(match.group())    # 返回一個或者多個匹配的子組。如果只有一個參數，結果就是一個字符串，如果有多個參數，結果就是一個元組，如果沒有參數，組1默認到0
# 實際上是去找 <img> 標籤裡面 src 屬性的網址
# 以上是在找圖片位置
# 以下是正式爬取圖片
url += str(match.group())
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(file, "wb") as wt:
        for chunk in response:
            wt.write(chunk)
    print("done")
else:
    print("fail")

