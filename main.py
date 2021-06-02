import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
import asyncio
import random
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

client = commands.Bot(command_prefix='b!')
#ddb = DiscordButton(client)

@client.event
async def on_ready():
  print("Bot is online")
  await client.change_presence(activity=discord.Game(
	  name="Eating Biscuits :) | b!help"))

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("That command doesn't exist. Type ```b!help``` to see the commands present")

@client.command(pass_context=True)
@client.event
async def on_member_join(ctx, *, member):
    print(f'{member} has joined {ctx.guild.name}')
    await client.change_presence(activity=discord.Game(name="Eating Biscuits :) | b!help"))

@client.event
async def on_member_remove(ctx, member):
    print(f'{member} has left {ctx.guild.name}')

@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong:***pong!*** {round(client.latency * 1000)}ms')

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(60)
    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]

@client.command()
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(title=f"Sniped message #{channel.name}",
                           description=snipe_message_content[channel.id],
                           color=ctx.author.color)
        em.set_footer(text=f"Message sniped by {ctx.author.name}")
        await ctx.send(embed=em)
        del snipe_message_content[channel.id]
        del snipe_message_author[channel.id]

    except:
        await ctx.send(f"**There is nothing to snipe!**")

@client.event
async def on_message(message):
  if message.content.startswith('b!guess'):
    answer = random.randint(1, 10)
    await message.channel.send(f'{message.author.mention} Guess a number between 1 and 10')

    def is_correct(m):
        return m.author == message.author and m.content.isdigit()

    try:
       guess = await client.wait_for('message', check=is_correct, timeout=5.0)

    except asyncio.TimeoutError:
      await message.channel.send(f'{message.author.mention} You took too long too respond. The answer was {answer}')

    if int(guess.content) == answer:
      await message.channel.send(f'{message.author.mention} you guessed it right. the answer was {answer}')
    else:
      await message.channel.send(f'{message.author.mention} your answer is wrong. The correct answer is {answer}')
    
  await client.process_commands(message)

@client.command()
async def pressff(ctx, *, member: discord.Member=None, reason=None):
    if member != None:
      msg_ = await ctx.send(f"Everyone!! Let's pay our respects to {member.mention},Reason: {reason}, React on the message to pay your respect")
      #await msg_.add_reaction('<:F_:713427539313557594>')
      await msg_.add_reaction('<:red_cross:817435952943071302>')

      def check(reaction, user):
        #return msg.id == ctx.message.id and msg.reaction == "<:red_cross:817435952943071302>"
        return str(reaction.emoji) == '<:red_cross:817435952943071302>' and user != client.user

      reaction, user = await client.wait_for("reaction_add",check=check)
      await ctx.send(f'{user.mention} has paid their respect')
      return

    elif member == None:
      await ctx.send(f'{ctx.author.mention} Hey idiot, Mention the member you want to pay respect')

@client.command()
async def pressf(ctx, *, member: discord.Member=None, reason=None):
  if member != None:
    m = await ctx.send(
      f"Everyone!! Let's pay respect {member.mention}, Reason: {reason}, Click on the button to pay your respect",
      buttons = [
        Button(style=ButtonStyle.blue, label="F"),
      ],
    )
    res = await client.wait_for_button_click(m)
    await res.respond(
      type=InteractionType.ChannelMessageWithSource,
      content=f'{res.user.name} has paid their respect'
    )
  else:
    await ctx.send(f'{ctx.author.mention} Hey idiot, Mention the member you want to pay respect')

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Extension loaded")

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Extension unloaded")

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Extension reloaded")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
client.run(os.getenv('Token'))
