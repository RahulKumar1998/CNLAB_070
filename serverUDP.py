from socket import *
serverport=12000
serversocket=socket(AF_INET,SOCK_DGRAM)
serversocket.bind(("10.124.7.89",serverport))
print("the server is ready to recieve")
while 1:
	sentence,clientadd=serversocket.recvfrom(2048)
	file1=open(sentence,"r")
	l=file1.read(2048)
	serversocket.sendto(bytes(l,"utf-8"),clientadd)
	print("SENT back to client", l)
	file1.close()
