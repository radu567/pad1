# client.py
import socket
import json

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999
s.connect((host, port))

while True:

    data = input('write to server: ')
    if not data:
        s.close()
    message = {
        'type': 'send',
        'message': str(data)
    }
    data = json.dumps(message).encode('utf-8')
    s.send(data)

s.close()
