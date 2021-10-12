from selenium import webdriver
import time

url = "https://tts-nptu.funday.asia/"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(url)

username = "cbe107037"
password = "cbe107037"

user = driver.find_element_by_css_selector("#email")
user.send_keys(username)
pwd = driver.find_element_by_css_selector("#password")
pwd.send_keys(password)
button = driver.find_element_by_css_selector("[onclick='login.submit();']")
button.click()

dv = driver.find_element_by_css_selector("#DV-0")
dv.click()
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"#STitle1"}
'''
div = driver.find_element_by_css_selector("#newsdiv")
player = driver.find_element_by_css_selector("#STitle1")
player.click()
'''

# driver.quit()
