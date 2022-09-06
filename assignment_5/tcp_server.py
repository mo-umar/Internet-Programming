from datetime import datetime

import socket
address = ('localhost', 6789)
max_size = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
client, addr = server.accept()
data = client.recv(max_size).decode()
print('At', datetime.now(), client, 'said', data)
client.sendall(datetime.now().isoformat().encode())
print('Are you talking to me?')
client.close()
server.close()
