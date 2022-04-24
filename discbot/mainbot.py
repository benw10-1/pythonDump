import discord

token = "NzM3NTI5ODYxNTcyMzk1MDA4.Xx-sNQ.tOyBX4FGbRhM7qkEBLnmCh0Qnyg"

client = discord.Client()

bb = client.guilds
print(bb)
for x in bb:
    print(x)
@client.event
async def on_ready():
    print("Online!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author)
    if message.content[:5] == "+move":
        message.content[1].moveto
client.run(token)
