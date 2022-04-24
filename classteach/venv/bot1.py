import os

import discord, random




TOKEN = 'NzEyMTM5MjU2ODcyNTY2ODc0.XsNViA.EYJViq7RmQ8Yn2duSrmRxnCv3sM'

client = discord.Client()



@client.event

async def on_message(message):


    msg = ""
    if message.author == client.user:

        return

    if message.content == "F":

        await message.channel.send("F")

        #3236 luke id
        #5122 shane id



client.run(TOKEN)