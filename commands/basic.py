from discord.ext import commands
import random

def setup(bot):
    bot.add_command(meowwoem)
    bot.add_command(mock)
    bot.add_command(spam)



@commands.command()
async def meowwoem(ctx):
    await ctx.send("https://media.discordapp.net/attachments/736362433634893924/746391689123594341/image0-5-2.gif")
    await ctx.send("https://media.discordapp.net/attachments/736362433634893924/746391689421258912/image0-3-1.gif")

@commands.command()
async def mock(ctx, *, text):
    output = ''.join(random.choice((str.upper, str.lower))(c) for c in text)
    await ctx.send(output)

@commands.command()
async def spam(ctx, amount, *, text):
    if not amount.isdigit():
        await ctx.send("Amount must be a number")
        return
    for x in range(int(amount)):
        await ctx.send(text)

