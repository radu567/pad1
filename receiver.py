# client.py
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 9999
s.connect((host, port))

while True:

    data = data = s.recv(1024)
    # if not data:
    #     s.close()

    data = str.decode(data)
    print(data)


s.close()