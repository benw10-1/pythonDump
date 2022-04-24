import socket
from riotwatcher import LolWatcher
api_key = 'RGAPI-6a7a070d-fbbe-4a78-9f95-d7bf33d749de'
watcher = LolWatcher(api_key)
my_region = 'na1'


def roman(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    return num

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "ashawabot"
PASS = 'oauth:6quxkxxu6l3d6uont08xur8fgtvnmk'
STREAM = "ashawa_"
i = 1
usercount = {}
usercount2 = {}

def send_message(message):
    s.send(bytes("PRIVMSG #" + STREAM + " :" + message + "\r\n", "UTF-8"))
    print("PRIVMSG #" + STREAM + " :" + NICK + " " + message + "\r\n")

def antispam(user):
    pass

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + STREAM + " \r\n", "UTF-8"))


while True:
    line = str(s.recv(1024))
    print(line)
    if "End of /NAMES list" in line:
        break

while True:
    recv = str(s.recv(1024))
    for line in recv.split('\\r\\n'):
        print(recv)
        parts = line.split(':')

        if len(parts) < 3:
            print(parts)
            continue

        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]


        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        try:
            print(username + ": " + message)
        except Exception as e:
            print(e)
            continue
        spamar = [x for x in message.split(" ")]
        try:
            usercount2[username]
        except KeyError:
            usercount2[username] = 0
        if len(message) > 250:
            usercount2[username] = usercount2[username]+1
        if usercount2[username] >= 3:
            usercount2[username] = 0
            send_message("/timeout {} 60".format(username))
        else:
            for x in message.split(" "):
                if spamar.count(x) >= 2:
                    try:
                        usercount[username]
                    except KeyError:
                        usercount[username] = 1
                        break
                    usercount[username] = usercount[username]+1
                    print (usercount[username])
                    if usercount[username] == 3:
                        send_message("/timeout {} 60".format(username))
                        usercount[username] = 0


        if message[:4] == "!pog":
            send_message("PogChamp "*5)


        if message[:5] == "!rank":
            try:
                me = watcher.summoner.by_name(my_region, 'Ashawa')
                my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
                for x in my_ranked_stats:
                    if x["queueType"] == 'RANKED_SOLO_5x5':
                        winrate = str((x["wins"] / (x["wins"] + x["losses"]) * 100).__round__(1)) + r"%"
                        tier = x["tier"][:1] + x["tier"][1:].lower()
                        rank = tier + " " + str(roman(x["rank"]))
                        LP = str(x["leaguePoints"])
                        print("Ashawa is {} at {} LP with a {} winrate".format(rank, LP, winrate))
                        send_message("Ashawa is {} at {} LP with a {} winrate".format(rank, LP, winrate))
            except Exception as e:
                send_message("This command is unavailable at the moment")
                print(str(e))

