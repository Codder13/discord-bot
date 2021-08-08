import discord
from random import randint
import requests
import os
from dotenv import load_dotenv


client = discord.Client()

load_dotenv()
my_secret = os.environ['TOKEN']
many_jokes = []


def get_joke():
    value = randint(0, 6)
    type_of_joke = ["Mist", "Programming", "Dark", "Pun", "Spooky", "Christmas"]

    url = "https://sv443.net/jokeapi/v2/joke/Misc/" + type_of_joke[value]

    querystring = {"format": "txt", "contains": "", "idRange": "0-150", "blacklistFlags": "racist"}

    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com'}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("chill hello" or "Chill hello"):
        await message.channel.send('Hello!')
        print('hello')

    if message.content.startswith("chilling" or "Chilling"):
        await message.channel.send("Glad you like the server!!")

    if message.content.startswith("chill joke" or "Chill joke" or "chill joke " or "Chill joke "):
        await message.channel.send(get_joke())


client.run(my_secret)

if __name__ == '__main__':
    print()
