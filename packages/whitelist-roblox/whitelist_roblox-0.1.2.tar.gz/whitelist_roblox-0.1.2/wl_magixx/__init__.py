import requests

apikey = ''
api_url = 'https://1.kelprepl.repl.co/api/v1/'

def add_whitelist(discord_id: int):
    response = requests.post(api_url + f"premium_add?discord_id={discord_id}&api_key={apikey}")
    return response.json()

def del_whitelist(discord_id: int):
    response = requests.delete(api_url + f"premium_add?discord_id={discord_id}&api_key={apikey}")
    return response.json()

def reset_whitelist(discord_id: int):
    response = requests.patch(api_url + f"premium_reset?discord_id={discord_id}&api_key={apikey}")
    return response.json()

def whitelist(discord_id: int):
    response = requests.get(api_url + f"premium_add?discord_id={discord_id}&api_key={apikey}")
    return response.json()