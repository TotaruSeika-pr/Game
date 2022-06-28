import random
from copy import deepcopy
from typing import Type
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
        self.Statistics = data["Statistics"]

    def PrintPlayer(self):
        Player.PrintProfile(self)
        Player.PrintBalance(self)
        Player.PrintInventory(self)
        Player.PrintOutfit(self)
    
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
                if i['Type'] == 'Weapon':
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

    def PrintOutfit(self):
        print('-----===== O U T F I T =====-----')
        dmg_outfit = 0
        def_outfit = 0
        if self.Outfit['Weapon'] != None:
            print(f"Weapon: {self.Outfit['Weapon']['Name']} | Dmg: {self.Outfit['Weapon']['Dmg']}")
            dmg_outfit += self.Outfit['Weapon']['Dmg']
        if self.Outfit['Head'] != None:
            print(f"Head: {self.Outfit['Head']['Name']} | Def: {self.Outfit['Head']['Def']}")
            def_outfit += self.Outfit['Head']['Def']
        if self.Outfit['Torso'] != None:
            print(f"Torso: {self.Outfit['Torso']['Name']} | Def: {self.Outfit['Torso']['Def']}")
            def_outfit += self.Outfit['Torso']['Def']
        if self.Outfit['Legs'] != None:
            print(f"Legs: {self.Outfit['Legs']['Name']} | Def: {self.Outfit['Legs']['Def']}")
            def_outfit += self.Outfit['Legs']['Def']
        print(f'Dmg: {self.Dmg+dmg_outfit}={self.Dmg}+{dmg_outfit} | Def: {self.Def+def_outfit}={self.Def}+{def_outfit}')
    
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
        elif a >= 95 and a <= 98:
            print('You have moved to a new location!')
        elif a >= 99 and a <= 100:
            print('You found diamonds!')
            Player.FindDiamonds(player)

    def FindDiamonds(self):
        self.Money["Diamonds"] += 1

    def PutItem(self, type, index):
        if self.Outfit[f'{type}'] == None:
                self.Outfit[f'{type}'] = deepcopy(self.Inventory['Inventory'][int(index)-1])
                self.Inventory['Inventory'].pop(int(index)-1)

        else:
            a = deepcopy(self.Outfit[f'{type}'])
            self.Outfit[f'{type}'] = self.Inventory['Inventory'][int(index)-1]
            self.Inventory['Inventory'][int(index)-1] = deepcopy(a)

    def RemoveItem(self, type):
        self.Inventory['Inventory'].append(deepcopy(self.Outfit[f'{type}']))
        self.Outfit[f'{type}'] = None

    def ActItem(self):
        Player.PrintInventory(self)
        event = input('What do you want to do?\n(put [num], throw [num], remove [type]) ')
        if event[:3] == 'put':
            index = event[4:]
            try:
                self.Inventory['Inventory'][int(index)-1]
            except TypeError:
                print('It must be a number!')
            except IndexError:
                print("You don't have that item in your inventory!")
            else:
                if self.Inventory['Inventory'][int(index)-1]['Type'] == 'potion':
                    if self.Inventory['Inventory'][int(index)-1]['Assistance type'] == 'HP':
                        self.HP['HP'] += round(self.Inventory['Inventory'][int(index)-1]['Benefit'] * self.HP['HPMax'])
                        if self.HP['HP'] > self.HP['HPMax']:
                            self.HP['HP'] = self.HP['HPMax']
                        self.Inventory['Inventory'].pop(int(index)-1)
                        print('You feel so much better!')

                elif self.Inventory['Inventory'][int(index)-1]['Type'] == 'Weapon':
                    Player.PutItem(self, 'Weapon', index)
                
                elif self.Inventory['Inventory'][int(index)-1]['Type'] == 'Head':
                    Player.PutItem(self, 'Head', index)
                
                elif self.Inventory['Inventory'][int(index)-1]['Type'] == 'Torso':
                    Player.PutItem(self, 'Torso', index)

                elif self.Inventory['Inventory'][int(index)-1]['Type'] == 'Legs':
                    Player.PutItem(self, 'Legs', index)
            
        elif event[:5] == 'throw':
            index = event[6:]
            try:
                self.Inventory['Inventory'][int(index)-1]
            except TypeError:
                print('It must be a number!')
            except IndexError:
                print("You don't have that item in your inventory!")
            else:
                if func.YesOrNoChecking(input(f"Are you sure you want to drop the {self.Inventory['Inventory'][int(index)-1]['Name']}? (y/n) ")):
                    self.Inventory['Inventory'].pop(int(index)-1)
                else:
                    pass

        elif event[:6] == 'remove':
            if Player.InventoryChecking(self):
                item_type = event[7:]
                Player.RemoveItem(self, item_type)

    
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
