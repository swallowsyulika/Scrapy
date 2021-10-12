from selenium import webdriver
from bs4 import BeautifulSoup

# find html without js html
'''         
url = "https://hahow.in/courses"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(url)

print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
file = "hahow.html"
fp = open(file, "w", encoding="utf8")
fp.write(soup.prettify())
print("done..")
fp.close()
driver.quit()
'''
# find all title are <h4 class="title ..."></h4>
# css selector are   h4.title
# do js

url = "https://hahow.in/courses"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(url)

items = driver.find_elements_by_css_selector("h4.title")
for item in items:
    print(item.text)

driver.quit()
