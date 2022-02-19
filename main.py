import discord
import commands
import utils
import os

from time import sleep
print("Main starting...")
#sleep()


botPrefix = utils.getAttribute('botPrefix')
status = discord.Streaming(name="shreksophone",url="https://www.youtube.com/watch?v=pxw-5qfJ1dk&t=291s")






class botClient(commands.Commands):

    async def on_ready(self):
        await self.change_presence(activity=status)
        print('Logged in as {0.user}'.format(self))

        try:
            f = open("restart.tmp","r")
            channelID = f.read()
            print("Client got restarted from "+channelID)
            f.close()
            os.remove("restart.tmp")
            await self.get_channel(int(channelID)).send("```Restarted!```")
        except: FileNotFoundError

            


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
client.run(utils.getAttribute('token'))