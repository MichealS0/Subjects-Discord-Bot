import discord
import discord.client
from datetime import date, time, datetime

TOKEN = 'MTAyMDIxMjQ3MTg5NTY5OTQ3Ng.G7JLuA.YhmCgNjPVA6f_ERNHAvObt7yEtA7JQ6pIvpAgU'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def getlesson(day4subject, time4subject):

    global content
    content = []

    with open(day4subject + ".txt", "r") as theFile:
        for subjects in theFile:
            content.append(subjects)

@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))

@client.event
async def on_message(message):

    if message.author != client.user:
        if message.content.startswith("hello"):
            await message.channel.send(f'Hello, {message.author.display_name}!')
            return

        elif message.content.startswith("/subject"):

            datenow = datetime.now()
            day = datenow.strftime('%A')
            timenow = datenow.strftime("%H:%w")

            getlesson(day, timenow)

            await message.channel.send(content)
            return

client.run(TOKEN)