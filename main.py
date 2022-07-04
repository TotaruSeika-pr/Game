from player import Player
from caravan import Caravan
import data_manager as dm
import controls
import functions
import entity

def main():
    if functions.GameInitialization():
        print(f'\t\tWelcome! {entity.VERSION}')
        dm.SelectFile()
        player = Player(dm.data)
        caravan = Caravan()
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
