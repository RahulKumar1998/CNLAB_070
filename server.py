from socket import *
servername="127.0.0.1"
serverPort=12000
serversocket=socket(AF_INET,SOCK_STREAM)
serversocket.bind((servername,serverPort))
serversocket.listen(1)
print("the server is ready to recieve")
while 1:
	connectionsocket,addr=serversocket.accept()
	sentence=connectionsocket.recv(1024).decode()
	file=open(sentence,"r")
	l=file.read(1024)
	connectionsocket.send(l.encode())
	file.close()
	connectionsocket.close()
