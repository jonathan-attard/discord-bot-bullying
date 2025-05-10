import discord
import random
from discord.ext import commands
from utils import DISCORD_TOKEN
from bully import bully

intents = discord.Intents.default()
intents.message_content = True  # Required to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Percentage chance to reply (e.g., 20%)
REPLY_CHANCE = 1.0

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    # Random chance to respond
    if random.random() < REPLY_CHANCE:
        text = message.content
        reply = bully_nikoali(text)
        await message.channel.send(reply)
        # await message.channel.send(f"Hi {message.author.name}, I heard you!")

    # Required so commands still work
    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
