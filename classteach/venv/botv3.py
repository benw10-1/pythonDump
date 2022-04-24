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
                #print (mems)

        guildlist.append(str(i)+ ". "+str(guild) + " (guild " + str(guild.id) + ")\n" + str(guildmems).replace("[","").replace("'","").replace("]","") + "\n" )
        i+=1

    #print(f'{client.user} has connected to Discord!\n'
          #f'{"".join(guildlist)}'
          #)

blacklist = ["7473", "3236","5122", "9282", "6910"]
dict1 = {}
@client.event

async def on_message(message):
    if message.author == client.user:

        return

    if message:
        await message.channel.send(":crab: VALORANT is DEAD :crab:")

        #3236 luke id
        #5122 shane id



client.run(TOKEN)