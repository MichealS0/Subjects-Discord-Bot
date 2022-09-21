import discord
import discord.client
from datetime import date, time, datetime

TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def getlesson(day4subject, time4subject):

    global lessonTime

    # Lesson Time
    lesson2 = "08:57"
    lesson3 = "10:10"
    lesson4 = "11:02"
    lesson5 = "12:10"
    lesson6 = "13:02"
    lesson7 = "13:50"

    # Lesson Time Thursday
    Thu2 = "8:54"
    Thu3 = "9:44"
    Thu4 = "10:53"
    Thu5 = "11:42"
    Thu6 = "12:30"

    global content
    content = []

    global subj
    subj = ""

    with open(day4subject + ".txt", "r") as theFile:
        for subjects in theFile:
            content.append(subjects)

    # Normal Days
    if lesson2 > str(time4subject):
        subj = content[0]
    
    elif lesson3 > str(time4subject):
        subj = content[1]
    
    elif lesson4 > str(time4subject):
        subj = content[2]
    
    elif lesson5 > str(time4subject):
        subj = content[3]
    
    elif lesson6 > str(time4subject):
        subj = content[4]
    
    elif lesson7 > str(time4subject):
        subj = content[5]
    
    elif lesson7 < str(time4subject):
        subj = content[6]
    
    # For Thursday
    if str(time4subject) < Thu2:
        subj = content[0]

    elif str(time4subject) < Thu3:
        subj = content[1]
    
    elif str(time4subject) < Thu4:
        subj = content[2]
    
    elif str(time4subject) < Thu5:
        subj = content[3]
    
    elif str(time4subject) < Thu6:
        subj = content[4]
    
    elif str(time4subject) > Thu6:
        subj = content[5]

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
            timenow = datenow.now()

            getlesson(day, timenow)

            await message.channel.send("You have: " + subj)
            return

client.run(TOKEN)