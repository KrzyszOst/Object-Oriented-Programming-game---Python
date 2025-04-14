from world.plants import plant

class Dandelion(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 0, 0, 0)

    #todo tries to reproduce 3 times

    def getName(self):
        return 'Dandelion'

    def getSymbol(self):
        return 'd'
