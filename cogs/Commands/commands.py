from discord.ext import commands
import discord
import requests
from datetime import datetime, timedelta
import asyncio
import praw
import random

reddit = praw.Reddit(client_id='kkM8aG_HAYrMKPDwWvO_zw',
 client_secret='x8D7OJ44MsAQqUTpHoXjTHk2YtdgEA',
 user_agent='YOUR_USER_AGENT')

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name='poll', help='Create a poll')
    async def create_poll(ctx, question, *options):
        if len(options) < 2:
            await ctx.send("You need to provide at least 2 options for the poll.")
            return

        formatted_options = [f"{index + 1}. {option}" for index, option in enumerate(options)]
        poll_message = f"**{question}**\n\n" + "\n".join(formatted_options)

        poll_embed = discord.Embed(title="Poll", description=poll_message, color=0x3498db)
        poll_embed.set_footer(text=f"Poll created by {ctx.author.display_name}")

        poll_message = await ctx.send(embed=poll_embed)

        for emoji in ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣'][:len(options)]:
            await poll_message.add_reaction(emoji)

    @commands.command()
    async def quote(ctx):
        response = requests.get('https://api.quotable.io/random')
        data = response.json()
        await ctx.send(f'"{data["content"]}" - {data["author"]}')

    @commands.command(aliases='commands', help='Show a list of commands with examples')
    async def show_commands(self, ctx):
        help_message = (
        "List of commands:\n"
        "!poll 'question' 'option1' 'option2' ... - Create a poll\n"
        "!quote - Get a random quote\n"
        "!countdown <hours> <minutes> <seconds> 'event_name' - Set a countdown to an event\n"
        "   Example: !countdown 2 30 0 'New Year's Eve' - Set a countdown for 'New Year's Eve'\n"
        "!timer <seconds> 'event_name' - Set a timer for an event\n"
        "   Example: !timer 3600 'Work Time' - Set a timer for 'Work Time' for 1 hour\n"
        "!meme - Get a random meme from Reddit\n"
        )

    @commands.command(name='countdown', help='Set a countdown to an event')
    async def set_countdown(self, ctx, hours: int, minutes: int, seconds: int, *, event_name):
        countdown_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        end_time = datetime.utcnow() + countdown_time

        countdown_embed = discord.Embed(title=f"Countdown to {event_name}", color=0xFF0000)

        countdown_embed.set_image(url='https://i.imgur.com/gD0gAo6.png')

        countdown_message = await ctx.send(embed=countdown_embed)

        while datetime.utcnow() < end_time:
            remaining_time = end_time - datetime.utcnow()
            remaining_str = str(remaining_time).split(".")[0]

            countdown_embed.set_footer(text=f"Time remaining: {remaining_str}")
            await countdown_message.edit(embed=countdown_embed)

        await asyncio.sleep(1)

        await ctx.send(f"The event '{event_name}' has started!")



    @commands.command(name='meme', help='Get a random meme')
    async def get_meme(self, ctx):
        try:
            subreddit = reddit.subreddit("memes")
            memes = list(subreddit.hot())

            random_meme = random.choice(memes)

            embed = discord.Embed(title=random_meme.title, color=0xFF4500)
            embed.set_image(url=random_meme.url)

            await ctx.send(embed=embed)    
            
        except Exception as e:
            print(f"An error occurred while fetching a meme: {e}")
        await ctx.send("Sorry, I encountered an error while fetching a meme. Please try again later.")



def setup(bot):
    bot.add_cog(commands(bot))