import json
import os
from sys import platform
import functions as func

def SelectFile():
    while True:
        file_name = input('Enter filename to upload: ')
        if file_name == '?':
            files = os.listdir('players')
            print('\n\tAvailable players:')
            for i in files:
                print(f'\t{i}')
            print('\n')
        elif file_name == '+':
            CreatePlayer()
        else:
            ans = LoadData(file_name)
            if ans:
                break

def LoadData(file_name):
    global data
    try:
        with open(f'players{func.separator}{file_name}.json', 'r', encoding='utf8') as f:
            data = json.load(f)
    except FileNotFoundError:
        if func.YesOrNoChecking(input('File with that name not found! Want to create a new file? (y/n) ').lower()):
            CreatePlayer()
            return False
        else:
            return False
        
    return True

def SaveData(player):
    data = {
        "Name": player.Name,
        "HP": player.HP,
        "Def": player.Def,
        "Dmg": player.Dmg,
        "Level": player.Level,
        "Outfit": player.Outfit,
        "Inventory": player.Inventory,
        "Position": player.Position,
        "Money": player.Money,
        "Statistics": player.Statistics
    }

    with open(f'players{func.separator}{player.Name}.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))

    print('Save completed successfully!')

def CreatePlayer():
    name = input('What is your name? ')
    with open(f'players{func.separator}{name}.json', 'w', encoding='utf8') as f:
        data = {
            "Name": name,
            "HP": {"HP": 25, "HPMax": 25},
            "Def": 0,
            "Dmg": 2,
            "Level": {"Exp": 0, "ExpMax": 10, "Level": 1},
            "Outfit": {"Weapon": None, "Head": None, "Torso": None, "Legs": None},
            "Inventory": {"Inventory": [], "Capacity":  5},
            "Position": {"Location_id": 0},
            "Money": {"Coins": 0, "Diamonds": 0},
            "Statistics": {"Steps": 0}
        }

        f.write(json.dumps(data, sort_keys=True, indent=4))
