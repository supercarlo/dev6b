from FarmGame import FarmStock
from FarmGame import Player

def game():
    playerStatus()
    x = str(input("buy, sell or exit      "))


    if x == "buy":
        y = str(input("What would you like to buy? Wheat (15 each) or Corn (20 each)    "))
        if y == "Wheat" or  y == "wheat":
            amount = str(input("How many would you like to buy?   "))
            FarmStock.Wheat.buyWheatAmount(int(amount))
        elif y == "Corn" or y ==  "corn":
            CornAmount = str(input("How many would you like to buy?   "))
            FarmStock.Corn.buyCornAmount(int(CornAmount))

    if x == "sell":
        y = str(input("What would you like to sell? Wheat (10 each) or corn (20 each)"))
        if y == "Wheat" or y == "wheat":
            amount = str(input("How many would you like to sell?   "))
            FarmStock.Wheat.sellWheatAmount(int(amount))
        elif y == "Corn" or y == "corn":
            amount = str(input("How many would you like to sell?   "))
            FarmStock.Corn.sellCornAmount(int(amount))


    if x != "exit":
        game()
    else:
        exit()


def playerStatus():
    print("Player money:   " + str(Player.Player.money))
    print("CORN amount in bag:  " + str(Player.Player.corn))
    print("WHEAT amount in bag:  " + str(Player.Player.wheat))


game()