from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.youtube.com/"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(url)

search = driver.find_element_by_css_selector("#search")
search.send_keys("搞神馬")
search.send_keys(Keys.ENTER)
items = driver.find_elements_by_css_selector("#video-title")

for item in items:
    print(item.get_attribute("aria-label"))
    print(item.get_attribute("href"))
print("共找到", len(items), "項")
driver.quit()

