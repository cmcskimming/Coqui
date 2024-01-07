from discord.ext import commands
import discord

mod_role_ids = [1190452673074438277, 1190452673074438275]

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hi")

@commands.command(name='kick', help='Kick a user from the server')
async def kick(ctx, member: discord.Member, *, reason=None):
    # Check if the command author has either of the two moderator roles
    if any(role.id in mod_role_ids for role in ctx.author.roles):
        try:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked.')
            await log_action(ctx.guild, ctx.author, 'Kick', member, reason)
        except commands.MissingPermissions:
            await ctx.send("The target user has equal or higher permissions than the bot.")
    else:
        await ctx.send("You don't have the necessary role to use this command.")

@commands.command(name='ban', help='Ban a user from the server')
async def ban(ctx, member: discord.Member, *, reason=None):
    # Check if the command author has either of the two moderator roles
    if any(role.id in mod_role_ids for role in ctx.author.roles):
        try:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned.')
            await log_action(ctx.guild, ctx.author, 'Ban', member, reason)
        except commands.MissingPermissions:
            await ctx.send("The target user has equal or higher permissions than the bot.")
    else:
        await ctx.send("You don't have the necessary role to use this command.")

@commands.command(name='warn', help='Warn a user')
async def warn(ctx, member: discord.Member, *, reason=None):
    # Check if the command author has either of the two moderator roles
    if any(role.id in mod_role_ids for role in ctx.author.roles):
        await ctx.send(f'{member.mention} has been warned. Reason: {reason}')
        await log_action(ctx.guild, ctx.author, 'Warn', member, reason)
    else:
        await ctx.send("You don't have the necessary role to use this command.")

@commands.command(name='mute', help='Mute a user')
async def mute(ctx, member: discord.Member):
    # Check if the command author has either of the two moderator roles
    if any(role.id in mod_role_ids for role in ctx.author.roles):
        # Add logic to mute the user
        # Example: assign a Muted role to the user
        # Replace 'Muted' with your actual Muted role name
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(muted_role)
        await ctx.send(f'{member.mention} has been muted.')
        await log_action(ctx.guild, ctx.author, 'Mute', member)
    else:
        await ctx.send("You don't have the necessary role to use this command.")

@commands.command(name='unmute', help='Unmute a user')
async def unmute(ctx, member: discord.Member):
    # Check if the command author has either of the two moderator roles
    if any(role.id in mod_role_ids for role in ctx.author.roles):
        # Add logic to unmute the user
        # Example: remove the Muted role from the user
        # Replace 'Muted' with your actual Muted role name
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(muted_role)
        await ctx.send(f'{member.mention} has been unmuted.')
        await log_action(ctx.guild, ctx.author, 'Unmute', member)
    else:
        await ctx.send("You don't have the necessary role to use this command.")

@commands.command(name='unban', help='Unban a user')
async def unban(ctx, user_id: int):
    # Check if the command author has either of the two moderator roles
    if any(role.id in mod_role_ids for role in ctx.author.roles):
        # Add logic to unban the user
        # Example: unban the user using user_id
        await ctx.guild.unban(discord.Object(id=user_id))
        await ctx.send(f'User with ID {user_id} has been unbanned.')
        await log_action(ctx.guild, ctx.author, 'Unban', user_id)
    else:
        await ctx.send("You don't have the necessary role to use this command.")

@commands.command(name='modhelp', help='Remind mods of available moderation commands')
async def mod_help(ctx):
    # Check if the command author has either of the two moderator roles
    if any(role.id in mod_role_ids for role in ctx.author.roles):
        help_message = (
            "Moderation Commands:\n"
            "!kick <mention_user> [reason] - Kick a user from the server\n"
            "!ban <mention_user> [reason] - Ban a user from the server\n"
            "!unban <user_id> - Unban a user from the server\n"
            "!mute <mention_user> - Mute a user\n"
            "!unmute <mention_user> - Unmute a user\n"
            "!warn <mention_user> [reason] - Warn a user\n"
        )
        await ctx.send(help_message)
    else:
        await ctx.send("You don't have the necessary role to use this command.")









def setup(bot):
    bot.add_cog(moderation(bot))