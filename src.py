import requests
import json
import os

if os.path.isfile('key.txt'):
    with open('key.txt', 'r') as f:
        key = f.readline()

else:
    key = input('\nInput your Hypixel API key: ')

    

while True:
    IGN = input('\nEnter IGN here: ')

    mojangdata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{IGN}').json()
    link = f"https://api.hypixel.net/player?key={key}&uuid={mojangdata['id']}"
    apidata = requests.get(link).json()

    Wins = (apidata["player"]["stats"]["Bedwars"]["wins_bedwars"])
    Stars = (apidata["player"]["achievements"]["bedwars_level"])
    FinalDeaths = (apidata["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
    FinalKills = (apidata["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
    Kills = (apidata["player"]["stats"]["Bedwars"]["kills_bedwars"])
    Deaths = (apidata["player"]["stats"]["Bedwars"]["deaths_bedwars"])
    Coins = (apidata["player"]["stats"]["Bedwars"]["coins"])
    winstreak = (apidata["player"]["stats"]["Bedwars"]["winstreak"])
    FKDR = round(float(FinalKills) / float(FinalDeaths), 1)

    print(f'\nHypixel Bedwars Stats of: {mojangdata["name"]}')
    print(f'\nWins: {Wins:,}')
    print(f'\nStars: {Stars:,}')
    print(f'\nFinal Deaths: {FinalDeaths:,}')
    print(f'\nFinal Kills: {FinalKills:,}')
    print(f'\nFKDR: {FKDR:,}')
    print(f'\nKills: {Kills:,}')
    print(f'\nDeaths: {Deaths:,}')
    print(f'\nCoins: {Coins:,}')
    print(f'\nWinstreak: {winstreak:,}')

    with open('key.txt', 'w') as f:
        f.write(key)
