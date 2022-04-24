import socket
import threading

connections = []


def handler(conn, addr):
    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
            print (msg)
        except:
            break
        for x in connections:
            x.send(f"{addr[0]}: {msg}".encode("utf-8"))


def start():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind((socket.gethostname(), 8888))

   s.listen(5)

   while True:
       conn, addr = s.accept()
       t = threading.Thread(target=handler, args=(conn, addr))
       t.start()


start()