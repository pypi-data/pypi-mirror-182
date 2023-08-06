import requests

apikey = ''
api_url = 'https://1.kelprepl.repl.co/api/v1/'

def add_whitelist(discord_id: int):
    response = requests.post(api_url + f"premium_add?discord_id={discord_id}&apikey={apikey}")
    return response.json()

def del_whitelist(discord_id: int):
    response = requests.post(api_url + f"premium_add?discord_id={discord_id}&apikey={apikey}")
    return response.json()

def whitelist(discord_id: int):
    response = requests.post(api_url + f"premium_add?discord_id={discord_id}&apikey={apikey}")
    return response.json()