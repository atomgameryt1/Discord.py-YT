import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='t!')
token = Put your Token Here


@bot.event
async def on_ready():
    print(f'Logged In to {bot.user}')

@bot.event
async def on_member_join(member):
    print('{member} has joined the server')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong!')

@bot.command()
async def youtube(ctx):
    await ctx.send('Go sucscribe to <https://www.youtube.com/channel/UCFz8iZht3zbqC58KLYOVVvg?view_as=subscriber>')

@bot.event
async def on_guild_join(guild):
    print(f'Bot has joined {guild.name}')

bot.run(token)

