import socket
def client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#ivp4,for streaming
    client.connect((socket.gethostname(),1234)) 
    file = input("Filename: ")
    client.sendall(file.encode())
    with open(f"downloaded_{file}","wb") as f:
        while True: 
            data = client.recv(1024)
            if not data:
                break
            f.write(data)
    print("Original file: ",file) 
    print("File on my pc: ",f"downloaded_{file}")

if __name__ == "__main__":
    client()

