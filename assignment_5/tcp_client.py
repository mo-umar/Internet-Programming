from datetime import datetime

import socket
address = ('localhost', 6789)
max_size = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.send(str(datetime.now()).encode())
data = client.recv(max_size).decode()
print('At', datetime.now(), 'some one replied', 'said', data)
client.close()