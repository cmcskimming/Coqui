import os
import discord
from discord.ext import commands
import json

from sqlalchemy import create_engine
# not sure if I need to import psycopg2 but sqlalchemy uses it so I'm just gonna leave this here
import psycopg2  

config = json.load(open('config.json'))

prefix = commands.when_mentioned_or('!')
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix = '.', intents=intents
)

# adding database engine to bot object for reference within cogs
engine = create_engine(f"postgresql+psycopg2://{config['db_user']}:{config['db_key']}@localhost/{config['db_name']}", echo=True)
bot.DB = engine

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

bot.run(config['token'])