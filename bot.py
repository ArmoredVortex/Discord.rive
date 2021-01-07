import discord
import os
from dotenv import load_dotenv
from pathlib import Path
import rivescript

rs = rivescript.RiveScript()
rs.load_directory('./brain')
rs.sort_replies()

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

token = os.getenv('BOT_token')
client = discord.Client()

    # trigger = rs.last_match("localuser")
    # info = rs.trigger_info(trigger)
    # print(trigger)
    # print(info)
    # print("Bot>", reply)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    content = message.content.lower()
    if message.author == client.user:
        return
    if message.channel.id != 796275181555286026:
        return
    if message.author.id == 722814184395374644:
        await message.channel.send("Haha Noob! I don't wanna talk to you")
        return
    else:
        reply = rs.reply("localuser", content)
        await message.channel.send(reply)


client.run(token)
