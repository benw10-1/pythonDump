try:
    import socket
    import sys
    import threading
    import time

    throwar = ["rock", "paper", "scissors"]
    c = socket.socket()
    c.connect(("107.202.105.8", 8888))
    print(str(c))
    c.send(bytes("197884", "utf-8"))
    c.send(bytes("!!!TEMP!!!{}".format(sys.argv[1]),"utf-8"))
    print ('yes')
    def sender():
        while True:
            try:
                inp = input("Enter throw: ")
                if inp.lower() in throwar:
                    if inp.lower() == "rock":
                        c.send(bytes("8771","utf-8"))
                    if inp.lower() == "paper":
                        c.send(bytes("8772", "utf-8"))
                    if inp.lower() == "scissors":
                        c.send(bytes("8773", "utf-8"))
                    print ("Throw sent!")
                    break
                else:
                    print("Invalid throw!")
            except Exception as e:
                print(str(e))
    def reciever():
        while True:
            try:
                rec = c.recv(2048).decode()
                if rec[3:] == "877":
                    print ("Waiting for {}!".format(rec[:3]))
                if rec[3:] == "099":
                    break
            except:
                print("Disconnected | Type anything to exit")
                break

    def strt():
        t = threading.Thread(target=reciever)
        sender()
    strt()
except Exception as e:
    with open("log.txt", "w+") as file:
        file.write(str(e))

