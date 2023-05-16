import socket

host='127.0.0.1'
port=5002
server=socket.socket()
server.bind((host,port))
server.listen()

conn,addr=server.accept()
print("Connnection estabilished from "+str(addr))

while True:
    msg=conn.recv(1024).decode()
    print("Message From Client " + str(msg))
    if str(msg)=='bye':
        print("Connection terminated....")
        conn.close()
        break
    text=input("Enter Msg >>> ")
    conn.send(text.encode())

server.close()