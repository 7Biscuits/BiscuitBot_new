import discord
from discord.ext import commands

class Purge(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['pr'])
  @commands.has_permissions(administrator=True)
  async def purge(self, ctx, amount:int=None):
    if amount == None:
      await ctx.send(f"{ctx.author.mention} You didn't provide the number of messages to be purged.")

    else:
      await ctx.channel.purge(limit=amount)
      await ctx.send(f'{amount} messages have been purged by {ctx.author.mention}')

  @purge.error
  async def purge_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(client):
  client.add_cog(Purge(client))