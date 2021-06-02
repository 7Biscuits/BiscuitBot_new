import discord
from discord.ext import commands

class F(commands.Cog):
  def __init__(self, client):
    self.client = client 
  '''
  @commands.Cog.listener()
  async def on_message(self, message):
    while message.content == "f":
      await message.channel.send('f')
      break
      '''

def setup(client):
  client.add_cog(F(client))