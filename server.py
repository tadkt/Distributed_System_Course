import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#ivp4,for streaming
s.bind((socket.gethostname(),1234))
s.listen(5)#queue of 5
while True:
    clientsocket, address = s.accept() #another socket object, address of client
    print("Connection from", address, "has been established")
    clientsocket.send(bytes("Welcome","utf-8"))
    clientsocket.close()