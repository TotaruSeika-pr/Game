from cgi import test
from player import Player
from caravan import Caravan
import data_manager as dm
import controls
import functions


def main():
    if functions.GameInitialization():
        print('\t\tWelcome!')
        dm.SelectFile()
        player = Player(dm.data)
        caravan = Caravan()
        player.Money["Coins"] += 100 # убрать
        print(f'\nHello, {player.Name}. Have a good hunting!')
        try:
            while True:
                controls.EventChecking(input('\n--> ').lower(), player, caravan)
        except KeyboardInterrupt:
            dm.SaveData(player)
    else:
        exit(1)

if __name__ == '__main__':
    main()
