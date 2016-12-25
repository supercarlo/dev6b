import random
from WoWgame import Player
class Missions:
    missions = 3
    RNG = random.randint(0,25)
    def startMission(x):
        if int(x) > Missions.missions:
            print ("Not enough missions available")
        else:
            Missions.missions = Missions.missions - int(x)
    def collectMission(x):
        if Missions.missions == 3:
            print ("There are no missions going!")
        else:
            while Missions.missions != 3:
                Player.Player.money = Player.Player.money + 25
                if Missions.RNG == 25:
                    Player.Player.weapons = Player.Player.weapons + 1
                    print("Lucky! You got an extra weapon from your mission!")
                Missions.missions = Missions.missions + 1






