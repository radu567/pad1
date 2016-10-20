import socket
import json
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999
s.connect((host, port))


while True:
    data = {
        'type': 'read',
        'message': ''
    }
    jsonObj = json.dumps(data).encode('utf-8')
    s.send(jsonObj)
    message = s.recv(1024).decode('utf-8')
    print(message)

# s.close()
