# server.py
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 9999
s.bind((host, port))

s.listen(10)

while True:
    clientsocket, addr = s.accept()

    print("Got a connection from %s" % str(addr))
    print('client addr: ', addr)

    data = clientsocket.recv(1024)

    if not data:
        clientsocket.close()
        break
    else:
        print(data)
    continue
