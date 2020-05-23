import requests

def tespit(url, dosya):
	data = open(dosya)
	wordlist = data.read().split("\n")
	print("Tespit edilen sayfalar:")
	for i in wordlist:
		istek = requests.get(url + "/" + i)
		statusCode = str(istek.status_code)
		if(statusCode[0] == "2"):
			print("+", istek.url)

def baslangic():
	url = input("Hedef sayfanın url adresi:")
	dosya = input("Kullanılacak olan wordlist dosayasının tam yolu:")
	onayMetni = "URL => " + url + "\r\nDosya =>" + dosya +"(e/h)"
	onay = input(onayMetni)
	if(onay.lower() != "e"):
		exit()
	tespit(url, dosya)


baslangic()
