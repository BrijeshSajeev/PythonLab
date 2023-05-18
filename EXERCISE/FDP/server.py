import socket

host=socket.gethostname()
port=5002
server=socket.socket()
print(host)



server.bind((host,port))
server.listen(1)
conn,addr=server.accept()

filename=input(str("Enter the file name to be transmitted >> "))
file=open(filename,'rb')
file_data=file.read(1024)
conn.send(file_data)
conn.close()
file.close()
