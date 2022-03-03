# `mermaidjs-discord`

`mermaidjs-discord` is a discord bot that allows you to render Mermaid.js diagrams in your discord chats.

## Server Installation instructions

Click here to [invite](https://discord.com/api/oauth2/authorize?client_id=935684419837132910&permissions=274877910016&scope=bot) the bot to your server.

Type in `!mermaid-help` for help on how to use this bot.

<br/>

## Running this bot locally
### Installation
---
This installation asumes you have `python3` installed on your machine and know how to use `pip`.

Run the following in the project root directory to get all the dependencies
>```bash
>pip install poetry
>poetry install
>```

<br/>

### Bot Token
---
After we have that installed, we need to grab a bot token from Discord.

Go to [this url](https://discordapp.com/developers/applications/me) and create a new application.<br/>
Add a name for your local bot, something like: `your-username-test-bot`. 

After you've made an application, you should be redirected to a page with all of the app's details on it. 
Scroll to the bottom of this page and press "create a bot user". You will then have a "click to reveal" link that shows you your bot's **token**.

Run the following in your terminal:
>```bash
>export TOKEN=[the token you copied above]
>```

Make sure you make that bot private in that page. 

<br/>

### Adding your Bot
---
1. On the side tab go to `OAuth2>URL Generator`.

2. Under scopes, select bot.

3. Under permissions, select admin.

4. Use the generated URL to add it to your personal discord server to test out that your code is working correctly.