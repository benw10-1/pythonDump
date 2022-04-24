import socket
import threading

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def rpsinput(self):
        self.sock.send(input(""))

    def __init__(self, address):
        self.sock.connect((address, 8888))

        iThread = threading.Thread(target=rpsinput)
        iThread.daemon= True
        iThread.start()