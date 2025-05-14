import discord
import random
from utils import DISCORD_TOKEN, PERSON_BOT_ID
from bully import bully, bully_wrapper

# Set up intents (message content intent is required to read message content)
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
client = discord.Client(intents=intents)

# Chance to reply when not mentioned
REPLY_CHANCE = 0.15
BOT_REPLY_CHANCE = 0.5

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.event
async def on_message(message: discord.Message):
    text = message.clean_content
    
    # Ignore messages from bots
    if message.author.bot:
        author_id = message.author.id
        if author_id == PERSON_BOT_ID and random.random() < BOT_REPLY_CHANCE:         
            reply = bully_wrapper(text,  author_id)
            await message.reply(reply)
        return

    text = message.clean_content

    # Always reply if mentioned
    if message.mentions and client.user in message.mentions:
        reply = bully(text)
        await message.reply(reply)

    # Otherwise, use random chance
    elif random.random() < REPLY_CHANCE:
        reply = bully(text)
        await message.reply(reply)

# Run the bot
client.run(DISCORD_TOKEN)
