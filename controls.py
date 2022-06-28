import sys
import entity
import random
import functions as func
import data_manager as dm

def EventChecking(event, player, caravan):
    if event == 'exit':
        if func.YesOrNoChecking(input('Are you sure you want to go out? (y/n) ').lower()):
            dm.SaveData(player)
            sys.exit()
        else:
            pass

    elif event == 'profile':
        player.PrintProfile()

    elif event == 'balance':
        player.PrintBalance()
    
    elif event == 'save':
        dm.SaveData(player)

    elif event == 'walk':
        player.Walking(player)

    elif event == 'inventory':
        player.PrintInventory()

    elif event == 'outfit':
        player.PrintOutfit()

    elif event == 'player':
        player.PrintPlayer()
    
    elif event == 'act':
        if len(player.Inventory['Inventory']) == 0:
            print('You have an empty inventory. Nothing to use :(\n')
        else:
            player.ActItem()
    
    else:
        func.SyntaxError()