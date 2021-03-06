from sock import sendMessage


def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024).decode("utf-8")
        temp = (readbuffer + "\n").split()
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(s, "Successfully joined chat\r\n")


def loadingComplete(line):
    if ("End of /NAMES list" in line):
        return False
    else:
        return True