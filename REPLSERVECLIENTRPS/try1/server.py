import socket
import threading
import random

s = socket.socket()
s.bind(("192.168.1.195", 8888))
RIP = "!STOP"
blacklist = []
connections = {}
codes = {"msg":"222", "challenge":"798", "error":"545", "throw":"877", "connectr":"133", "done": "099","aord":"344"}
challenges = {}
namechal = {}



with open("blacklist.txt", "r+") as file:
    for x in file.readlines():
        blacklist.append(str(x))
    file.close()
def rps(t1, t2):
    if t1 == t2:
        return 0
    if t1==1 and t2 ==2:
        return 2
    if t1==1 and t2 ==3:
        return 1
    if t1==2 and t2 ==1:
        return 1
    if t1==2 and t2 ==3:
        return 2
    if t1==3 and t2 ==1:
        return 2
    if t1==3 and t2 ==2:
        return 1


def handler(conn, addr):
    print("Thread started for {}".format(addr))
    while True:
        try:
            name = conn.recv(1024).decode("utf-8")
            if name not in [x for x in connections]:
                conn.send(bytes("!GOOD", "utf-8"))
                connections[name] = conn
                break

            else:
                conn.send(bytes("!BAD", "utf-8"))
        except:
            break
    if "!!!TEMP!!!" == name[:10]:
        print(name)
        aname = name[10:]
    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
        except:
            break

        if msg == RIP:
            break

        if msg[:3] == "798":
            if msg[3:] not in connections or msg[3:] in namechal:
                conn.send(bytes("545{}".format(msg[3:]),"utf-8"))

            else:
                conn.send(bytes("222Waiting for {} to accept your challenge!".format(msg[3:]), "utf-8"))
                connections[msg[3:]].send(bytes("798{}".format(msg[3:]), "utf-8"))
                namechal[msg[3:]] = name

        if msg[:3] == "133":
            conn.send(bytes("222{}".format([x for x in connections if x[:10]!="!!!TEMP!!!"]),"utf-8"))

        if msg[:3] == "222":
            for y in connections:
                connections[y].send(bytes("222{}:{}".format(name,msg[3:]),"utf-8"))
        if msg[:3] == "344":
            if msg[3:] == "y":
                connections[namechal[name]].send(bytes("344y","utf-8"))
                conn.send(bytes("344y","utf-8"))
                challenges["{}:{}".format(name,namechal[name])] = {name:None,namechal[name]:None}
            else:
                connections[namechal[name]].send(bytes("344n", "utf-8"))
                conn.send(bytes("344n", "utf-8"))
                namechal.pop(name)

        if msg[:3] == "877":
            for x in challenges:
                i = 0
                templst = []
                if aname in x.split(":"):
                    print("yer")
                    challenges["{}:{}".format(x.split(":")[0], x.split(":")[1])][aname] = int(msg[3:])
                    for y in challenges["{}:{}".format(x.split(":")[0], x.split(":")[1])]:
                        print(y)
                        if challenges["{}:{}".format(x.split(":")[0], x.split(":")[1])][y]:
                            i+=1
                        if i == 2:
                            print("yes")
                            for p in challenges["{}:{}".format(x.split(":")[0], x.split(":")[1])]:
                                templst.append(challenges["{}:{}".format(x.split(":")[0], x.split(":")[1])][p])
                            if rps(templst[0], templst[1]) == 1:
                                    for y in connections:
                                        connections[y].send(bytes("222{} won versus {}".format(x.split(":")[0], x.split(":")[1]), "utf-8"))
                                    for y in connections:
                                        if y == "!!!TEMP!!!{}".format(x.split(":")[0]) or y == "!!!TEMP!!!{}".format(x.split(":")[1]):
                                            connections[y].send(bytes("099","utf-8"))
                                    challenges.pop("{}:{}".format(x.split(":")[0], x.split(":")[1]))
                                    namechal.pop(x.split(":")[0])
                            elif rps(templst[0], templst[1]) == 0:
                                    for y in connections:
                                        connections[y].send(bytes("222{} tied versus {}".format(x.split(":")[1], x.split(":")[0]), "utf-8"))
                                    for y in connections:
                                        if y == "!!!TEMP!!!{}".format(x.split(":")[0]) or y == "!!!TEMP!!!{}".format(x.split(":")[1]):
                                            connections[y].send(bytes("099","utf-8"))
                                    challenges.pop("{}:{}".format(x.split(":")[0], x.split(":")[1]))
                                    namechal.pop(x.split(":")[0])
                            else:
                                for y in connections:
                                    connections[y].send(bytes("222{} won versus {}".format(x.split(":")[1], x.split(":")[0]), "utf-8"))
                                for y in connections:
                                    if y == "!!!TEMP!!!{}".format(x.split(":")[0]) or y == "!!!TEMP!!!{}".format(
                                            x.split(":")[1]):
                                        connections[y].send(bytes("099", "utf-8"))
                                challenges.pop("{}:{}".format(x.split(":")[0], x.split(":")[1]))
                                namechal.pop(x.split(":")[0])


                else:
                            conn.send(bytes("877","utf-8"))
                            break


        print("{}:\"{}\"".format(name, msg))

    connections.pop(name)
    conn.close()
    print("{} has disconnected!".format(addr[0]))
def strt():
    s.listen(10)
    print("Server is running on {}".format(socket.gethostname()))
    while True:
        conn, addr = s.accept()
        if addr in blacklist:
            conn.close()
            continue
        recv = conn.recv(1024).decode("utf-8")
        #not a regular client so noone can join without "code"
        if recv != "197884":
            conn.close()
        #if it is an rpsgame
        elif recv == "163411":
            pass
        #normal client
        else:
            t = threading.Thread(target=handler, args=(conn,addr))
            t.start()

strt()