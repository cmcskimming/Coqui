import discord
import json

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'logged in as {self.user}.')

client = MyClient()
client.run(json.load(open('token.json'))['token'])