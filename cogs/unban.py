import discord
from discord.ext import commands

class Unban(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['ub'])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member=None):
    if member == None:
      await ctx.send(f'{ctx.author.mention} Provide a member to unban')
    elif member != None:
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          await ctx.send(f"{user.name}#{user.discriminator} has been unbanned by {ctx.author.name}")
          return
          
        else:
          await ctx.send(f'{ctx.author.mention} Member not found')

  @unban.error
  async def unban_error(self, ctx , error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")
          
def setup(client):
  client.add_cog(Unban(client))

