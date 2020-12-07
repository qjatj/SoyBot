# Import Discord.py to access Discord's API
import discord
# Import the os module
import os
# Import load_dotenv function from dotenv module
from dotenv import load_dotenv
# loads the .env file that resides on the same level as the script
load_dotenv()
# Grab the API token from the .env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
#intents.members = True


# Gets the client object from discord.py.
client = discord.Client(intents=intents)

# Event listener for when the bot has switched from offline to online
@client.event
async def on_ready():
    guild_count = 0

    # Print all servers bot is in
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    
    # Print number of servers bot is in
    print("SampleDiscordBot is in  " + str(guild_count) + " guilds.")

# Event listener for when a new message is sent to a channel
@client.event
async def on_message(message):
    if message.content == "!hello":
        await message.channel.send("hi  " + str(message.author.display_name))

    #if message.channel.name == "welcome" and message.is_system():
        #guild = message.channel.guild
        #role = guild.get_role(785377420563709994)
        #user = message.author
        #await bot.add_roles(user, role)
    print("tests")

@client.event 
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='member')
    await member.add_roles(role)
    print("new member assigned role")


client.run(DISCORD_TOKEN)


