import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New thread started for "+ip+":"+str(port))

    def run(self):
        print("Connection from : "+ip+":"+str(port))

#        clientsock.send("\nWelcome to the server\n\n")

        data = clientsock.recv(1024)
        list1 = []
        i = 1

        while data:  # Atit timp cit sunt date
            print(data)  # Le afisam
            list1[i].append(data)

            if data:
                i += 1
                clientsock.send(list1)
                clientsock.close()
            data = clientsock.recv(1024)  # Citim urmatoarele 1024 bytes de la client
        clientsock.close()  # Inchidem conexiunea

        print("Client disconnected...")

host = "0.0.0.0"
port = 9999

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host, port))
threads = []



while True:
    tcpsock.listen(4)
    print("\nListening for incoming connections...")
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
