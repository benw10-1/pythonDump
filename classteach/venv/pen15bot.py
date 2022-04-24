import os

import discord, random




TOKEN = 'NzEyMTM5MjU2ODcyNTY2ODc0.XsNViA.EYJViq7RmQ8Yn2duSrmRxnCv3sM'

client = discord.Client()
guildlist = []
guildmems = []

@client.event

async def on_ready():
    i=1
    for guild in client.guilds:
        for mems in guild.members:
            if str(mems) != str(client.user) and not mems.bot:
                guildmems.append(str(mems))
                print (mems)

        guildlist.append(str(i)+ ". "+str(guild) + " (guild " + str(guild.id) + ")\n" + str(guildmems).replace("[","").replace("'","").replace("]","") + "\n" )
        i+=1

    print(f'{client.user} has connected to Discord!\n'
          f'{"".join(guildlist)}'
          )

blacklist = ["7473", "3236","5122", "9282", "6910"]

@client.event

async def on_message(message):
    guildmems = []
    guildids = []
    list1 = []
    msg = ""
    if message.author == client.user:

        return

    if message.content == "8=D":
        i=0
        for guild in client.guilds:
            for mems in guild.members:

                if str(mems) != str(client.user) and not mems.bot:
                    guildmems.append(str(i)+"."+str(mems))

                    print(mems)
            guildids.append(str(guild.id))
            i+=1

        print (guildids)
        index = str(guildids.index(str(message.guild.id)))+"."
        stripper = index
        for k in guildmems:
            if index in k:
                if k[len(k)-4:] in blacklist:
                    list1.append(k.split("#")[0].strip(stripper).strip("\n")+" sorrybruh1223344111")
                else:
                    list1.append(k.split("#")[0].strip(stripper).strip("\n"))
        p = 0
        for m in list1:
            if "sorrybruh1223344111" in m:
                msg = msg + m.strip("sorrybruh1223344111") + ": "+str(random.choice(range(2, 4))) + ' inches\n'
            else:
                msg = msg + m + ": "+str(random.choice(range(8,15))) + ' inches\n'
            if p > 55:
                break
            p+=1

        await message.channel.send("Peen lengths \n"+ msg)

        #3236 luke id
        # 5122 shane if



client.run(TOKEN)