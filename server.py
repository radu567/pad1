import socket
import threading
import queue
import collections
import json

q = queue.Queue()

MESSAGE_TYPE = collections.namedtuple('MessageType', ('send', 'read'))(*('send', 'read'))

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsock = clientsock
        print("[+] New thread started for "+ip+":"+str(port))

    def run(self):
        print("Connection from : "+ip+":"+str(port))

#        clientsock.send("\nWelcome to the server\n\n")

        jsonObj = self.clientsock.recv(1024)
        while True:
            data = json.loads(jsonObj.decode('utf-8'))
            type = data.get('type')

            if type == MESSAGE_TYPE.read:
                if q:
                    m = q.get()
                    # print(m)   # comentat de radu
                    tcpsock.send(m.encode("utf-8"))
                    # tcpsock.send(m.str.encode())
                else:
                    tcpsock.send('Queue is empty')
            elif type == MESSAGE_TYPE.send:
                message = data.get('message')
                print('Mesaj:', message)
                q.put(message) # scriem datele primite in coada

                # print(q.get())  # Le afisam+

            data = self.clientsock.recv(1024)  # Citim urmatoarele 1024 bytes de la client
        clientsock.close()  # Inchidem conexiunea

        print("Client disconnected...")

host = "127.0.0.1"
port = 9999

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host, port))
threads = []


while True:
    tcpsock.listen(4)
    print("\nListening for incoming connections...")
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
