import discord
from discord.ext import commands

class Bonk(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def bonk(self, ctx, *, member: discord.Member = None):
    if member == None:
      await ctx.send(f"{ctx.author.mention} Listen Idiot you have to Mention the member You want to bonk -_-")
    else:
      await ctx.send(f'{ctx.author.mention} **BONKED** {member.mention}')
      await ctx.send("https://tenor.com/view/bonk-meme-dog-doge-gif-14889944")

def setup(client):
  client.add_cog(Bonk(client))