from random import randint

import requests


def get_quote():
    value = randint(0, 6)
    type_of_joke = ["Mist", "Programming", "Dark", "Pun", "Spooky", "Christmas"]

    url = "https://sv443.net/jokeapi/v2/joke/Misc/" + type_of_joke[value]

    querystring = {"format": "txt", "contains": "", "idRange": "0-150", "blacklistFlags": "racist"}

    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com'}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

get_quote()