import discord
from discord.ext import commands

class Poll(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases = ['pl'])
  async def poll(self, ctx, *, msg):
    channel = ctx.channel
    try:
      op1, op2 = msg.split('or')
      txt = f'React with :white_check_mark: for {op1} and :negative_squared_cross_mark: for {op2}'
    except:
      await ctx.send('Correct syntax: [Choice1] or [Choice2]')
      return

    embed = discord.Embed(title = 'Poll', description = txt, colour = discord.Colour.red())
    message_ = await ctx.send(embed=embed)
    await message_.add_reaction(":white_check_mark:")
    await message_.add_reaction(":negative_squared_cross_mark:")
    await ctx.message.delete()

def setup(client):
  client.add_cog(Poll(client))