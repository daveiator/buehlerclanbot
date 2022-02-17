from cgitb import text
import discord
import commands
import os
import string

client = discord.Client()

botPrefix = "!"


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(botPrefix):
        textMessage = message.content.split(botPrefix,1)[1]
        splitTextMessage = textMessage.split(" ")
        print("Imput detecteted: "+ textMessage +"\n Searching for command: "+splitTextMessage[0])
        try:
            outputMessage = getattr(commands, splitTextMessage[0])(splitTextMessage)
        except AttributeError:
            print("Command not found")
            outputMessage = "This command does not exist!"

        await message.channel.send(outputMessage)

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

def spam(a):
    print("a")

print("Building client...")
client.run(getToken())

#print(commands.dc("123p"))