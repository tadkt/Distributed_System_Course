import socket

def sendfile(client_socket, filename):
    try:
        with open(filename, 'rb') as file:
            chunk = file.read(1024)  
            while chunk:
                client_socket.send(chunk)
                chunk = file.read(1024)
        client_socket.send(b'EOF')  # Send end-of-file marker
    except FileNotFoundError:
        error_message = f"Error: File '{filename}' not found."
        print(error_message)  
        client_socket.send(bytes(error_message, "utf-8"))  
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Server setup
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    print("Server is listening...")
    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")

        # Receive filename from client
        filename = clientsocket.recv(1024).decode('utf-8')
        print(f"Client requested file: {filename}")

        # Send file
        sendfile(clientsocket, filename)

        clientsocket.close()
def receivefile(client_socket,filename):
    with open(filename, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if data == b'EOF':  # Check for end-of-file marker
                break
            f.write(data)
    print(f"File received successfully: {filename}")
if __name__ == "__main__":
    main()
