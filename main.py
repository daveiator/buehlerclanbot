import discord
import commands
import os
from time import sleep
print("Startup in t 2")
sleep(2)


botPrefix = "!"
status = discord.Streaming(name="shreksophone",url="https://www.youtube.com/watch?v=pxw-5qfJ1dk&t=291s")

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



class botClient(commands.Commands):

    async def on_ready(self):
        await self.change_presence(activity=status)
        print('Logged in as {0.user}'.format(self))


    async def on_message(self, message):
        
        if message.author == self.user:
            return

        if self.multiLineCode:
            splitTextMessage = message.content.split(" ")
            print("2")
            for i in range(len(self.multiLineChannels)):
                thisChannel = self.multiLineChannels[i]
                if message.channel == thisChannel[0]:
                    print("Multiline Input detected in"+message.channel.name+" : "+message.content)
                    await getattr(self, thisChannel[1])(message,splitTextMessage)

        if message.content.startswith(botPrefix):
            textMessage = message.content.split(botPrefix,1)[1]
            splitTextMessage = textMessage.split(" ")
            print("Imput detecteted: "+ textMessage +"\n Searching for command: "+splitTextMessage[0])
            try:
                await getattr(self, splitTextMessage[0])(message,splitTextMessage)
            except AttributeError:
                print("Command not found")
                await message.channel.send("This command does not exist!")


print("Building client...")
client = botClient()
client.run(getToken())