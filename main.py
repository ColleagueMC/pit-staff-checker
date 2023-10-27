import requests
import time

def get_uuid(api_key, username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["id"]
    else:
        return None

def track_guild_xp(api_key, players):
    url = "https://api.hypixel.net/guild"
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    uuids = {}
    guild_xp = {}
    while True:
        for player in players:
            if player not in uuids:
                uuid = get_uuid(api_key, player)
                if uuid:
                    uuids[player] = uuid
                else:
                    print(f"Failed to get UUID for {player}")
                    continue
            params["player"] = uuids[player]
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                new_guild_xp = data["guild"]["exp"]
                if player in guild_xp and new_guild_xp != guild_xp[player]:
                    print(f"{player} xp changed")
                guild_xp[player] = new_guild_xp
            else:
                print(f"Failed to get guild data for {player}")

        time.sleep(120)  # Wait for 2 minutes

# Ask for API key and list of players
api_key = input("Enter your API key: ")
players = input("Enter a comma-separated list of players: ").split(",")

# Track guild XP changes
track_guild_xp(api_key, players)
