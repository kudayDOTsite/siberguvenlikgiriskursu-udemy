from bs4 import BeautifulSoup
from bs4 import Comment
import requests

url = input("[*] Hedef sistemin URL adresini giriniz:\r\n")
istek = requests.get(url)
html = istek.text
soup = BeautifulSoup(html, "lxml")
comment = soup.findAll(text = lambda text: isinstance(text, Comment))
for i in comment:
	print(i)
