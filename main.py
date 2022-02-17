import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!suffer'):
        await message.channel.send('pain')

def getToken():
    filepath = os.path.join(os.getcwd(), "token.txt")
    try:
        f = open(filepath)
    except FileNotFoundError:
        print("No Token found!\nPlease set new token:")
        token = input()
        f = open(filepath, "w+")
        f.write(token)
    finally:
         f.close()

    f = open(filepath, "r")
    token = f.read()
    f.close()
    return token

print("Building client...")
client.run(getToken())
