from discord.ext import tasks, commands
from discord.utils import get
import discord
import os

class GamingTimeChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_gaming_time.start()
    
    def cog_unload(self):
        self.check_gaming_time.cancel()
    
    @tasks.loop(minutes=1)
    async def check_gaming_time(self):
        await self.bot.wait_until_ready()
        for guild in self.bot.guilds:
            with open(os.path.join(os.getcwd(), 'data/' + str(guild.id) + '_gaming_channel.txt'), 'r') as f:
                channel = self.bot.get_channel(int(f.read()))
            with open(os.path.join(os.getcwd(), 'data/' + str(guild.id) + '_gaming_role.txt'), 'r') as f:
                role = get(guild.roles, id=int(f.read()))
            if channel == None or role == None:
                return
            gaming = True
            for member in role.members:
                if member.status == discord.Status.online:
                    continue
                else:
                    gaming = False
                    pass
            if gaming:
                await channel.send(role.mention)
            pass