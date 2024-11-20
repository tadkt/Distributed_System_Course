import socket # Socket is the endpoint that send and receive data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ivp4,for streaming
s.bind((socket.gethostname(), 1234)) # Host the server on the same machine that we have the code
s.listen(5) # Prepare for multiple connection in the queue of 5
while True:
    clientsocket, address = s.accept() # https://docs.python.org/3/library/socket.html#socket.socket.accept
    # "clientsocket" is a new socket object usable to send and receive data on the connection, and "address" is the address bound to the socket on the other end of the connection
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server","utf-8")) # Send the information to the clientsocket (a bit weird pls remember)
    clientsocket.close() # Close whenever clientsocket is done sending