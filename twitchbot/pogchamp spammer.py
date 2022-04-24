import socket
import time
HOST = "irc.twitch.tv"
PORT = 6667
NICK = "pee_nyss"
PASS = 'oauth:hf507zvoxyu6y9fwhstvglvzhr0jnf'
STREAM = "bentensmexicans"
i = 1
def send_message(message):
    s.send(bytes("PRIVMSG #" +STREAM+ " :"+ message + "\r\n", "UTF-8"))
    print("PRIVMSG #" +STREAM+ " :"+NICK+" " + message + "\r\n")

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + STREAM + " \r\n", "UTF-8"))


while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

for x in range(1, 3):
        if x % 2 == 0:
            send_message("PogChamp "*2)
            time.sleep(1.5)
        else:
            send_message("PogChamp ")
            time.sleep(1.5)
