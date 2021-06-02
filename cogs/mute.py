import discord
from discord.ext import commands

class Mute(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['m'])
  @commands.has_permissions(kick_members=True)
  async def mute(self, ctx, *, member: discord.Member=None, reason="No Reason Provided"):
    if member == None:
      await ctx.send(f'{ctx.auhtor.mention} Provide a member to mute')
    elif member != None:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        await ctx.send(f"Muted {member.mention} successfully!, Reason: {reason}")
        await member.send(f" You have been muted in: {ctx.guild.name} by {ctx.author.name} Reason: {reason}")

  @mute.error
  async def mute_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(client):
  client.add_cog(Mute(client))