import discord
from discord.ext import commands

class op(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def op(self, ctx, *, member: discord.Member=None):
    if member == None:
      member = ctx.author
      await ctx.send(f"I don't lie but {ctx.author.mention} is awesome!")
      return
    await ctx.send(f"I don't lie but {member.mention} is awesome!")

def setup(client):
  client.add_cog(op(client))