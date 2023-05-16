import socket

host='127.0.0.1'
port=5002

client = socket.socket()
client.connect((host,port))
data=input('Enter msg >> ')


while str(data)!='bye':
    client.send(data.encode())
    msg=client.recv(1024).decode()
    print("Recieved msg >> "+str(msg))
    data=input('Enter msg >> ')
    client.send(data.encode())

print("Connection terminated")
client.close()
