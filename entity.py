
LOCATIONS = {
            "1": {"Name": "Forest", "id": 0, "Complexity": ["Easily", 1]},
            "2": {"Name": "Desert", "id": 1, "Complexity": ["Medium", 2]},
            "3": {"Name": "FoVolcanorest", "id": 2, "Complexity": ["Difficult", 3]}
            }

ENEMIES = {
            "1": {"Name": "Stone", "HP": [10, 25], "Dmg": [0, 2], "Spawn": [0, 1, 2]},
            "2": {"Name": "Wolf", "HP": [8, 12], "Dmg": [1, 3], "Spawn": [0, 1]},
            "3": {"Name": "Rogue", "HP": [12, 18], "Dmg": [3, 5], "Spawn": [0, 1]},
            "4": {"Name": "Big stone worm", "HP": [20, 32], "Dmg": [2, 5], "Spawn": [0, 2]},
            "5r": {"Name": "Lava monster", "HP": [15, 25], "Dmg": [4, 8], "Spawn": [2]}
          }

WEARABLE_ITEMS = {
  
  'Weapons':
            [{"Type": "Weapon", "Name": "Stick", "Dmg": 2, "Rarity": "Common", "Price": 35},
             {"Type": "Weapon", "Name": "Rusty knife", "Dmg": 4, "Rarity": "Common", "Price": 40},
             {"Type": "Weapon", "Name": "Wooden spear", "Dmg": 5, "Rarity": "Common", "Price": 50},
             {"Type": "Weapon", "Name": "Dagger", "Dmg": 7, "Rarity": "Unusual", "Price": 65},
             {"Type": "Weapon", "Name": "Iron sword", "Dmg": 10, "Rarity": "Unusual", "Price": 70},
             {"Type": "Weapon", "Name": "Katana", "Dmg": 13, "Rarity": "Rare", "Price": 80},
             {"Type": "Weapon", "Name": "Battle Ax", "Dmg": 17, "Rarity": "Rare", "Price": 90}],
  'Heads':
            [{'Type': 'Head', 'Name': 'Russian scarf', 'Def': 1, 'Rarity': 'Common', 'Price': 15},
             {'Type': 'Head', 'Name': 'Asian hat', 'Def': 2, 'Rarity': 'Common', 'Price': 20},
             {'Type': 'Head', 'Name': 'Hat with ear flaps', 'Def': 3, 'Rarity': 'Common', 'Price': 30},
             {'Type': 'Head', 'Name': 'Metal cap', 'Def': 5, 'Rarity': 'Unusual', 'Price': 45},
             {'Type': 'Head', 'Name': 'Military helmet', 'Def': 7, 'Rarity': 'Unusual', 'Price': 60},
             {'Type': 'Head', 'Name': 'Cast iron helmet', 'Def': 10, 'Rarity': 'Rare', 'Price': 80},
             {'Type': 'Head', 'Name': 'Kevlar helmet', 'Def': 15, 'Rarity': 'Rare', 'Price': 115}],
  'Torsos':
            [{'Type': 'Torso', 'Name': 'Light Windbreaker', 'Def': 2, 'Rarity': 'Common', 'Price': 25},
             {'Type': 'Torso', 'Name': 'Coat', 'Def': 5, 'Rarity': 'Common', 'Price': 45},
             {'Type': 'Torso', 'Name': 'Leather Jacket', 'Def': 8, 'Rarity': 'Unusual', 'Price': 65},
             {'Type': 'Torso', 'Name': 'Body Armor', 'Def': 11, 'Rarity': 'Unusual', 'Price': 80},
             {'Type': 'Torso', 'Name': 'Iron Barrel', 'Def': 15, 'Rarity': 'Rare', 'Price': 100}],
  'Legs':
            [{'Type': 'Legs', 'Name': 'Galoshes', 'Def': 1, 'Rarity': 'Common', 'Price': 15},
             {'Type': 'Legs', 'Name': 'Sneakers', 'Def': 2, 'Rarity': 'Common', 'Price': 25},
             {'Type': 'Legs', 'Name': 'Leather boots', 'Def': 4, 'Rarity': 'Unusual', 'Price': 40},
             {'Type': 'Legs', 'Name': 'Metal boots', 'Def': 6, 'Rarity': 'Rare', 'Price': 60}]
}


potions = {
            "1" : {"Type": "potion", "Name": "Lesser Healing Potion", "Assistance type": "HP", "Benefit": 0.25, "Price": 40},
            "2": {"Type": "potion", "Name": "Medium Healing Potion", "Assistance type": "HP", "Benefit": 0.5, "Price": 65},
            "3": {"Type": "potion", "Name": "Major Healing Potion", "Assistance type": "HP", "Benefit": 1, "Price": 90}
          }