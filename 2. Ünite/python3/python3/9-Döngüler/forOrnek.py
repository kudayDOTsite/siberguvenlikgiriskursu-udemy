sifre = input("LÜtfen şifrenizi giriniz\r\n")

trHarfler = "işçöğü"

for harf in trHarfler:
	if(harf in sifre):
		print("Türkçe harfler kullanmayınız")

