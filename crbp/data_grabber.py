import pandas as pd
from tqdm import tqdm
import requests

header = {"Accept": "application/json",
          "authorization": input("Clash Royale API Token: ")
          }
url = "https://api.clashroyale.com/v1/"

def translate_id(id):
    id -= 26000000
    id_change = 0

    if id < 1000000:
        if id >= 67:
            id_change -= 2
        if id >= 72:
            id_change -= 2
        if id >= 74:
            id_change -= 1
        if id >= 80:
            id_change -= 5
        if id >= 83:
            id_change -= 2
    elif id < 2000000:
        id -= 999926
        if id >= 86:
           id_change -= 1
    else:
        id -= 1999913

    return id + id_change

def encode_battle(battle):
    cards = battle["team"][0]["cards"]
    row = [0] * 19

    col = 0
    for card in cards:
        id = translate_id(int(card["id"]))
        row[col] = id
        col += 1

    col = 8
    cards = battle["opponent"][0]["cards"]
    for card in cards:
        id = translate_id(int(card["id"]))
        row[col] = id
        col += 1

    crown_difference = battle["team"][0]["crowns"] - battle["opponent"][0]["crowns"]
    row[16] = battle["team"][0]["startingTrophies"]
    row[17] = battle["opponent"][0]["startingTrophies"]
    row[18] = 1 if crown_difference > 0 else 0

    return row

data = []
clans = requests.get(url + "clans?minScore=" + input("Minimum clan score? "), headers=header).json()["items"]
count = int(input(str(len(clans)) + " clans found. Total number of clans to evaluate? "))
while count > len(clans):
    print("Desired amount of clans exceed number of clans found.")
    count = int(input(str(len(clans)) + " clans found. Total number of clans to evaluate? "))
min_trophies = int(input("Minimum trophies per player? "))

for c in tqdm(range(0, count), position=0):
    members = requests.get(url + "clans/%23" + clans[c]["tag"][1:] + "/members", headers=header).json()["items"]
    for player in tqdm(members, position=1, leave=False):
        if player["trophies"] >= min_trophies:
            battle_log = requests.get(url + "players/%23" + player["tag"][1:] + "/battlelog", headers=header).json()
            for battle in battle_log:
                if "Ladder" in battle["gameMode"]["name"]:
                    encoded_battle = encode_battle(battle)
                    data.append(encoded_battle)
        

cols = [
    "p1card1",
    "p1card2",
    "p1card3",
    "p1card4",
    "p1card5",
    "p1card6",
    "p1card7",
    "p1card8",
    "p2card1",
    "p2card2",
    "p2card3",
    "p2card4",
    "p2card5",
    "p2card6",
    "p2card7",
    "p2card8",
    "p1trophies",
    "p2trophies",
    "outcome"
]

pd.DataFrame(data, columns=cols).to_csv("../data/data_ord.csv")
