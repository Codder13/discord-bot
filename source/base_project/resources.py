from random import randint
import requests
from replit import db

many_jokes = []
def get_joke():
    value = randint(0, 6)
    type_of_joke = ["Mist", "Programming", "Dark", "Pun", "Spooky", "Christmas"]

    url = "https://sv443.net/jokeapi/v2/joke/Misc/" + type_of_joke[value]

    querystring = {"format": "txt", "contains": "", "idRange": "0-150", "blacklistFlags": "racist"}

    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com'}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

def submit_joke():

    url = "https://jokeapi-v2.p.rapidapi.com/submit"

    payload = "{\n    \"formatVersion\": 2,\n    \"category\": \"Miscellaneous\",\n    \"type\": \"single\",\n    \"joke\": \"A horse walks into a bar...\",\n    \"flags\": {\n        \"nsfw\": true,\n        \"religious\": false,\n        \"political\": true,\n        \"racist\": false,\n        \"sexist\": false\n    }\n}"
    headers = {
        'content-type': "application/text",
        'x-rapidapi-key': "d069813a30mshf25bb909801eab3p1e3666jsnb43e75aac043",
        'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com"
    }

    response = requests.request("PUT", url, data=payload, headers=headers)

    return response.text


def update_jokes(joke1):
    many_jokes.append(joke1)



def delete_jokes(index):
    del many_jokes[index]
