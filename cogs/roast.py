import discord
from discord.ext import commands
import random

class Roast(commands.Cog):
  def __init__(self, client):
    self.client = client

  roast_responses = ["You’re not pretty enough to have such an ugly personality.", "I would call you a pig, but that would be offensive for pigs.", "You deserve a high five, but in the face.", "Why don't you slip into something more comfortable, like a coma.", "Don't let your mind wander, Its too small to be let it out by itself.", "You’re the reason I prefer animals over people.", "Keep rolling your eyes. Maybe you’ll find your brain back there."]

  @commands.command()
  async def roast(self, ctx, *, member: discord.Member=None):

    roast_responses = ["You’re not pretty enough to have such an ugly personality.", "I would call you a pig, but that would be offensive for pigs.", "You deserve a high five, but in the face.", "Why don't you slip into something more comfortable, like a coma.", "Don't let your mind wander, Its too small to be let it out by itself.", "You’re the reason I prefer animals over people.", "Keep rolling your eyes. Maybe you’ll find your brain back there."]

    if member == None:
      await ctx.send("mention a member you want to roast -_- else I will roast you!")
    else:
      await ctx.send(random.choice(roast_responses))
      await ctx.send(f"**Roasted** {member.mention}")
      await ctx.send("https://tenor.com/view/qc-got-roast-quebec-get-gif-13626924")
def setup(client):
  client.add_cog(Roast(client))