from socket import *
servername="10.124.7.89"
serverport=12000
clientsocket=socket(AF_INET,SOCK_DGRAM)
sentence=input("enter file name")
clientsocket.sendto(bytes(sentence,"utf-8"),(servername,serverport))
filec.serverAddress=clientsocket.recvfrom(2048)
print("from server:",filec)
clientsocket.close()
