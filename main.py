import discord
from discord.ext import commands
import os
import base64
import keep_alive
from replit import db
import json

client = commands.Bot(command_prefix=commands.when_mentioned_or(("!mermaid-")))

client.remove_command('help')

@client.event
async def on_ready():
  print('Logged on as', client.user.name)

async def helpCommand(ctx):
  embed = discord.Embed(description="Help on using the Mermaid.js Discord Bot.", color=4372867)
  embed.set_author(name="Help")
  embed.add_field(name="Helpful Links", value="[GitHub](https://github.com/Yash-Singh1/mermaidjs-discord) | [Issue Tracker](https://github.com/Yash-Singh1/mermaidjs-discord/issues) | [Mermaid.js Documentation](https://mermaid-js.github.io/)", inline=False)
  embed.add_field(name="Commands", value="__!mermaid-help__: Displays the current message.\n\
__!mermaid-r__ or __!mermaid-render__: Renders the diagram with the code following the command. Allows Mermaid.js diagram syntax.\n\
__!mermaid-invite__: Gets the invite link of the bot.\n\
__!mermaid-support__: Gets a link to a support issue tracker for the bot.\n\
__!mermaid-setTheme__: Sets the theme to use for the diagrams rendered for the user.\n\
__!mermaid-getTheme__: Gets the currently set theme for the user.\n\
__!mermaid-setStatus__: Sets the current status of the bot. One of `dnd` or `do_not_disturb`, `online`, `idle`, `offline`, or `invisible`.", inline=False)
  embed.add_field(name="Example Diagram", value="""
```markdown
!mermaid-render
graph TD
  A[Christmas] -->|Get money| B(Go shopping)
  B --> C{Let me think}
  C -->|One| D[Laptop]
  C -->|Two| E[iPhone]
  C -->|Three| F[fa:fa-car Car]
```
""")
  embed.set_image(url="https://mermaid.ink/img/pako:eNpVkMtqw0AMRX9FaNVA_ANeFBI7zSbQQrLzeCE8SmZI54E8JgTb_95x00KileCcexEasQuascSLUDRwqpWHPJumMmL75KhvoSjepz0ncMHzfYLt2z5Ab0KM1l9WD3-7SFCNh0VjSMb66_xA1W_-0_MEdXOgmEJsn8npFibYNfbL5PpXYoRz6qM5U3mmoiOBiqTFNToWR1bns8cloDAZdqywzKsmuSpUfs7eEDUl3mmbgmDu-O55jTSkcLz7DsskA_9LtaX8AvdnzT9s-1qQ")
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
  if (ctx.message.author.mention + "#" + str(ctx.message.author.id)) in db.keys():
    await ctx.message.reply('https://mermaid.ink/img/' + base64.b64encode(json.dumps({ 'mermaid': {'theme': db[ctx.message.author.mention + "#" + str(ctx.message.author.id)]}, 'code': arg }).encode('ascii')).decode('ascii') + ("?bgColor=333" if db[ctx.message.author.mention + "#" + str(ctx.message.author.id)] == 'dark' else ""))
  else:
    await ctx.message.reply('https://mermaid.ink/img/' + base64.b64encode(arg.encode('ascii')).decode('ascii'))

@client.command()
async def invite(ctx):
  await ctx.send(embed=discord.Embed(description="The invite link is https://discord.com/api/oauth2/authorize?client_id=935684419837132910&permissions=274877910016&scope=bot", color=4372867))

@client.command()
async def support(ctx):
  await ctx.send(embed=discord.Embed(description="The link to the issue tracker is https://github.com/Yash-Singh1/mermaidjs-discord/issues", color=4372867))

@client.command()
async def setTheme(ctx, theme = ''):
  if not(theme):
    await ctx.message.reply("A theme must be specified for this command to work")
  else:
    db[ctx.message.author.mention + "#" + str(ctx.message.author.id)] = theme
    await ctx.message.reply("Theme successfully set to " + theme)

@client.command()
async def getTheme(ctx):
  if (ctx.message.author.mention + "#" + str(ctx.message.author.id)) in db.keys():
    await ctx.message.reply(db[ctx.message.author.mention + "#" + str(ctx.message.author.id)])
  else:
    await ctx.message.reply("default")

@client.command()
async def setStatus(ctx,arg='Online'):
  try:
    newStatus = discord.Status[arg]
  except:
    await ctx.message.reply("There was an error parsing the status")
  else:
    await client.change_presence(status=newStatus)

keep_alive.keep_alive()

client.run(os.environ['TOKEN'])
