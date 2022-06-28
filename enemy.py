from copy import deepcopy

class Enemy:

    def __init__(self, enemy):
        self.name_enemy = enemy['Name']
        self.HP_enemy = enemy['HP']
        self.Dmg_enemy = enemy['Dmg']
