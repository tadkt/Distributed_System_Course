import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#ivp4,for streaming
s.connect((socket.gethostname(),1234)) 
msg = s.recv(1024) #buffer memory
print(msg.decode("utf-8"))