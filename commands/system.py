from discord.ext import commands
import os
import sys
import logging

def setup(bot):
    bot.add_command(restart)

@commands.command()
async def restart(ctx):
    command = sys.executable +" "+ '"'+os.path.join(os.getcwd(), "main.py"+'"')
    logging.debug(command)
    await ctx.send("Restarting...")
    await ctx.send("https://c.tenor.com/2kYfZmX6v6UAAAAC/stairs-da.gif")
    f = open("restart.tmp","w+")
    f.write(str(ctx.channel.id))
    f.close()
    os.system(command)
    sys.exit("Process restarting")

def isAdmin(self, message):
            logging.warning("User "+str(message.author.id)+" is trying to acces admin functions")
            if message.author.id == int(os.getenv("ADMIN_ID")):
                logging.info("Admin command executed")
                return 1
            return 0