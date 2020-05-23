def alan(yaricap, pi=3.14):
	return pi * yaricap ** 2

def cevre(yaricap, pi=3.14):
	return pi * yaricap * 2

try:
	yaricap = int(input("Ltfen yarıçapı giriniz:"))

	print("Dairenin alanı: {}".format(alan(yaricap)))
	print("Dairenin çevresi: {}".format(cevre(yaricap)))

except:
	print("Bir hata oldu!")
	exit()
finally:
	exit()
