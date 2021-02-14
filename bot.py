# bot.py
import os
import discord
from discord.ext import commands

TOKEN = os.environ['DISCORD_TOKEN']

def create_bot():
    intents = discord.Intents.default()
    intents.members = True
    return commands.Bot(command_prefix='~', intents=intents)

bot = create_bot()

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
    await ctx.send("Messages sent!")

def user_has_role(user, role):
    role_names = list(map(lambda r: r.name, user.roles))
    return role in role_names

@send_messages.error
async def send_messages_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**ERROR**: You don't have the MENTION_EVERYONE permission.")

bot.run(TOKEN)
