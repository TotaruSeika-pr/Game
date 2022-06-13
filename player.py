import random
import controls
import functions as func
from caravan import Caravan

class Player(Caravan):
    
    def __init__(self, data):
        self.Name = data["Name"]
        self.HP = data["HP"]
        self.Def = data["Def"]
        self.Dmg = data["Dmg"]
        self.Level = data["Level"]
        self.Outfit = data["Outfit"]
        self.Inventory = data["Inventory"]
        self.Money = data["Money"]

    def PrintPlayer(self):
        Player.PrintProfile(self)
        Player.PrintBalance(self)
        Player.PrintInventory(self)

    
    def PrintProfile(self):
        print('-----===== P R O F I L E =====-----')
        print(f'  Name: {self.Name}')
        print(f'  HP: {self.HP["HP"]}/{self.HP["HPMax"]}')
        print(f'  Level: {self.Level["Level"]} | {self.Level["Exp"]}/{self.Level["ExpMax"]}')

    def PrintInventory(self):
        print('-----===== I N V E N T O R Y =====-----')
        index = 1
        for i in self.Inventory["Inventory"]:
            try:
                i['Def']
            except KeyError:
                if i['Type'] == 'weapon':
                    print(f"{index}) {i['Name']} | Damage: {i['Dmg']} | {i['Rarity']}")
                elif i['Type'] == 'potion':
                    print(f"{index}) {i['Name']} | {i['Benefit']*100}% {i['Assistance type']}")
                index += 1
            else:
                print(f"{index}) {i['Name']} | Def: {i['Def']} | {i['Rarity']}")
                index += 1

        print(f"Items: {len(self.Inventory['Inventory'])}/{self.Inventory['Capacity']}")
            

    def InventoryChecking(self):
        if len(self.Inventory["Inventory"]) < self.Inventory["Capacity"]:
            return True
        else:
            print('\nThere is no room in inventory!\n')
            return False
    
    def PrintBalance(self):
        print('-----===== B A L A N C E =====-----')
        print(f'  Coins: {self.Money["Coins"]}')
        print(f'  Diamonds: {self.Money["Diamonds"]}')

    def Walking(self, player):
        a = random.randint(0, 100)
        if a >= 0 and a <= 49:
            print('You walked around and found nothing.')
        elif a >= 50 and a <= 79:
            print('You met a monster!')
        elif a >= 80 and a <= 94:
            print('You met a caravan!')
            if func.YesOrNoChecking(input('Would you like to see the products of the caravan? (y/n) ')):
                Caravan.FindCaravan(self, player)
        elif a >= 95 and a <= 100:
            print('You found diamonds!')
            Player.FindDiamonds(player)

    def FindDiamonds(self):
        self.Money["Diamonds"] += 1
    
    def LevelUp(self):
        if self.Level['Exp'] >= self.Level['ExpMax']:
            self.Level['Level'] += 1
            self.Level['Exp'] -= self.Level['ExpMax']
            self.Level['ExpMax'] = (self.Level['ExpMax']*1.5)//1
            self.Inventory['Capacity'] += 1
            self.HP['HPMax'] += 10
            self.HP['HP'] = self.HP['HPMax']
            self.Dmg += 3
            self.Def += 2
