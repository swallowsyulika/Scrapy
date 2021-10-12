from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)          # wait 10s to load web and if loaded will close
driver.get("http://example.com")    # url
print(driver.title)
html = driver.page_source           # html
# print(html)
soup = BeautifulSoup(html, "lxml")
fp = open("example.html", "w", encoding="utf8")
fp.write(soup.prettify())
print("already...success")
fp.close()
driver.quit()

