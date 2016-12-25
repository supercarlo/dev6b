from WoWgame import Blacksmith
from WoWgame import Player
from WoWgame import Missions

def game():
    playerStatus()
    x = str(input("buy, sell, start, collect or exit      "))
    if x == "buy":
        y = str(input("What would you like to buy? Gear (15 each) or Weapons (20 each)    "))
        if y == "Gear" or y == "gear":
            amount = str(input("How many would you like to buy?   "))
            Blacksmith.Gear.buyGearAmount(int(amount))
        elif y == "Weapons" or y ==  "weapons":
            amount = str(input("How many would you like to buy?   "))
            Blacksmith.Weapons.buyWeaponsAmount(int(amount))
    if x == "sell":
        y = str(input("What would you like to sell? Gear (10 each) or Weapons (15 each)   "))
        if y == "Gear" or y == "gear":
            amount = str(input("How many would you like to sell?   "))
            Blacksmith.Gear.sellGearAmount(int(amount))
        elif y == "Weapons" or y == "weapons":
            amount = str(input("How many would you like to sell?   "))
            Blacksmith.Weapons.sellWeaponsAmount(int(amount))
    if x == "start":
        amount = input("How many would you like to start?: ")
        Missions.Missions.startMission(amount)
    if x == "collect":
        Missions.Missions.collectMission(x)

    if x != "exit":
        game()
    else:
        exit()


def playerStatus():
    print("Player money:   " + str(Player.Player.money))
    print("Gear amount equipped:  " + str(Player.Player.gear))
    print("Weapons amount equipped:  " + str(Player.Player.weapons))
    print("Missions Available: " + str(Missions.Missions.missions))
    print("Itemlevel on your hero is now " + str(Player.Player.itemlevel))

game()