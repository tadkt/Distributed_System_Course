import socket

def sendfile(client_socket, filename):
    try:
        with open(filename, 'rb') as file:
            chunk = file.read(1024)  
            while chunk:
                client_socket.send(chunk)
                chunk = file.read(1024)
    except Exception as e:
        print(f"An error occured: {e}")
    except FileNotFoundError:
        error_message = f"Error: File '{filename}' not found."
        print(error_message)  
        client_socket.send(bytes(error_message, "utf-8"))  

def main():
    # Server setup
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    print("Server is listening...")

    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")

        # Send file
        sendfile(clientsocket, "file.txt")

        clientsocket.close()

if __name__ == "__main__":
    main()
