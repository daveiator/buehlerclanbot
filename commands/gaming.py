from discord.ext import commands
import os

def setup(bot):
    bot.add_command(gaming)

    bot.shut_up = {}
    bot.gaming = {}


@commands.command()
async def gaming(ctx, arg1=None, arg2=None):
    match arg1:
        case "channel":
            # Get channel of message
            channel = ctx.message.channel
            with open(os.path.join(os.getcwd(), 'data/' + str(ctx.guild.id) + '_gaming_channel.txt'), 'w+', newline='') as f:
                f.write(str(channel.id))
            await ctx.send("Gaming channel set to " + channel.mention)
        case "role":
            # Get role of message
            role = ctx.message.role_mentions[0]
            with open(os.path.join(os.getcwd(), 'data/' + str(ctx.guild.id) + '_gaming_role.txt'), 'w+', newline='') as f:
                f.write(str(role.id))
            await ctx.send("Gaming role set to " + role.mention)
        case "gaming":
            await ctx.send("gaming")
        case _:
            await ctx.send("Invalid argument")