# client.py
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 9999
s.connect((host, port))

while True:

    data = input('write to server: ')
    if not data:
        s.close()

    data = str.encode(data)
    s.send(data)

tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
