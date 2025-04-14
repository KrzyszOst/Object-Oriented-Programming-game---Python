from world.animals import animal

class Wolf(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 5, 9, 0)

    def getName(self): return 'Wolf'

    def getSymbol(self): return 'W'
