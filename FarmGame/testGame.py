from FarmGame import FarmStock
from FarmGame import Player
from FarmGame import Farm
from FarmGame import Planting
import time

def game():
    playerStatus()
    x = str(input("buy, sell, plant, harvest or exit      "))


    if x == "buy":
        y = str(input("What would you like to buy? Wheat (15 each) or Corn (20 each)    "))
        if y == "Wheat" or y == "wheat":
            amount = str(input("How many would you like to buy?   "))
            FarmStock.Wheat.buyWheatAmount(int(amount))
        elif y == "Corn" or y ==  "corn":
            amount = str(input("How many would you like to buy?   "))
            FarmStock.Corn.buyCornAmount(int(amount))

    if x == "sell":
        y = str(input("What would you like to sell? Wheat (10 each) or corn (20 each)   "))
        if y == "Wheat" or y == "wheat":
            amount = str(input("How many would you like to sell?   "))
            FarmStock.Wheat.sellWheatAmount(int(amount))
        elif y == "Corn" or y == "corn":
            amount = str(input("How many would you like to sell?   "))
            FarmStock.Corn.sellCornAmount(int(amount))

    if x == "plant":
        y = str(input("What would you like to plant"))
        if y == "Wheat" or 'wheat':
            amount = str(input("How many would you like to plant?"))
            FarmStock.Wheat.grownWheat(amount)
            Planting.planting.plantSeeds(amount, y)
        if y == "Corn" or 'corn':
            amount = str(input("How many would you like to plant?"))
            FarmStock.Corn.grownCorn(amount)
            Planting.planting.plantSeeds(amount, y)



    if x == "harvest":
        print("Planted seeds:    " + str(Planting.planting.plantList))
        y = str(input("Which one would you like to harvest"))
        if y =="Wheat" or y =="wheat":
            FarmStock.Wheat.harvestWheat()
        if y == "Corn" or y == "corn":
            FarmStock.Corn.harvestCorn()

    if x != "exit":
        game()
    else:
        exit()


def playerStatus():
    print("Player money:   " + str(Player.Player.money))
    print("CORN amount in bag:  " + str(Player.Player.corn))
    print("WHEAT amount in bag:  " + str(Player.Player.wheat))
    print("WHEAT planted:    "  + str(FarmStock.Wheat.planted))
    print("FARMSIZE:    " + str(Farm.Farm.farmSize))
    print("Planted seeds:   " + str(Planting.planting.plantList))

game()