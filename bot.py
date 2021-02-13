# bot.py
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents, command_prefix='~')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='send-messages')
@commands.has_permissions(mention_everyone=True) 
async def send_messages(ctx, role, message):
    members = await ctx.guild.fetch_members(limit=150).flatten()
    for member in members:
        if user_has_role(member, role):
            await member.send(message)
    await ctx.author.send("Messages sent!")

def user_has_role(user, role):
    role_names = list(map(lambda r: r.name, user.roles))
    return role in role_names

bot.run(TOKEN)
