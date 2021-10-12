from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")   # ./chromedriver
time.sleep(5)
driver.quit()

