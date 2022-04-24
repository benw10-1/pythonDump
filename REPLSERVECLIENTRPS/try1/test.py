import socket
import sys
import threading
import time
import os
import subprocess

def openscr(arg):
    console = ['cmd.exe', '/c', 'start']
    script = os.getcwd() + r"\rpssub.py"
    cmd = ['python', script, arg]
    return subprocess.Popen(console + cmd)
try:
    c = socket.socket()
    c.connect((socket.gethostname(), 8888))
    c.send(bytes("197884", "utf-8"))
except:
    print("The server is not up or you are not connected to the internet!")
    sys.exit()
while True:
    name = input("Enter name: ")
    c.send(bytes(name, "utf-8"))
    recv = c.recv(2048).decode()
    if recv == "!GOOD":
        print("Good to go!")
        break
    print("Name already chosen!")

def sender():
    while True:
        try:
            time.sleep(.3)
            inp = input(": ")
            if inp[:6] == "!chal ":
                inp = "798" + inp[6:]
                c.send(bytes(inp, "utf-8"))
                continue
            if inp == "!y":
                c.send(bytes("344y", "utf-8"))
                continue
            if inp == "!n":
                c.send(bytes("344n", "utf-8"))
                continue
            if inp.lower() == "connected":
                c.send(bytes("133", "utf-8"))
                continue
            else:
                inp = "222" + inp
                c.send(bytes(inp, "utf-8"))
        except Exception as e:
            print(e)

def receiver():
    while True:
        try:
            recv = c.recv(2048).decode()
            if recv[:3] == "798":
                print("{} has challenged you! Type !y to accept or !n to decline!".format(recv[3:]))

            if recv[:3] == "545":
                print("{} is not online or is in a challenge!".format(recv[3:]))
            if recv[:3] == "222":
                print (recv[3:])
            if recv[:3] == "344":
                if recv[3:] == "y":
                    openscr(name)
                else:
                    print("Challange declined!")
        except Exception as e:
            print(e)
            time.sleep(5)


def strt():
    t = threading.Thread(target=receiver)
    t.start()
    sender()


strt()











