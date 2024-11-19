import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ivp4,for streaming
s.connect((socket.gethostname(),1234)) # We are not binding anymore because this is client now

full_msg = ''
while True: # We need to consistently receive the data
    msg = s.recv(8) # Buffer memory, decice how big a chunk of data maximum we want at a time
    if len(msg) <= 0:
        break # End if no more message
    full_msg += msg.decode("utf-8") # Connect all msg together
print(full_msg)