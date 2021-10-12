from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get("http://example.com")
# selenium
h1 = driver.find_element_by_tag_name("h1")
print(h1.text)
p = driver.find_element_by_tag_name("p")
print(p.text)
html_h1 = h1.get_attribute("innerHTML")     # not have <tag>
print(html_h1)
html_h1 = h1.get_attribute("outerHTML")     # whole tag
print(html_h1)
print("-"*20)
# BeautifulSoup
soup = BeautifulSoup(driver.page_source, "lxml")
tag_h1 = soup.find("h1")
print(tag_h1.string)
tag_p = soup.find("p")
print(tag_p.string)     # compared with selenium, more \n and space
driver.quit()
