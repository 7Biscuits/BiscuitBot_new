import discord
from discord.ext import commands
import random

class magicBall(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases = ['8ball'])
  async def _8ball(self, ctx, *, question):
    responses = [
        'It is certain.', 'Without a doubt.', 'You may rely on it.',
        'Yes definitely.', 'It is decidedly so.', 'As I see it, yes.',
        'Most likely.', 'Yes.', 'Outlook good.',
        'Signs point to yes Neutral Answers.', 'nope.', 'no.', 'never.',
        'maybe.', 'probably.', 'probably not.', 'could be.'
    ]
    await ctx.send(f'question: {question}\nAnswer: {random.choice(responses)}')
  
def setup(client):
  client.add_cog(magicBall(client))
