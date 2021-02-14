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

@bot.command(name='send-messages', brief='Sends a DM to all members with specified role', description='This command will send message <message> to all members with the role <role>. Remember to use double quotes around the message, eg. ~send-message Role1 "Hello World!". The command will return the number of messages sent. IMPORTANT: It can only be excuted by members with the MENTION_EVERYONE permission.')
@commands.has_permissions(mention_everyone=True) 
async def send_messages(ctx, role, message):
    total = 0
    members = await ctx.guild.fetch_members(limit=150).flatten()
    for member in members:
        if user_has_role(member, role):
            await member.send(message)
            total += 1
    await ctx.send('{0} message(s) sent!'.format(total))

def user_has_role(user, role):
    role_names = list(map(lambda r: r.name, user.roles))
    return role in role_names

@send_messages.error
async def send_messages_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('**ERROR**: You don\'t have the MENTION_EVERYONE permission.')

bot.run(TOKEN)
