from discord.ext import commands
import praw
import os
import logging
import stuff.reddit as redditapi

def setup(bot):
    bot.add_command(reddit)

@commands.command()
async def reddit(ctx, sub):
    await ctx.send("Getting a random post from r/"+sub)
    output = redditapi.subredditRand(sub)
    await ctx.send(output)