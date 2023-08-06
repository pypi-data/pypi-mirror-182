import requests
from . import discordbot

apikey = ""
api_url = "https://1.kelprepl.repl.co/api/v1/"
name = ""
admins = []

def add_whitelist(discord_id: int):
    response = requests.post(api_url + f"premium_add?discord_id={discord_id}&api_key={apikey}")
    return response.json()

def del_whitelist(discord_id: int):
    response = requests.delete(api_url + f"premium?discord_id={discord_id}&api_key={apikey}")
    return response.json()

def reset_whitelist(discord_id: int):
    response = requests.patch(api_url + f"premium_reset?discord_id={discord_id}&api_key={apikey}")
    return response.json()

def whitelist(discord_id: int):
    response = requests.get(api_url + f"premium?discord_id={discord_id}&api_key={apikey}")
    return response.json()

def get_whitelist_list():
    response = requests.get(api_url + f"premium_list?api_key={apikey}")
    return response.json()
