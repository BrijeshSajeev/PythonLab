import socket

host =input(str("Enter the host name >> "))
port=5002

client=socket.socket()

client.connect((host,port))
print("Connected...")

filename = input(str("Enter the file name to be transmitted as >> "))
file=open(filename,'wb')
file_data=client.recv(1024)
file.write(file_data)
print("Process Succesfully completed")
client.close()
file.close()




