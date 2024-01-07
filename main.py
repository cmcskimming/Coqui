import os
import discord
from discord.ext import commands
import json

from sqlalchemy import create_engine
import psycopg2  

engine = create_engine("postgresql+psycopg2://@localhost/edward", echo=True)

prefix = commands.when_mentioned_or('!')
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix = '.', intents=intents
)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')


# so that we don't have to manually type all the cogs out to add them
cogFiles = []  

for folder in os.listdir("./cogs/"):
    for filename in os.listdir(f"./cogs/{folder}/"):
        if filename.endswith('.py'):
            cogFiles.append(f"cogs.{folder}.{filename[:-3]}")

for cogFile in cogFiles:
    try:
        bot.load_extension(cogFile)
    except Exception as error:
        print(error)

bot.run(json.load(open('config.json'))['token'])