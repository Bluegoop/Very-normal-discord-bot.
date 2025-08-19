import discord
from discord import app_commands
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

#this just sets up the intents of what the bot can and can't do
intents = discord.Intents.default()
intents.message_content = True

#this just loads the contents within the file.env
load_dotenv(dotenv_path = '#enter path here')
token = os.getenv('TOKEN')

#this creates the client
client = discord.Client(intents=intents)

#this allows us to make slash commands
tree = app_commands.CommandTree(client)

#here is where the bot becomes online!!!!
@client.event
async def on_ready():
    print(f'I AM HERE, YES {client.user}!')
    await tree.sync()

#meme spam lol
@tree.command(name='definetly_not_spam_tehehe',description='curiosity killed the cat')
async def definetly_not_spam_tehehe(interaction: discord.Interaction, number_of_memes: int):
    channel_id = #enter channel id here
    channel = client.get_channel(channel_id)

    if channel is not None:
        for i in range(number_of_memes):
            response = requests.get('https://meme-api.com/gimme')
            data = response.json()
            coolMeme_url = data["url"]
            await channel.send(coolMeme_url)
            print(f"Meme {i} has been sent.")
    else:
        print("Yeaaaaa we couldn't find your channel id lol. u suck")

#text spam lol
@tree.command(name='spam_text_coz_y_not',description='to find the userid, right-click on the user and copy the userid. Paste it in the userid placeholder.')
async def spam_text_coz_y_not(interaction: discord.Interaction, userid: str, message: str, number_of_times: int):
    channel_id = #enter channel id here
    channel = client.get_channel(channel_id)

    for i in range(number_of_times):
        await channel.send(f"<@{userid}> message")
        print(f"Message {i} has been sent.")


client.run(token)
