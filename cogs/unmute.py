import discord
from discord.ext import commands

class Unmute(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['um'])
  @commands.has_permissions(kick_members=True)
  async def unmute(self, ctx, *, member: discord.Member=None):
    if member == None:
      await ctx.send(f'{ctx.author.mention} Provide a member to unmute')
      
    elif member != None:
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await ctx.send(f'Unmuted {member.mention} successfully!')
        await member.send(
            f'you have unmuted from {ctx.guild.name} by {ctx.author.name}')

  @unmute.error
  async def unmute_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(client):
  client.add_cog(Unmute(client))