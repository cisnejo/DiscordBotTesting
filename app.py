import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

os.environ

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} Welcome to  Discord!')
    await client.wait_until_ready()
    channel = client.get_channel(int(os.environ["channel_id"]))
    print(channel)
    await channel.send("Hello, I am sending this message programmatically")
client.run(os.environ["bot_token"])
