from world.plants import plant

class Guarana(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 0, 0, 0)

    def getName(self):
        return 'Guarana'

    def getSymbol(self):
        return 'g'
