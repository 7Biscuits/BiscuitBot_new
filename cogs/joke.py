import discord
from discord.ext import commands
import json
import random
import requests

class Joke(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def joke(self, ctx):
    '''
    def get_joke():
      response = requests.get("https://v2.jokeapi.dev/Any")
      json_data = json.loads(response.text)
      joke = json_data[0] ['j']
      return joke
      '''
    
    def get_joke():
      api_end_point = "https://official-joke-api.appspot.com/jokes/random"
      joke = requests.get(api_end_point)
      json_data = json.loads(joke.text)
      joke = json_data[0] ['j']
      return joke

    joke = get_joke()
    await ctx.send(joke)

def setup(client):
  client.add_cog(Joke(client))