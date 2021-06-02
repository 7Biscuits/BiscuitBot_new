import discord
from discord.ext import commands
from replit import db

class tagCommands(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def tag(self, ctx,tag=None):
    if tag == None:
      await ctx.send(f'{ctx.author.mention} dumbo atleast mention a tag -_-')

    elif tag is not None:
      value = db[tag]
      await ctx.send(value)

  @commands.command()
  async def createtag(self, ctx, tag=None,*,value):
    if tag == None:
      await ctx.send(f'{ctx.author.mention} Hey idiot write a tag to create -_-')

    elif tag is not None:
      db[tag] = value
      await ctx.send (f'tag has been succesfully made with name {tag}')

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def deletetag(self, ctx, tag=None):
    if tag == None:
      await ctx.send(f'{ctx.author.mention} write the tag name to be deleted')

    elif tag is not None:
      del db[tag]
      await ctx.send(f'tag {tag} has been deleted succesfully!')

  @deletetag.error
  async def deletetag_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(client):
  client.add_cog(tagCommands(client))
