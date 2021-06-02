import discord
from discord.ext import commands

class WhoIs(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def id(self, ctx, member : discord.Member=None):
    if member == None:
      member = ctx.author
    
    embed = discord.Embed(title = member.name, discription =member.mention, colour = discord.Colour.orange())
    embed.add_field(name = 'ID' , value = member.id , inline = True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url , text = f'requested by {ctx.author.name}')
    await ctx.send(embed = embed)

def setup(client):
  client.add_cog(WhoIs(client))
