import discord
import asyncio
from stuff import reddit
from tasks import gaming
import logging
import os
from dotenv import load_dotenv
import re

def main():
    # Starting logging
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info("Started logging")

    # Load environment variables
    load_dotenv()

    # Starting reddit API
    reddit.init()

    global botPrefix 
    botPrefix = os.getenv("BOT_PREFIX")
    global status 
    #status = discord.Streaming(name="shreksophone",url="https://www.youtube.com/watch?v=pxw-5qfJ1dk&t=291s")
    #status = discord.Streaming(name="huh?", url="https://www.youtube.com/watch?v=4kEO7VjKRB8")
    status = discord.Streaming(name="bibletime", url="https://www.youtube.com/watch?v=GTh5J0HsIAg")

    logging.info("Starting bot")
    intents = discord.Intents.all()
    intents.members = True
    bot = discord.ext.commands.Bot(command_prefix=botPrefix, intents=intents)

    for filename in os.listdir('./commands'):
        if filename.endswith('.py') & (filename != "__init__.py"):
            extentinon = f'commands.{filename[:-3]}'
            logging.info(f"Loading extention {filename}")
            bot.load_extension(extentinon)

    bot.add_cog(gaming.GamingTimeChecker(bot))

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=status)
        logging.info('Logged in as {0.user}'.format(bot))

        try:
            f = open("restart.tmp","r")
            channelID = f.read()
            logging.info("Client got restarted from "+channelID)
            f.close()
            os.remove("restart.tmp")
            await bot.get_channel(int(channelID)).send("```Restarted!```")
        except: FileNotFoundError

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        # Reaction Emotes
        from stuff import filters
        
        if re.search('.+us\\b', message.content):
            await message.add_reaction(discord.utils.get(bot.emojis, name="amogus"))
        else:
            for sus in filters.sus_list:
                if sus in message.content:
                    await message.add_reaction(discord.utils.get(bot.emojis, name="amogus"))
        
        for direct in filters.direct_emotes:
            if direct in message.content:
                await message.add_reaction(discord.utils.get(bot.emojis, name=direct))
        
        # Gaming Shut up
        from tasks import gaming
        await gaming.shut_up(bot, message)

        await bot.process_commands(message)
    
    bot.run(os.getenv("TOKEN"))
"""


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
        """
if __name__ == "__main__":
    main()
