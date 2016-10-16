import threading
from threading import Thread
import socket
import select
import queue
import sys


# Tratare mesaje primite
class ProcessThread(Thread):
    def __init__(self):
        super(ProcessThread, self).__init__()
        self.running = True
        self.q = queue.Queue()

    def add(self, data):
        self.q.put(data)

    def stop(self):
        self.running = False

    def run(self):
        q = self.q
        while self.running:
            try:
                # block for 1 second only:
                value = q.get(block=True, timeout=1)
                process(value)
            except queue.Empty:
                sys.stdout.write('.')
                sys.stdout.flush()
        #
        if not q.empty():
            print("Elements left in the queue:")
            while not q.empty():
                print(q.get())


t = ProcessThread()
t.start()
