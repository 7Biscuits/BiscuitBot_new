import discord
from discord.ext import commands

class Text(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def text(self, ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

  @text.error
  async def text_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.author.mention} You don't Have permission to use this command")

def setup(client):
  client.add_cog(Text(client))