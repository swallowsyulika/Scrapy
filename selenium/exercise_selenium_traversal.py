from selenium import webdriver
import os

driver = webdriver.Chrome("chromedriver")
path = "file:///" + os.path.abspath("index.html")   # from computer
driver.implicitly_wait(10)
driver.get(path)
# print(driver.title)    # test successful loading
# id
form = driver.find_element_by_id("loginForm")
print(form.tag_name)
print(form.get_attribute("id"))

# name
user = driver.find_element_by_name("username")
print(user.tag_name)
print(user.get_attribute("type"))

# elements return list
eles = driver.find_elements_by_name("continue")
for ele in eles:
    print(ele.get_attribute("type"))    # submit button
print('-'*20)

# xpath
f = driver.find_element_by_xpath("/html/body/form[1]")
print(f.tag_name)       # "//form[1]"   "//form[@id='loginForm']"
pwd = driver.find_element_by_xpath("//form/input[2][@name='password']")
print(pwd.get_attribute("type"))     # "//form[@id='loginForm']/input[2]"   "//input[@name='password']"
clear = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
print(clear.get_attribute("type"))   # "//form[@id='loginForm']/input[4]"

# link
link1 = driver.find_element_by_link_text('Continue')
print(link1.text)
link2 = driver.find_element_by_partial_link_text('Conti')
print(link2.text)
link3 = driver.find_element_by_link_text('取消')
print(link3.text)
link4 = driver.find_element_by_partial_link_text('取')
print(link4.text)

print('-'*20)
# class
content = driver.find_element_by_class_name("content")
print(content.text)

# css
cont = driver.find_element_by_css_selector("h3.content")
print(cont.text)
p = driver.find_element_by_css_selector("p")
print(p.text)

driver.quit()
