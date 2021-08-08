import discord
from random import randint
import requests
from discord.ext import commands
from keep_alive import keep_alive


client = discord.Client()

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

    if message.content.startswith("chilling" or "Chilling"):
        await message.channel.send("Glad you like the server!!")

    if message.content.startswith("chill joke" or "Chill joke" or "chill joke " or "Chill joke "):
        await message.channel.send(get_joke())

    if message.content.startswith("chill new joke"):
        new_joke = message.content.split("chill new joke ", 1)[1]
        many_jokes.append(new_joke)
        await message.channel.send("New joke added")

    if message.content.startswith("chill jokes list"):
        await message.channel.send(many_jokes)


@commands.command(
    name="echo"
)
async def echo(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="Please tell me what to repeat: "
    )
    sent = await ctx.send(embed=embed)

    try:
        msg = await self.bot.wait_for(
            "message",
            timeout=60,
            check=lambda message: message.author == ctx.author
                                  and message.channel == ctx.channel
        )
        if msg:
            await sent.delete()
            await msg.delete()
            await ctx.send(msg.content)

    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send("Cancelling due to timeout", delete_after=10)

keep_alive()

client.run('ODcyMDk3ODIzODk2NzcyNjI5.YQk6ZA.e-SfMzUoo1sjfO-jM12GjZ5MZWo')

if __name__ == '__main__':
    print()
