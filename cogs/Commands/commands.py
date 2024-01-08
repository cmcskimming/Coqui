from discord.ext import commands
import discord
import requests

class moderation(commands.Cog):
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






def setup(bot):
    bot.add_cog(commands(bot))