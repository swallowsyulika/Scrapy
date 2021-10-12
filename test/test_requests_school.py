import requests
from bs4 import BeautifulSoup

url = "https://www.nptu.edu.tw/bin/home.php"
r = requests.get(url)
r.encoding = 'utf-8'    # remember!
soup = BeautifulSoup(r.text, 'lxml')
with open('test_requests_school_results.html', 'w', encoding='utf8') as wt:
    wt.write(r.headers['Content-Type'])
    wt.write('\n')
    wt.write(soup.prettify())
# hit encoding="utf8" not "utf-8"
