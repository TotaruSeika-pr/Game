import random
import controls
import functions as func
from caravan import Caravan

class Player(Caravan):
    
    def __init__(self, data):
        self.Name = data["Name"]
        self.HP = data["HP"]
        self.Dmg = data["Dmg"]
        self.Level = data["Level"]
        self.Outfit = data["Outfit"]
        self.Inventory = data["Inventory"]
        self.Money = data["Money"]
    
    def PrintProfile(self):
        print('-----===== P R O F I L E =====-----')
        print(f'  Name: {self.Name}')
        print(f'  HP: {self.HP["HP"]}/{self.HP["HPMax"]}')
        print(f'  Level: {self.Level["Level"]} | {self.Level["Exp"]}/{self.Level["ExpMax"]}')

    def PrintStats(self):
        pass

    def PrintInventory(self):
        for i in self.Inventory["Inventory"]:
            print(i)

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