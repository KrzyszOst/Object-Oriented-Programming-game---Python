import random

from world.animals import animal

class Turtle(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 1, 2, 0)

    def action(self):
        super().action() if random.randint(0, 3) == 0 else None

    def checkDefence(self, attacker):
        return True if attacker.getStrength() < 5 else False

    def getName(self): return 'Turtle'

    def getSymbol(self): return 'T'
