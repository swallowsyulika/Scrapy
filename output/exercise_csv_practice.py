import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.w3schools.com/html/html_media.asp'
csvfile = "Execise.csv"
r = requests.get(url)
r.encoding = 'utf8'
soup = BeautifulSoup(r.text, 'lxml')
tag_table = soup.find(class_="w3-table-all")
rows = tag_table.find_all("tr")
with open(csvfile, "w+", newline='', encoding='utf8') as wt:    # remember encoding
    writer = csv.writer(wt)
    for row in rows:
        rowlist = []
        for cell in row.find_all(["th", "td"]):     # get_text() == a.text
            rowlist.append(cell.get_text().replace("\n", "").replace("\r", ""))
        writer.writerow(rowlist)
