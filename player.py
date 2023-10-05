from stats import *

class Player:
    def __init__(self, name, faction, health, defense):
        self.name = name
        self.faction = faction
        self.stats = [Stat("Health", 0, 100), Stat("Defense", 0, 100)]
        self.updatestat(health, "Health")
        self.updatestat(defense, "Defense")

    def displaystats(self):
        for stat in self.stats:
            stat.display()

    def updatestat(self, val, name):
        #self.stats[0].setvalue(val)
        for stat in self.stats:
            if stat.name == name: 
                stat.setvalue(val)