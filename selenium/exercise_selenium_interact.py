from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
url = "https://www.google.com/"
driver.get(url)

keyword = driver.find_element_by_css_selector(".gLFyf")
keyword.send_keys("python")
keyword.send_keys(Keys.ENTER)

itrms = driver.find_elements_by_xpath("//div[@class='r']")
for item in itrms:
    h3 = item.find_element_by_tag_name("h3")
    print(h3.text)
    a = item.find_element_by_tag_name("a")
    print(a.get_attribute("href"))

driver.quit()
