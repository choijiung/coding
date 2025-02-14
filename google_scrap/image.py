import requests
from bs4 import BeautifulSoup
import time
import csv
import os
from PIL import Image  # 추가

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

url = "https://www.google.com/search?q=Chatgpt&sca_esv=4be518e6148afb1c&sxsrf=AHTn8zox_hdlFOp9eNIN-M2bXx5Jos2P0A:1739432387730&ei=w6GtZ8eWLNGSvr0PuPjfiAI&start=00&sa=N&sstk=Af40H4UNaTiWexFwHapDDO605ma911LWzaYTpEI6ReS2hlhOZJDPjGb21WesgSoqs9TZ5A5ah3zhGzF-WSOQfqktsgVonIXB8Ggeso2GNWbxlEHg_1GAdQO8O_uoE9UdWVxt&ved=2ahUKEwiHhNPMksCLAxVRia8BHTj8FyE4HhDy0wN6BAgGEAY&biw=1440&bih=812&dpr=2"
    
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
scraped = soup.find_all("span", attrs = {"jscontroller" : "msmzHf"})
# title = scraped.h3.get_text()
# link = scraped.a["href"]
print(scraped)
# print(title)
# print(link)

# for i in range(1, 6):
#     url = "https://www.google.com/search?q=Chatgpt&sca_esv=4be518e6148afb1c&sxsrf=AHTn8zox_hdlFOp9eNIN-M2bXx5Jos2P0A:1739432387730&ei=w6GtZ8eWLNGSvr0PuPjfiAI&start={}0&sa=N&sstk=Af40H4UNaTiWexFwHapDDO605ma911LWzaYTpEI6ReS2hlhOZJDPjGb21WesgSoqs9TZ5A5ah3zhGzF-WSOQfqktsgVonIXB8Ggeso2GNWbxlEHg_1GAdQO8O_uoE9UdWVxt&ved=2ahUKEwiHhNPMksCLAxVRia8BHTj8FyE4HhDy0wN6BAgGEAY&biw=1440&bih=812&dpr=2".format(i-1)
    
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")

#     scraped = soup.find_all("div", attrs = {"class" : "yuRUbf"})
#     for scrap in scraped:
#         title = scrap.h3.get_text()
#         link = scrap.a["href"]
#         currnt_time = time.strftime("_%Y%m%d_%H%M%S")

#         print(title + link)
#         name = "/Users/Jiung/Documents/GitHub/coding/google_scrap/scrap{}.txt".format(currnt_time)
#         with open(name, "a", encoding = 'utf-8') as f:
#             f.write("\n제목ㅁ : " + title + "\n링크 : " + link + "\n")

#         print(title + link)