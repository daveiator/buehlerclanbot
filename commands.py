import io
import sys
import os
import discord
import random
import subprocess
import reddit
import logging



class Commands(discord.Client):

    """
    def dc(expression):
        dcFilepath = "C:\\Program Files (x86)\\GnuWin32\\bin"
        tempdcFilepath = os.getcwd()+"\\tempdc.txt"
        expression = '"'+expression+'"'
        dcFilepath = '"'+dcFilepath+"\\dc.exe"+'"'+" -e "
        command = '"'+dcFilepath+expression+" > "+'"'+tempdcFilepath+'"'+'"'
        command = os.path.normcase(command)
        print(command)
        os.system(command)
        f = open(tempdcFilepath, "r")
        output = f.read()
        f.close()
        os.remove(tempdcFilepath)
        return output
    """
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.multiLineCode = 0
        self.multiLineChannels = []
        self.shutdownPermit = False

    def isAdmin(self, message):
            logging.warning("User "+str(message.author.id)+" is trying to acces admin functions")
            if message.author.id == int(os.getenv("ADMIN_ID")):
                logging.info("Admin command executed")
                return 1
            return 0


    async def spam(client, message, text):
            output = text[1]
            for x in range(int(text[2])):
                #output = output + "\n" + text[1]
                await message.channel.send(output)
            return
    """
    async def a(client, message, text):
        logging.debug("a")
        return
    """
    async def meowwoem(client, message, text):
        await message.channel.send("https://media.discordapp.net/attachments/736362433634893924/746391689123594341/image0-5-2.gif")
        await message.channel.send("https://media.discordapp.net/attachments/736362433634893924/746391689421258912/image0-3-1.gif")
        return

    async def mock(client, message, text):
        output = ''.join(random.choice((str.upper, str.lower))(c) for c in ' '.join(text[1:len(text)]))
        await message.channel.send(output)
        return


    async def reddit(client, message, text):
        output = reddit.subredditRand(text[1])
        # print(output)
        await message.channel.send(output)
        return
    
    async def shutdown(client, message, text):
        if(client.shutdownPermit or client.isAdmin(message)):
            try:
                match text[1]:
                    case "arm":
                        client.shutdownPermit = True
                        await message.channel.send("Shutdown armed!")
                        return
                    case "disarm":
                        client.shutdownPermit = False
                        await message.channel.send("Shutdown disarmed!")
                        return
                    case "cancel":
                        os.system("shutdown /a")
                        await message.channel.send("Shutdown disarmed!")
                        return
            except IndexError:
                t = 300
                os.system("shutdown /s /t "+ str(t) +' /c " "')
                await message.channel.send("Shutting down the host in "+ str(t) + " Seconds")
        return


    async def restart(client, message, text):
        command = sys.executable +" "+ '"'+os.path.join(os.getcwd(), "main.py"+'"')
        logging.debug(command)
        await message.channel.send("Restarting...")
        await message.channel.send("https://c.tenor.com/2kYfZmX6v6UAAAAC/stairs-da.gif")

        f = open("restart.tmp","w+")
        f.write(str(message.channel.id))
        f.close()
        os.system(command)
        sys.exit("Process restarting")

    async def terminal(client, message, text):
        if client.isAdmin(message):
            client.multiLineCode = client.multiLineCode + 1
            thisChannel = [message.channel, "terminalint"]
            client.multiLineChannels.append(thisChannel)
            logging.info("Starting terminal")
            await message.channel.send("Starting terminal")
            return
        await message.channel.send("Higher permissions required")
        return

    async def terminalint(client, message, text):
        if client.isAdmin(message):
            if message.content == "exit":
                client.multiLineCode = client.multiLineCode - 1
                for x in range(len(client.multiLineChannels)):
                    thisChannel = client.multiLineChannels[x]
                    if thisChannel[1] == "terminalint":
                        client.multiLineChannels.pop(x)
                        logging.info("Closed terminal")
                        await message.channel.send("Closed terminal")
            
            stdout = subprocess.Popen(message.content, shell=True, stdout=subprocess.PIPE).stdout
            output = stdout.read().decode("utf-8").strip("'b")
            output = "```\n"+output+"\n```"
            logging.debug(output)
            await message.channel.send(output)
            return
        await message.channel.send("Higher permissions required")
        return