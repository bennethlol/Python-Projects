import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.137.248', 9999))

client.send('Message from client.'.encode())
print(client.recv(1024))