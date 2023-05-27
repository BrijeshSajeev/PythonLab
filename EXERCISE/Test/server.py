import socket

host = "127.0.0.1"
port = 5003

client_socket = socket.socket()

client_socket.connect((host, port))

while True:
    data = input("Enter message : ")
    client_socket.send(data.encode())

    if data.lower() == "exit":
        break

    response = client_socket.recv(1024).decode()
    print("Received from server:", response)

client_socket.close()
