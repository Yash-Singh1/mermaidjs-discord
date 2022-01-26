import discord
from discord.ext import commands
import os
import base64

client = commands.Bot(command_prefix=commands.when_mentioned_or(("!mermaid-")))

client.remove_command('help')

@client.event
async def on_ready():
  print('Logged on as', client.user.name)

async def helpCommand(ctx):
  embed = discord.Embed(description="Help on using the Mermaid.js Discord Bot", color=4372867)
  embed.set_author(name="Help")
  embed.add_field(name="Helpful Links", value="[GitHub](https://github.com/Yash-Singh1/mermaidjs-discord) | [Issue Tracker](https://github.com/Yash-Singh1/mermaidjs-discord/issues)", inline=False)
  embed.add_field(name="Commands", value="__!mermaid-version__: Display the current version of the `mermaidjs-discord`\n__!mermaid-help__: Displays the current message\n__!mermaid-r__ or __!mermaid-render__: Renders the diagram with the code following the command", inline=False)
  await ctx.send(embed=embed)

@client.event
async def on_guild_join(guild):
  if guild.system_channel:
    await helpCommand(guild.system_channel)

@client.command()
async def version(ctx):
  await ctx.send('You currently have `mermaidjs-discord` version 0.0.1 installed')

@client.command()
async def help(ctx):
  await helpCommand(ctx)

@client.command(aliases=['r'])
async def render(ctx, *, arg):
  await ctx.message.reply('https://mermaid.ink/img/' + base64.b64encode(arg.encode('ascii')).decode('ascii'))

client.run(os.environ['TOKEN'])
