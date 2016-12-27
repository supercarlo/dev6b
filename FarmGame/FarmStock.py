from FarmGame import Farm
from FarmGame import Player
class Wheat():
    buyPrice = 15
    sellPrice = 10
    multiplier = 2
    planted = 0
    @staticmethod
    def buyWheatAmount(x):
        if (x*Wheat.buyPrice > Player.Player.money):
            print ("Not enough money")
        else:
            Player.Player.money -= x * Wheat.buyPrice
            Player.Player.wheat += x

    def sellWheatAmount(x):
        if x > Player.Player.wheat:
            print("Not enough wheat to sell!")
        else:
            Player.Player.money += (x * Wheat.sellPrice)
            Player.Player.wheat -= x
    def grownWheat(x):
        Player.Player.wheat -= int(x)
        Wheat.planted += int(x)
    @staticmethod
    def harvestWheat():
        Player.Player.wheat += (Wheat.planted * Wheat.multiplier)

        Farm.Farm.farmSize += Wheat.planted
        Wheat.planted -= Wheat.planted


class Corn():
    buyPrice = 20
    sellPrice = 15
    multiplier = 2
    planted = 0

    def buyCornAmount(x):
        if (x*Corn.buyPrice > Player.Player.money):
            print ("Not enough money")
        else:
            Player.Player.money -= x * Corn.buyPrice
            Player.Player.wheat += x

    def sellCornAmount(x):
        if x > Player.Player.corn:
            print("Not enough wheat to sell!")
        else:
            Player.Player.money += (x * Corn.sellPrice)
            Player.Player.wheat -= x
    def grownCorn(x):
        Player.Player.corn -= int(x)
        Corn.planted += int(x)
    @staticmethod
    def harvestCorn():
        Player.Player.Corn += (Corn.planted * Corn.multiplier)

        Farm.Farm.farmSize += Corn.planted
        Corn.planted -= Corn.planted
