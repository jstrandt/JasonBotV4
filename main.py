import discord
import os
import requests
import json
import neuralintents
from keep_alive import keep_alive
from neuralintents import GenericAssistant

assistant = GenericAssistant('intents.json')
assistant.train_model()
assistant.save_model()



print("Bot Running...")

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$aibot"):
    response = chatbot.request(message.content[7:])
    await message.channel.send(response)


keep_alive()

token = os.environ.get("DISCORD_BOT_SECRET")

client.run(token)