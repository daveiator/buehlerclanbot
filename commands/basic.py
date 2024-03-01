from discord.ext import commands
import random

def setup(bot):
    bot.add_command(meowwoem)
    bot.add_command(mock)
    bot.add_command(spam)



@commands.command()
async def meowwoem(ctx):
    await ctx.send("https://tenor.com/view/cat-gif-25399804")

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

