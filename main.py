import os
import discord
from discord.ext import commands
import json

from sqlalchemy import create_engine
# not sure if I need to import psycopg2 but sqlalchemy uses it so I'm just gonna leave this here
import psycopg2  

config = json.load(open('config.json'))

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

print(cogFiles)

for cogFile in cogFiles:
    try:
        bot.load_extension(cogFile)
    except Exception as error:
        print(error)

bot.run(config['token'])