from FarmGame import FarmStock
from FarmGame import Farm
from FarmGame import Player

class planting():
    plantList = []
    def plantSeeds(x,y):
        # print (x,     y)
        if int(x) > int(Farm.Farm.farmSize):
            print ("Not enough space!")
        else:
            Farm.Farm.farmSize -= int(x)
            planting.plantList.append(y)
