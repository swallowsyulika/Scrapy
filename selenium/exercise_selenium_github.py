from selenium import webdriver

url = "https://github.com/login"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(url)

username = "swallowsyulika"
password = "swallowsyulika0210"
user = driver.find_element_by_css_selector("#login_field")
user.send_keys(username)
pwd = driver.find_element_by_css_selector("#password")
pwd.send_keys(password)
button = driver.find_element_by_css_selector("input[type='submit']")
button.click()

items = driver.find_elements_by_xpath("//header/div[3]/nav/a")
for item in items:
    if item.text == "":
        pass
    else:
        print(item.text)
        print(item.get_attribute("href"))
driver.quit()

