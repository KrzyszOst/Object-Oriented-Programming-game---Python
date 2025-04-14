from world.plants import plant

class NightShade(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 0, 99, 0)

    def getName(self):
        return 'NightShade'

    def getSymbol(self):
        return 'n'
