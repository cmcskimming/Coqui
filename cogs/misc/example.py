from discord.ext import commands
import discord

# pretty much just make a folder in the "cogs" folder to hold all the cogs for that category
# just copy this template and replace "example" with the name of your cog
# never put a naked file in the "cogs" folder always put it in a folder like how this one's in "misc"

class example(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("hi")

#Events
#    @commands.Cog.listener()

def setup(bot):
    bot.add_cog(example(bot))