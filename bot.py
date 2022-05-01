from discord.ext import commands
from config import bot_token

bot = commands.Bot(command_prefix="w!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.check
async def bot_check(ctx):
    return ctx.author.id in [270141848000004097, 647041687541121044]  # [yan, wyvest]


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Syntax: w!edit <file> <key> <value> [message]")
    else:
        print(error)


bot.load_extension("jishaku")
bot.load_extension("cogs.github")

bot.run(bot_token)
