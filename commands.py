import sys
import os
import discord
import random

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

    multiLineCode = 0
    miltiLineChannels = []


    async def spam(client, message, text):
            output = text[1]
            for x in range(int(text[2])):
                #output = output + "\n" + text[1]
                await message.channel.send(output)
            return

    async def a(client, message, text):
        print("a")
        return

    async def meowwoem(client, message, text):
        await message.channel.send("https://media.discordapp.net/attachments/736362433634893924/746391689123594341/image0-5-2.gif")
        await message.channel.send("https://media.discordapp.net/attachments/736362433634893924/746391689421258912/image0-3-1.gif")
        return

    async def mock(client, message, text):
        output = ''.join(random.choice((str.upper, str.lower))(c) for c in text[1])
        await message.channel.send(output)
        return


    async def restart(client, message, text):
        command = sys.executable +" "+ '"'+os.path.join(os.getcwd(), "main.py"+'"')
        print(command)
        await message.channel.send("Restarting...\n```"+command+"```")
        await message.channel.send("https://c.tenor.com/2kYfZmX6v6UAAAAC/stairs-da.gif")
        os.system(command)
        sys.exit("Process restarting")

