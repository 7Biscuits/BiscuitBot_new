import discord
from discord.ext import commands

class Av(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['av'])
  async def avatar(self, ctx, *,  avamember : discord.Member=None):
    if avamember != None:
      userAvatarUrl = avamember.avatar_url
      await ctx.send(userAvatarUrl)

    elif avamember == None:
      avamember = ctx.author
      userAvatarUrl = avamember.avatar_url
      await ctx.send(userAvatarUrl)

def setup(client):
  client.add_cog(Av(client))

