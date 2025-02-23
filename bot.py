import discord, os
from rasa.core.agent import Agent
from rasa.utils.endpoints import EndpointConfig

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_TOKEN")

# Load Rasa model
agent = Agent.load("models/20250223-004426-natural-determinant.tar.gz", action_endpoint=EndpointConfig(url="http://localhost:5055/webhook"))

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = await agent.handle_text(message.content)

    await message.channel.send(response[0]['text'])

# Run the bot
client.run(DISCORD_BOT_TOKEN)
