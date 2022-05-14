import random
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
                    del self.caravan_weapons
                    break
                elif event == 'sell':
                    Caravan.ItemSale(self, player)
                else:
                    print('Is it something in a foreign language?')
            else:
                try:
                    if int(event) < 6:
                        self.caravan_weapons[int(event)-1]
                    else:
                        self.caravan_potions[int(event)-6]
                except IndexError:
                    print('There is no product with this number!')
                else:
                    Caravan.BuyingItem(self, player, event)
                    

    def ItemGeneration(self):

        number_generated_weapons = {'Common': 0, 'Unusual': 0, 'Rare': 0}

        number_generated_weapons['Common'] = random.randint(1, 4)
        number_generated_weapons['Unusual'] = random.randint(1, (5-number_generated_weapons['Common']))
        number_generated_weapons['Rare'] = random.randint(0, 5-(number_generated_weapons['Common']+number_generated_weapons['Unusual']))

        number_crafted_weapons = {'Common': 0, 'Unusual': 0, 'Rare': 0}
        
        self.caravan_weapons = []


        for i in ['Common', 'Unusual', 'Rare']:
            while True:
                weapon = random.choice(entity.WEAPONS)
                if weapon['Rarity'] == i:
                    if number_crafted_weapons[i] < number_generated_weapons[i]:
                        self.caravan_weapons.append(weapon)
                        number_crafted_weapons[i] += 1
                    else:
                        break

        for i in range(len(self.caravan_weapons)-1):
            coefficient = random.randint(-25, 25)
            self.caravan_weapons[i]['Price'] += coefficient


        self.caravan_potions = [entity.potions['1'], entity.potions['2'], entity.potions['3']]
        for i in range(3):
            coefficient = random.randint(-25, 25)
            self.caravan_potions[i]["Price"] += coefficient

    def PrintAssortment(self):
        index = 1
        for i in self.caravan_weapons:
            print(f'{index}) {i["Name"]} | Dmg: {i["Dmg"]} | {i["Rarity"]} | Price: {i["Price"]} (c)')
            index += 1

        index = 6
        for i in self.caravan_potions:
            print(f"{index}) {i['Name']}: +{i['Benefit']*100}% {i['Assistance type']} | {i['Price']} (c)")
            index += 1

    def BuyingItem(self, player, event):
        if player.InventoryChecking():
                if int(event) < 6:
                    if player.Money["Coins"] >= self.caravan_weapons[int(event)-1]["Price"]:
                        player.Money["Coins"] -= self.caravan_weapons[int(event)-1]["Price"]
                        player.Inventory["Inventory"].append(self.caravan_weapons[int(event)-1])
                        self.caravan_weapons.pop(int(event)-1)
                    else:
                        print('Insufficient funds!')
                elif int(event):
                    if player.Money["Coins"] >= self.caravan_potions[int(event)-6]["Price"]:
                        player.Money["Coins"] -= self.caravan_potions[int(event)-6]["Price"]
                        player.Inventory["Inventory"].append(self.caravan_potions[int(event)-6])
                        self.caravan_potions.pop(int(event)-6)
                    else:
                        print('Insufficient funds!')


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
