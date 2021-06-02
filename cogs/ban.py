import discord
from discord.ext import commands

class Ban(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['b'])
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, *, member: discord.Member=None, reason='No reason provided'):
    if member == None:
      await ctx.send(f'{ctx.author.mention} Provide a member to ban.')
    elif member != None:
        await member.send(f'You have been banned in {ctx.guild.name} by {ctx.author.name}, Reason: {reason}')
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned from the server successfully, Reason: {reason}')

  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(client):
  client.add_cog(Ban(client))