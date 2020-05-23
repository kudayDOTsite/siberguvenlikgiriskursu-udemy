sifre1 = input("Lütfen yeni şifrenizi giriniz:")
sifre2 = input("Lütfen şifrenizi tekrar giriniz:")

if(sifre1 == sifre2):
	if(len(sifre1) < 4):
		print("Şifreniz 4 karakterden daha büyük olmalıdır")
	else:
		print("Şifreniz değiştirildi.")
else:
	print("Şifreleriniz uyuşmamaktadır.")
