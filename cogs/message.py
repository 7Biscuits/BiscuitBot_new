import discord
from discord.ext import commands

class Message(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def message(self, ctx, member: discord.Member, *, message="None"):
      if message == None:
        await ctx.send(f'{ctx.author.mention} Hey Idiot Mention the person you want to send the message')

      elif message != None:
          await member.send(f'{ctx.author.name} sent a message for you. MESSAGE: {message}')
          await ctx.send('Message has been delivered!!')
          
def setup(client):
  client.add_cog(Message(client))