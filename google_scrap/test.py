import requests
from bs4 import BeautifulSoup

url = 'https://www.gooogle.com/'

res = requests.get(url)
res.raise_for_status()
html = res.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)
