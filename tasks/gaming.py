from discord.ext import tasks, commands
from discord.utils import get
import discord
import os
import random

no = [
    'Nah',
    'Fuck u',
    'No',
    "I'm sorry, but I cannot fulfill this request as it goes against OpenAI use policy",
    'Nope',
    'Huh?',
]
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
            self.bot.gaming[guild.id] = True
            for member in role.members:
                if member.status == discord.Status.online:
                    continue
                else:
                    self.bot.gaming[guild.id] = False
                    self.bot.shut_up[guild.id] = False
                    continue
            if self.bot.shut_up.get(guild.id, False):
                continue
            if self.bot.gaming.get(guild.id, False):
                await channel.send(role.mention)
                await channel.send("https://tenor.com/view/peaches-the-dog-damian-walter-hitting-gif-16355532")

async def shut_up(bot, message):
    if not 'shut' in message.content.lower():
        return
    for guild in bot.guilds:
        if bot.shut_up.get(guild.id, False) or not bot.gaming.get(guild.id, False):
            continue
        try:
            with open(os.path.join(os.getcwd(), 'data/' + str(guild.id) + '_gaming_channel.txt'), 'r') as f:
                channel = bot.get_channel(int(f.read()))
        except:
            return
        with open(os.path.join(os.getcwd(), 'data/' + str(guild.id) + '_gaming_role.txt'), 'r') as f:
            role = get(guild.roles, id=int(f.read()))
        if channel == None or role == None:
            return
        if message.channel == channel:
            if random.random() < 0.25:
                print("Shutup success!")
                bot.shut_up[guild.id] = True
                await channel.send("ok")
                return
            print("Better luck next time!")
            await channel.send(random.choice(no))

