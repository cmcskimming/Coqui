from discord.ext import commands
import discord

class eventLogging(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        channel_id = 1192707501959950336
        channel = self.bot.get_channel(channel_id)
        inviter = invite.inviter
        await channel.send(f"Invite {invite.code} created by {inviter.name}#{inviter.discriminator}")

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        channel_id = 1192707501959950336
        channel = self.bot.get_channel(channel_id)
        inviter = invite.inviter
        await channel.send(f"Invite {invite.code} deleted by {inviter.name}#{inviter.discriminator}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 1190452673531625605
        admin_channel_id = 1192707501959950336

        channel = self.bot.get_channel(channel_id)
        admin_channel = self.bot.get_channel(admin_channel_id)

        guild = member.guild
        banner_url = "https://i.imgur.com/dnYnfmo.png"
        custom_message = "Welcome to {guild.name}! We're excited to have you here. Feel free to reach out if you have any questions or just want to say hello. Don't forget to explore our other communities!"

        await channel.send(f"Welcome to {guild.name}! Dive into discussions, squad up, and enjoy the journey with us. Don't forget to explore our other communities {banner_url}")

        invites = await guild.invites()
        for invite in invites:
            if invite.uses != invite.max_uses:
                await admin_channel.send(f"Admin: {member.name}#{member.discriminator} joined using the invite: {invite.url}")
                break

        await member.send(custom_message)

    @commands.Cog.listener()
    async def log_action(self, guild, moderator, action, target, reason=None):
        log_channel_id = 1193092709896945664
        log_channel = guild.get_channel(log_channel_id)

        if log_channel:
            log_message = f"**{action}**\n" \
                            f"Moderator: {moderator.mention}\n" \
                            f"Target: {target.mention}\n" \
                            f"Reason: {reason or 'Not specified'}"

            await log_channel.send(log_message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel_id = 1193092709896945664
        log_channel = self.bot.get_channel(log_channel_id)

        if log_channel:
            log_message = f"**Member Left**\n" \
                        f"Member: {member.mention}\n"

            await log_channel.send(log_message)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # Replace 'message_id' with the ID of the message you sent in choose_roles
        if payload.message_id == 1193123808119365694:
            guild = self.bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)

            if payload.emoji.name == '🌍':
                role = discord.utils.get(guild.roles, name='PR.FN | Universal')
                await member.add_roles(role)
            elif payload.emoji.name == '🚀':
                role = discord.utils.get(guild.roles, name='PR.FN | Renegade Raiders')
                await member.add_roles(role)
            elif payload.emoji.name == '🦖':
                role = discord.utils.get(guild.roles, name='PR.FN | Preds')
                await member.add_roles(role)
            elif payload.emoji.name == '🛡️':
                role = discord.utils.get(guild.roles, name='CoC | Recruit')
                await member.add_roles(role)
            elif payload.emoji.name == '👾':
                role = discord.utils.get(guild.roles, name='PR.FN | Senpais')
                await member.add_roles(role)

def setup(bot):
    bot.add_cog(eventLogging(bot))