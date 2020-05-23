islem = input("LÜtfen yapmak istediğiniz işlemi seçiniz...\r\n" + 
"1-Toplama işlemi için\r\n" + 
"2-Çıkarma işlemi için\r\n" +
"3-Çarpma işlemi için\r\n" + 
"4-Bölme işlemi için seçeneklerininden birini seçerek ilerleyiniz...")

sayi1 = int(input("Sayı 1:"))
sayi2 = int(input("Sayı 2:"))

if(islem == "1"):
	print("Cevap:",end=" ")
	print(sayi1 + sayi2)
elif(islem == "2"):
	print("Cevap:",end=" ")
	print(sayi1 - sayi2)
elif(islem == "3"):
	print("Cevap:",end=" ")
	print(sayi1 * sayi2)
elif(islem == "4"):
	print("Cevap:",end=" ")
	print(sayi1 / sayi2)
else:
	print("Yanlış bir işlem yaptınız.\r\nProgramdan çıkılıyor")
	exit()
