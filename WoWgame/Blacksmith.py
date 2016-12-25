from WoWgame import Player
class Gear():
    buyPrice = 15
    sellPrice = 10

    def buyGearAmount(x):
        if (x*Gear.buyPrice > Player.Player.money):
            print ("Not enough money")
        else:
            Player.Player.money -= x * Gear.buyPrice
            Player.Player.gear += x
            Player.Player.itemlevel = Player.Player.itemlevel + (x * int(5))

    def sellGearAmount(x):
        if x > Player.Player.gear:
            print("Not enough Gear to sell!")
        else:
            Player.Player.money += (x * Gear.sellPrice)
            Player.Player.gear -= x
            Player.Player.itemlevel = Player.Player.itemlevel - (x * int(5))




class Weapons():
    buyPrice = 20
    sellPrice = 15

    def buyWeaponsAmount(x):
        if (x * Weapons.buyPrice > Player.Player.money):
            print("Not enough money")
        else:
            Player.Player.money -= x * Weapons.buyPrice
            Player.Player.itemlevel = Player.Player.itemlevel + (x * 10)




    def sellWeaponsAmount(x):
        if x > Player.Player.weapons:
            print("Not enough Weapons to sell!")
        else:
            Player.Player.money += x * Weapons.sellPrice
            Player.Player.itemlevel = Player.Player.itemlevel - ( x * 10)



