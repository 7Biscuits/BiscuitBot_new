import discord
from discord.ext import commands
import json
import random
import requests

class Inspire(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def inspire(self, ctx):
    def get_quote():
      response = requests.get("https://zenquotes.io/api/random")
      json_data = json.loads(response.text)
      quote = json_data[0] ['q'] + " ~" + json_data[0] ['a']
      return(quote)

    quote = get_quote()
    await ctx.send(quote)

def setup(client):
  client.add_cog(Inspire(client))