from world.plants import plant

class PineBorscht(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 0, 10, 0)

    #kill every animal in proximity
    def action(self):
        if self._x > 0 and self._world.getOrganism(self._x - 1, self._y) is not None and \
                self._world.getOrganism(self._x - 1, self._y).getInitiative() > 0 and \
                self._world.getOrganism(self._x - 1, self._y).getName() != 'CyberSheep':
            print('Pine Borscht killed', self._world.getOrganism(self._x - 1, self._y).getName())
            self._world.removeOrganism(self._x - 1, self._y)
        if self._x < self._world.getWidth() - 1 and self._world.getOrganism(self._x + 1, self._y) is not None and \
                self._world.getOrganism(self._x + 1, self._y).getInitiative() > 0 and \
                self._world.getOrganism(self._x + 1, self._y).getName() != 'CyberSheep':
            print('Pine Borscht killed', self._world.getOrganism(self._x + 1, self._y).getName())
            self._world.removeOrganism(self._x + 1, self._y)
        if self._y > 0 and self._world.getOrganism(self._x, self._y - 1) is not None and \
                self._world.getOrganism(self._x, self._y - 1).getInitiative() > 0 and \
                self._world.getOrganism(self._x, self._y - 1).getName() != 'CyberSheep':
            print('Pine Borscht killed', self._world.getOrganism(self._x, self._y - 1).getName())
            self._world.removeOrganism(self._x, self._y - 1)
        if self._y < self._world.getHeight() - 1 and self._world.getOrganism(self._x, self._y + 1) is not None and \
                self._world.getOrganism(self._x, self._y + 1).getInitiative() > 0 and \
                self._world.getOrganism(self._x, self._y + 1).getName() != 'CyberSheep':
            print('Pine Borscht killed', self._world.getOrganism(self._x, self._y + 1).getName())
            self._world.removeOrganism(self._x, self._y + 1)

    def getName(self):
        return 'PineBorscht'

    def getSymbol(self):
        return 'p'
