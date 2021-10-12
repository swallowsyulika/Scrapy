from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os

driver = webdriver.Chrome("chromedriver")
path = "file:///" + os.path.abspath("index.html")   # from computer
driver.implicitly_wait(10)
driver.get(path)
try:
    content = driver.find_element_by_css_selector("h2.content")
    print(content.text)
except NoSuchElementException:
    print("nonexistent")
driver.quit()

