import discord
import commands
import os


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