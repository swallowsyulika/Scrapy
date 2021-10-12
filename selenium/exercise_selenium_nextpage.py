from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
import time

url = "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(url)

page_remaining = True
page_num = 1
while page_remaining:
    soup = BeautifulSoup(driver.page_source, "lxml")
    table = soup.select_one("body > main > div.stats-container__inner > div > div.row > div > div > nba-stat-table > div.nba-stat-table > div.nba-stat-table__overflow > table")
    df = pandas.read_html(str(table))
    df[0].to_csv("NBAplayer" + str(page_num) + ".csv")
    print("already save", page_num)
    try:
        next_link = driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]")
        next_link.click()
        time.sleep(3)
        if page_num < 11:
            page_num += 1
        else:
            page_remaining = False
    except Exception:
        page_remaining = False

driver.quit()
