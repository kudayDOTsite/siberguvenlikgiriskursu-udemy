sayi = input("Bir sayı giriniz:")

try:
	print("Sayının 2'ye bölümü:", int(sayi)/0)
except ZeroDivisionError:
	print("Bir sayı 0'a bölünemez")
#except ValueError:
#	print("Lütfen bir sayı giriniz")
except:
	print("Beklenmeyen bir hata oldu...")
finally:
	print("Program kapatılıyor...")
	exit()
