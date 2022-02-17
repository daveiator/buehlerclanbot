import os
import discord

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

    async def spam(client, message, text):
            output = text[1]
            for x in range(int(text[2])):
                #output = output + "\n" + text[1]
                await message.channel.send(output)
            return

    async def a(client, message, text):
        print("a")
        return