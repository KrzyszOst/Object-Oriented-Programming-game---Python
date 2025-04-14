import random

from world.animals import animal

class Antelope(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 4, 4, 0)

    def action(self):
        super().action()
        super().action()

    def rollEscape(self):
        return True if random.randint(0, 1) == 1 else False

    def getName(self): return 'Antelope'

    def getSymbol(self): return 'A'
