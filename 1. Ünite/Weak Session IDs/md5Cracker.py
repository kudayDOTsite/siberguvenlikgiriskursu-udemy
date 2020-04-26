import hashlib

kirilacakHash = input("[*] Kırılacak Hash'i Giriniz:\r\n")
wordlistPath = input("[*] Wordlist Dosyasını Giriniz:\r\n")

dosya = open(wordlistPath, encoding="ISO-8859-1")
wordlist = dosya.read()
wordlist = wordlist.split("\n")
for i in wordlist:
	if(kirilacakHash == hashlib.md5(i.encode("utf-8")).hexdigest()):
		print("[*] Hash Başarılı Bir Şekilde Kırıldı!")
		print(i,":",kirilacakHash)
		exit()
