import discord
from discord.ext import commands

class Kick(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['k'])
  @commands.has_permissions(ban_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason='No reason provided'):
    await member.kick(reason=reason)
    await ctx.send(
        f'{member} has been kicked from the server successfully, Reason: ' +
        reason)
    await member.send(
        f'You have been kicked from {ctx.guild.name} by {ctx.author.name}, Reason: '
        + reason)

  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(client):
  client.add_cog(Kick(client))