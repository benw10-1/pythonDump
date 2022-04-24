import string
from read import getUser, getMessage
from sock import openSocket, sendMessage
from init import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    readbuffer = str(readbuffer) + str(s.recv(1024).decode("utf-8"))
    temp = (readbuffer+ "\n").split()
    readbuffer = temp.pop()

    for line in temp:
        print(line)
        if "PING" in line:
            s.send(line.replace("PING", "PONG\r\n"))
            break
        user = getUser(line)
        message = getMessage(line)
        print(user + " typed :" + message)
        sendMessage(s, "Lol\r\n")