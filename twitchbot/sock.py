import socket
from setting import HOST, PORT, PASS, IDENT, CHANNEL


def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(bytes("PASS " + "PASS" + "\r\n","utf-8"))
    s.send(bytes("NICK " + "IDENT" + "\r\n","utf-8"))
    s.send(bytes("JOIN #" + " CHANNEL" + "\r\n","utf-8"))
    return s


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(bytes(messageTemp + "\r\n","utf-8"))
    print("Sent: " + messageTemp)