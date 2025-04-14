from world.plants import plant

class Grass(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 0, 0, 0)

    def getName(self):
        return 'Grass'

    def getSymbol(self):
        return 't'
