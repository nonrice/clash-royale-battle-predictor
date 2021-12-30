import pandas as pd
from tqdm import tqdm
import requests

header = {"Accept": "application/json",
          "authorization": input("Clash Royale API Token: ")
          }
url = "https://api.clashroyale.com/v1/"


# LOCATIONS (inclusive): 57000001-57000006 NON COUNTRIES, 57000007-57000260 COUNTRIES
# USA: 57000249

def encode_battle(battle, card_list):
    cards = battle["team"][0]["cards"]
    output = [0] * 213
    for card in cards:
        id = int(card["id"]) - 26000000
        output[id if id < 1000000 else (id - 999926 if id < 2000000 else id - 1999912)] += 1
        card_list[id if id < 1000000 else (id - 999926 if id < 2000000 else id - 1999912)] = card["name"]
    cards = battle["opponent"][0]["cards"]
    for card in cards:
        id = int(card["id"]) - 26000000
        output[(id if id < 1000000 else (id - 999926 if id < 2000000 else id - 1999912))+105] += 1
        card_list[(id if id < 1000000 else (id - 999926 if id < 2000000 else id - 1999912))+105] = card["name"]
    crown_difference = battle["team"][0]["crowns"] - battle["opponent"][0]["crowns"]
    output[212] = 1 if crown_difference > 0 else 0
    return output, card_list

data = []
card_list = [""] * 212
locations_list = ["57000056", "57000249", "57000216", "57000077", "57000122"]

for location in locations_list:
    print("Accessing data from location: " + location + " (" + requests.get(url + "locations/" + location, headers=header).json()["name"] + ")")
    top_players = requests.get(url + "locations/" + location + "/rankings/players", headers=header, params={"limit": 1000})
    for i in tqdm(range(0, 1000)):
        try:
            battle_log = requests.get(url + "players/%23" + (top_players.json()["items"][i]["tag"])[1:] + "/battlelog", headers=header)
            for j in range(0, 25):
                if "Ladder" in battle_log.json()[j]["gameMode"]["name"]:
                    encoded_battle, card_list = encode_battle(battle_log.json()[j], card_list)
                    data.append(encoded_battle)
        except:
            continue

pd.DataFrame(data).to_csv("../data/data.csv")

card_data = []
for card in range(len(card_list)):
    card_data.append([card, card_list[card]])

pd.DataFrame(card_data).to_csv("../data/cardlist.csv")