import random

from world.animals import animal

class Fox(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 3, 7, 0)

    def action(self):
        d = random.randint(0, 3)
        if d == 0:
            if self._x > 0:
                if self._world.getOrganism(self._x - 1, self._y) is not None:
                    if self.getStrength() > self._world.getOrganism(self._x - 1, self._y).getStrength():
                        self.collision(self, self._world.getOrganism(self._x - 1, self._y))
                else:
                    self._x -= 1
        elif d == 1:
            if self._x < self._world.getWidth() - 1:
                if self._world.getOrganism(self._x + 1, self._y) is not None:
                    if self.getStrength() > self._world.getOrganism(self._x + 1, self._y).getStrength():
                        self.collision(self, self._world.getOrganism(self._x + 1, self._y))
                else:
                    self._x += 1
        elif d == 2:
            if self._y > 0:
                if self._world.getOrganism(self._x, self._y - 1) is not None:
                    if self.getStrength() > self._world.getOrganism(self._x, self._y - 1).getStrength():
                        self.collision(self, self._world.getOrganism(self._x, self._y - 1))
                else:
                    self._y -= 1
        elif d == 3:
            if self._y < self._world.getHeight() - 1:
                if self._world.getOrganism(self._x, self._y + 1) is not None:
                    if self.getStrength() > self._world.getOrganism(self._x, self._y + 1).getStrength():
                        self.collision(self, self._world.getOrganism(self._x, self._y + 1))
                else:
                    self._y += 1

    def getName(self): return 'Fox'

    def getSymbol(self): return 'F'
