import random
from copy import deepcopy
import time
import entity
import functions as func

class Caravan:

    def FindCaravan(self, player):
        
        Caravan.ItemGeneration(self)

        print(f'-----===== C A R A V A N =====-----\n')

        while True:
            Caravan.PrintAssortment(self)
            event = input('\nWhat do you want? ')
            try:
                int(event)
            except ValueError:
                if event == 'leave':
                    break
                elif event == 'sell':
                    Caravan.ItemSale(self, player)
                else:
                    print('Is it something in a foreign language?')
            else:
                try:
                    if int(event) < 6:
                        self.caravan_items[int(event)-1]
                    else:
                        self.caravan_potions[int(event)-6]
                except IndexError:
                    print('There is no product with this number!')
                else:
                    Caravan.BuyingItem(self, player, event)
                    

    def ItemGeneration(self):
        
        number_generated_items = {'Common': 0, 'Unusual': 0, 'Rare': 0}

        types = ['Weapons', 'Heads', 'Torsos', 'Legs']
        
        item_type = random.choice(types)
        rare_item_type = random.choice(types)

        number_generated_items['Common'] = random.randint(1, 4)
        number_generated_items['Unusual'] = random.randint(1, (5-number_generated_items['Common']))
        number_generated_items['Rare'] = random.randint(0, 5-(number_generated_items['Common']+number_generated_items['Unusual']))

        number_crafted_items = {'Common': 0, 'Unusual': 0, 'Rare': 0}
        
        self.caravan_items = []
        self.caravan_special_offer = []

        for i in ['Common', 'Unusual', 'Rare']:
            while True:
                item = deepcopy(random.choice(entity.WEARABLE_ITEMS[item_type]))
                if item['Rarity'] == i:
                    if number_crafted_items[i] < number_generated_items[i]:
                        self.caravan_items.append(item)
                        number_crafted_items[i] += 1
                    else:
                        break
        
        while True:
            rare_item = deepcopy(random.choice(entity.WEARABLE_ITEMS[rare_item_type]))
            if rare_item['Rarity'] == 'Unusual' or rare_item['Rarity'] == 'Rare':
                rare_item['Price'] += random.randint(-10, 30)
                rare_item['Price'] *= 2
                self.caravan_special_offer = rare_item
                break

        for i in range(len(self.caravan_items)-1):
            coefficient = random.randint(-25, 25)
            self.caravan_items[i]['Price'] += coefficient


        self.caravan_potions = [entity.potions['1'], entity.potions['2'], entity.potions['3']]
        for i in range(3):
            coefficient = random.randint(-25, 25)
            self.caravan_potions[i]["Price"] += coefficient

    def PrintAssortment(self):
        index = 1
        for i in self.caravan_items:
            try:
                i['Def']
            except KeyError:
                print(f'{index}) {i["Name"]} | Dmg: {i["Dmg"]} | {i["Rarity"]} | {i["Price"]} (c)')
            else:
                print(f'{index}) {i["Name"]} | Def: {i["Def"]} | {i["Rarity"]} | {i["Price"]} (c)')
            index += 1

        index = 6
        for i in self.caravan_potions:
            print(f"{index}) {i['Name']}: +{i['Benefit']*100}% {i['Assistance type']} | {i['Price']} (c)")
            index += 1

        if self.caravan_special_offer != None:
            i = self.caravan_special_offer
            print('\tSpecial offer!!!')
            try:
                self.caravan_special_offer['Def']
            except KeyError:
                print(f'0) {i["Name"]} | Dmg: {i["Dmg"]} | {i["Rarity"]} | {i["Price"]} (c)')
            else:
                print(f'0) {i["Name"]} | Def: {i["Def"]} | {i["Rarity"]} | {i["Price"]} (c)')

    def BuyingItem(self, player, event):
        if player.InventoryChecking():
                if int(event) < 6 and int(event) > 0:
                    if player.Money["Coins"] >= self.caravan_items[int(event)-1]["Price"]:
                        player.Money["Coins"] -= self.caravan_items[int(event)-1]["Price"]
                        player.Inventory["Inventory"].append(self.caravan_items[int(event)-1])
                        self.caravan_items.pop(int(event)-1)
                    else:
                        print('Insufficient funds!')
                elif int(event) > 5:
                    if player.Money["Coins"] >= self.caravan_potions[int(event)-6]["Price"]:
                        player.Money["Coins"] -= self.caravan_potions[int(event)-6]["Price"]
                        player.Inventory["Inventory"].append(self.caravan_potions[int(event)-6])
                        self.caravan_potions.pop(int(event)-6)
                    else:
                        print('Insufficient funds!')
                elif int(event) == 0:
                    if player.Money["Coins"] >= self.caravan_special_offer["Price"]:
                        player.Money["Coins"] -= self.caravan_special_offer["Price"]
                        player.Inventory["Inventory"].append(self.caravan_special_offer)
                        self.caravan_special_offer = None


    def ItemSale(self, player):
        player.PrintInventory()
        ans = input('\nWhat do you want to sell? ')
        if ans == 'back':
            func.End()
        else:
            try:
                ans = int(ans)-1
                player.Inventory["Inventory"][ans]
            except IndexError:
                print('Invalid number!')
            except ValueError:
                print('Invalid command!')
            else:
                item = player.Inventory['Inventory'][ans]
                price = player.Inventory['Inventory'][ans]['Price']//2
                player.Money['Coins'] += price
                player.Inventory['Inventory'].pop(ans)
                print(f'\nYou sold {item["Name"]} for {price} (c)\n')