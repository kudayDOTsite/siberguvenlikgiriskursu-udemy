#Bu python dosyası kullanıcıdan alınan veri ile alan ve çevre hesaplaması yapmaktadır

pi = 3.14

r = int(input("[*] Yarıçap değerini giriniz.\r\n")) #kullanıcıdan alınan veri int tipine dönüştürülmüştür int()

cevre = 2 * pi * r

alan = pi * r * r

print("Dairenin çevresi:", cevre)
print("Dairenin alanı:", alan)
