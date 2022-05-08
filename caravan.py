import random
import entity


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
                    Caravan.Sale(self, player)
                else:
                    print('Is it something in a foreign language?')
            else:
                try:
                    if int(event) < 6:
                        self.caravan_weapons[int(event)-1]
                    else:
                        print(self.caravan_potions[int(event)-6])
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

        

        # rarity = ['Common', 'Unusual', 'Rare']

        for i in ['Common', 'Unusual', 'Rare']:
            while True:
                weapon = random.choice(entity.WEAPONS)
                if weapon['Rarity'] == i:
                    if number_crafted_weapons[i] < number_generated_weapons[i]:
                        self.caravan_weapons.append(weapon)
                        number_crafted_weapons[i] += 1
                    else:
                        break
        
        """while True:
            if rarity_index > 2:
                break
            else:
                weapon = entity.WEAPONS[random.randint(0, len(entity.WEAPONS)-1)]
                try:
                    int(weapon["Price"])
                except TypeError:
                    if weapon["Rarity"] == rarity[rarity_index]:
                        if number_crafted_weapons[rarity[rarity_index]] < number_generated_weapons[rarity[rarity_index]]:
                            self.caravan_weapons.append(weapon)
                            number_crafted_weapons[rarity[rarity_index]] += 1
                        else:
                            rarity_index += 1
                else:
                    weapon = None
        
        weapon = None"""

        print(self.caravan_weapons)

        caravan_weapons = list(self.caravan_weapons)
        print(f'{id(caravan_weapons)} | {id(self.caravan_weapons)}')

        for i in range(len(caravan_weapons)-1):
            weapon_price = random.randint(caravan_weapons[i]["Price"][0], caravan_weapons[i]["Price"][1])
            caravan_weapons[i]["Price"] = weapon_price
            #self.caravan_weapons[i]["Price"] = random.randint(self.caravan_weapons[i]["Price"][0], self.caravan_weapons[i]["Price"][1])

        self.caravan_potions = caravan_weapons
            
            

        self.caravan_potions = [entity.potions['1'], entity.potions['2'], entity.potions['3']]
        for i in range(3):
            self.caravan_potions[i]["Price"] = random.randint(self.caravan_potions[i]["Price"][0], self.caravan_potions[i]["Price"][1])

    def PrintAssortment(self):
        index = 1
        for i in self.caravan_weapons:
            print(f'{index}) {i["Name"]} | Dmg: {i["Dmg"]} | {i["Rarity"]} | Price: {i["Price"]} (c)')
            index += 1

        print(f'6) {self.caravan_potions[0]["Name"]}: +{self.caravan_potions[0]["Benefit"]*100}% | {self.caravan_potions[0]["Price"]} (c)')
        print(f'7) {self.caravan_potions[1]["Name"]}: +{self.caravan_potions[1]["Benefit"]*100}% | {self.caravan_potions[1]["Price"]} (c)')
        print(f'8) {self.caravan_potions[2]["Name"]}: +{self.caravan_potions[2]["Benefit"]*100}% | {self.caravan_potions[2]["Price"]} (c)')

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
                    if player.Money["Coins"] >= self.caravan_potions[int(event)-1]["Price"]:
                        player.Money["Coins"] -= self.caravan_potions[int(event)-1]["Price"]
                        player.Inventory["Inventory"].append(self.caravan_potions[int(event)-6])
                    else:
                        print('Insufficient funds!')


    def Sale(self, player):
        player.PrintInventory()
        ans = int(input('\nWhat do you want to sell? '))
        try:
            player.Inventory["Inventory"][ans-1]
        except IndexError:
            print('Invalid number!')
        else:
            # фикс
            price = random.randint(player.Inventory["Inventory"][ans-1]["Price"][0], player.Inventory["Inventory"][ans-1]["Price"][1])//2
            player.Money["Coins"] += price
            player.Inventory["Inventory"].pop(ans-1)
            print(f'\nYou sold {player.Inventory["Inventory"]["Name"]} for {price} (c)')
