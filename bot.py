# bot.py
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents, command_prefix='~')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='send-messages')
async def sendmessages(ctx, role, message):
    
    result = []
    members = await ctx.guild.fetch_members(limit=150).flatten()
    for member in members:
        role_names = list(map(lambda r: r.name, member.roles))
        if role in role_names:
            result.append(member)
    for target in result:
        await target.send(message)
    await ctx.author.send("Messages sent!")

bot.run(TOKEN)
