import socket

#Setup client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = b''
while True:
    chunk = s.recv(1024) #Receive data from chunk
    if not chunk:
        break
    full_msg += chunk

print(full_msg.decode("utf-8"))
s.close()
