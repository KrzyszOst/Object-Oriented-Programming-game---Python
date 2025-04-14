from world.animals import animal

class Human(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 4, 5, 0)

    def actionC(self, char):
        if char == 'w' or char == 'W':
            self.goUp()
        elif char == 's' or char == 'S':
            self.goDown()
        elif char == 'a' or char == 'A':
            self.goLeft()
        elif char == 'd' or char == 'D':
            self.goRight()

    def empower(self): self._strength += 10

    def looseStrength(self): self._strength -= 1

    def getName(self): return 'Human'

    def getSymbol(self): return '@'
