import os

import discord, random

TOKEN = 'NzEyMzY2NzkxMzUxMDc0OTEw.XsQhgg.fe-3Fot1yiBl1tofLn90tg5wGBk'

client = discord.Client()


@client.event

async def on_message(message):
    msg = message.content
    yes1 = False
    yes = False
    split = list(msg.split("&"))
    print(split[1])
    limit=100
    if split[1] == "setlimit":
        try:
            message.channel.send(f"Current limit is {str(limit)}")

            limit = int(msg.split("&")[2].strip())
            msg = "Limit set to "+ str(limit)

            yes1 = True

        except:
            yes1 = True

            msg = "Use numbers retard"

    if split[1] == "spam":
        try:
            msg = (split[2].strip(" "))
            yes = True
            if int(split("&"))[3] > limit:
                msg = "Above limit doe"
                yes = False
                yes1 = True

        except:
            msg = "Use correct format"
            yes1 = True
            yes = False



    if yes1:
        await message.channel.send(msg)
    if yes:
        for x in range(0,int(msg.split("&"))[3]):
            await message.channel.send(msg)

client.run(TOKEN)