import discord
import math
import string

from key import BOT_KEY

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Successfully connected.')
    await bot.change_presence(activity=discord.Game(name="a game"))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    words = message.content.split()

    if words[0] == '!factorial':

        if(len(words) != 2):
            print('Incorrect number of arguments')
            return
        
        solve = math.factorial(int(words[1]))
        content = words[1] + "! = " + str(solve)
        await message.channel.send(content)
        return

client.run(BOT_KEY)