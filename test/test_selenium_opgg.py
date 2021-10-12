from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
summoner = input()
print(summoner)
print("-"*20)
url = "https://tw.op.gg/"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.get(url)

name = driver.find_element_by_name("userName")
name.send_keys(summoner)
name.send_keys(Keys.ENTER)
button = driver.find_element_by_id("SummonerRefreshButton")
if button.text == "戰績更新":
    button.click()
    time.sleep(5)
games = driver.find_elements_by_class_name("GameItemWrap")
for game in games:
    print(game.find_element_by_class_name("GameType").text, end=" ")
    print(game.find_element_by_class_name("GameResult").text, end=" ")
    print(game.find_element_by_class_name("GameLength").text)
    cp = game.find_element_by_class_name("ChampionName")
    print(cp.find_element_by_css_selector("[target=_blank]").text, end=" ")
    KDA = game.find_element_by_class_name("KDA")
    KDA2 = KDA.find_element_by_class_name("KDA")
    kda = KDA2.find_elements_by_tag_name("span")
    for ele in kda:
        print(ele.text, end=" ")
    print("")
    print("-"*20)
driver.quit()
