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
  embed = discord.Embed(description="Help on using the Mermaid.js Discord Bot.", color=4372867)
  embed.set_author(name="Help")
  embed.add_field(name="Helpful Links", value="[GitHub](https://github.com/Yash-Singh1/mermaidjs-discord) | [Issue Tracker](https://github.com/Yash-Singh1/mermaidjs-discord/issues) | [Mermaid.js Documentation](https://mermaid-js.github.io/)", inline=False)
  embed.add_field(name="Commands", value="__!mermaid-help__: Displays the current message.\n__!mermaid-r__ or __!mermaid-render__: Renders the diagram with the code following the command. Allows Mermaid.js diagram syntax.\n__!mermaid-invite__: Gets the invite link of the bot.\n__!mermaid-support__: Gets a link to a support issue tracker for the bot.", inline=False)
  await ctx.send(embed=embed)

@client.event
async def on_guild_join(guild):
  if guild.system_channel:
    await helpCommand(guild.system_channel)

@client.command()
async def help(ctx):
  await helpCommand(ctx)

@client.command(aliases=['r'])
async def render(ctx, *, arg):
  await ctx.message.reply('https://mermaid.ink/img/' + base64.b64encode(arg.encode('ascii')).decode('ascii'))

@client.command()
async def invite(ctx):
  await ctx.send(embed=discord.Embed(description="The invite link is https://discord.com/api/oauth2/authorize?client_id=935684419837132910&permissions=274877910016&scope=bot", color=4372867))

@client.command()
async def support(ctx):
  await ctx.send(embed=discord.Embed(description="The link to the issue tracker is https://github.com/Yash-Singh1/mermaidjs-discord/issues", color=4372867))

client.run(os.environ['TOKEN'])
