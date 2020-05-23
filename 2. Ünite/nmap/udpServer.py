import socket #socket kütüphanesi socket programlamada kuallnılan bir kütüphanedir

localIp = "127.0.0.1" #sunucumuzun IP adresi
port = 1822 #kullanacağımız port numarası

print("[*] UDP Server'a hoşgeldiniz.")

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #server kurallarını belirttik
#socket.AF_INET == IPv4 Kullancağımızı ve
#socket.SOCK_STREAM == TCP
#socket.SOCK_DGRAM == UDP

server.bind((localIp, port)) #dinlemeyi başlattık

print("[*] ",localIp,":",port," noktasında dinleeye başladı...",sep="")

while(1): #cevapları yakalamak ve iletişimi devam ettirebilmek için bir sonsuz föngü oluşturuyoruz
	data = server.recvfrom(1024)
	msg = data[0]
	clienIP =data[1][0]
	clientPort = data[1][1]
	print(clienIP,":",clientPort," ==> ", msg, sep="")
