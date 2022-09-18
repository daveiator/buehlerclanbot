import discord
import commands
import logging
import os
from dotenv import load_dotenv
from time import sleep

def main():
    print("Main starting...")
    # Starting logging
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info("Started logging")

    # Load environment variables
    load_dotenv()

    # reddit.init()

    global botPrefix 
    botPrefix = os.getenv("BOT_PREFIX")
    global status 
    status = discord.Streaming(name="shreksophone",url="https://www.youtube.com/watch?v=pxw-5qfJ1dk&t=291s")


    logging.info("Starting bot")
    client = botClient()
    client.run(os.getenv("TOKEN"))




class botClient(commands.Commands):

    async def on_ready(self):
        await self.change_presence(activity=status)
        logging.info('Logged in as {0.user}'.format(self))

        try:
            f = open("restart.tmp","r")
            channelID = f.read()
            logging.info("Client got restarted from "+channelID)
            f.close()
            os.remove("restart.tmp")
            await self.get_channel(int(channelID)).send("```Restarted!```")
        except: FileNotFoundError

            


    async def on_message(self, message):
        
        if message.author == self.user:
            return

        if self.multiLineCode:
            splitTextMessage = message.content.split(" ")
            logging.debug(msg)("2")
            for i in range(len(self.multiLineChannels)):
                thisChannel = self.multiLineChannels[i]
                if message.channel == thisChannel[0]:
                    logging.info("Multiline Input detected in"+message.channel.name+" : "+message.content)
                    await getattr(self, thisChannel[1])(message,splitTextMessage)

        if message.content.startswith(botPrefix):
            textMessage = message.content.split(botPrefix,1)[1]
            splitTextMessage = textMessage.split(" ")
            logging.info("Imput detecteted: "+ textMessage +"\n Searching for command: "+splitTextMessage[0])
            try:
                await getattr(self, splitTextMessage[0])(message,splitTextMessage)
            except AttributeError:
                logging.info("Command not found")
                await message.channel.send("This command does not exist!")

if __name__ == "__main__":
    main()
