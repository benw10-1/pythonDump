
from riotwatcher import LolWatcher, ApiError

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


# golbal variables
api_key = 'RGAPI-320f5b8c-374d-4f4e-92b4-557bbc7af791'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'wildcard260')
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

for x in my_ranked_stats:
    if x["queueType"] == 'RANKED_SOLO_5x5':
        winrate = str((x["wins"] / (x["wins"] + x["losses"]) * 100).__round__(1)) + r"%"
        tier = x["tier"][:1] + x["tier"][1:].lower()
        rank = tier + " " + str(roman(x["rank"]))
        LP = str(x["leaguePoints"])
        print("{} is {} at {} LP with a {} winrate".format(me["name"],rank, LP, winrate))

