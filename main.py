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

# Variables 
role_message = 821627229174890517
member_role = 821627945654681621
auto_deafen = False #default

# Event listener for when the bot has switched from offline to online
@client.event
async def on_ready():
    guild_count = 0

    # Print all servers bot is in
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    
    # Print number of servers bot is in
    print("SoyBot is in  " + str(guild_count) + " guilds.")

# Event listener for when a new message is sent to a channel
@client.event
async def on_message(message):
    # Basic bot message response
    if message.content == "!hello":
        await message.channel.send("hi  " + str(message.author.display_name))

    # Enable/Disable auto deafen feature
    if (message.content.startswith("!ad")):
        if (message.author.guild_permissions.administrator):
            global auto_deafen
            auto_deafen = not auto_deafen
            tmp = "AutoDeafen is"
            tmp += " enabled" if auto_deafen else " disabled"
            await message.channel.send(tmp)
    
    # Deafen/Undeafen players in lobby
    if (message.content.startswith("!d") & auto_deafen == True):
        try:
            member = message.author
            if (member.guild_permissions.administrator):
                users = message.mentions if message.mentions else message.author.voice.channel.members
                for user in users:
                    await user.edit(deafen=not (user.voice.deaf), mute=not (user.voice.mute))
        except Exception as e:
                await message.channel.send(e)

#Assigns default role to new users
@client.event 
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='member')
    await member.add_roles(role)
    print("new member assigned role")

# Ping me function for active users
@client.event
async def on_raw_reaction_add(payload):
    try:
        if (payload.message_id == role_message):
            if (payload.emoji.name == "❌"):
                await payload.member.remove_roles(payload.member.guild.get_role(member_role))
            if (payload.emoji.name == "✅"):
                await payload.member.add_roles(payload.member.guild.get_role(member_role))
    except Exception as e:
        await message.channel.send(e)


client.run(DISCORD_TOKEN)


