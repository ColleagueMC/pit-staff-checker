
import requests
import json
import time
import threading

API_KEY = "API KEY"

players = ["player1", "player2", "player3", "player4"]

def get_uuid(username):
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    return response.json()['id']

def check_player(uuid, username):
    while True:
        url = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
        response = requests.get(url)
        data = json.loads(response.text)
        initial_xp = data['player']['stats']['Pit']['profile']['xp']

        time.sleep(660)

        response = requests.get(url)
        data = json.loads(response.text)

        current_xp = data['player']['stats']['Pit']['profile']['xp']

        if current_xp != initial_xp:
            print(f"{username} is online!")


for player in players:
    uuid = get_uuid(player)
    threading.Thread(target=check_player, args=(uuid, player)).start()
