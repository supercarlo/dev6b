from FarmGame import Player
class Wheat():
    buyPrice = 15
    sellPrice = 10
    multiplier = 2

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
        return x * Wheat.multiplier

class Corn():
    buyPrice = 20
    sellPrice = 15
    multiplier = 2

    def buyCornAmount(x):
        if (x * Corn.buyPrice > Player.Player.money):
            print("Not enough money")
        else:
            Player.Player.money -= x * Corn.buyPrice
            Player.Player.corn += x


    def sellCornAmount(x):
        if x > Player.Player.corn:
            print("Not enough corn to sell!")
        else:
            Player.Player.money += x * Corn.sellPrice
            Player.Player.corn -= x

    def grownCorn(x,Time):
        if Time >= 10:
            Player.Player.Corn += (x * Corn.multiplier)
        else:
            pass

#
# print ("CORN amount in bag:  " + str(Player.Player.Corn))
# print ("WHEAT amount in bag:  " + str(Player.Player.Wheat))
# print ("Player money before buying   " + str(Player.Player.money))
# print ("Buying 2 Wheat  (15 each) ")
# Wheat.buyWheatAmount(2)
# print ("Player money after buying:   " + str(Player.Player.money))
# print()
# print ("Buying 1 Corn (20 each)  ")
# Corn.buyCornAmount(1)
# print ("CORN amount in bag:  " + str(Player.Player.Corn))
#
# print ("Player money after buying:   " + str(Player.Player.money))
# print ("TIME PASSED")
# Corn.grownCorn(Player.Player.Corn, 10 )
#
# print ()
# print ("CORN amount in bag:  " + str(Player.Player.Corn))
# print ("WHEAT amount in bag:  " + str(Player.Player.Wheat))
#
#

