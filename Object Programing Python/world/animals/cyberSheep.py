from world.animals import animal

class CyberSheep(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 4, 11, 0)

    def action(self):
        nearest = self.findNearestPB()
        if nearest is not None:
            if nearest.getX() < self._x:
                self.goLeft()
            elif nearest.getX() > self._x:
                self.goRight()
            elif nearest.getY() < self._y:
                self.goUp()
            elif nearest.getY() > self._y:
                self.goDown()
        else:
            super().action()

    def getName(self): return 'CyberSheep'

    def getSymbol(self): return 'C'

    def findNearestPB(self):
        nearest = None
        nearestDistance = 100
        for i in range(self._world.getWidth()):
            for j in range(self._world.getHeight()):
                if self._world.getOrganism(i, j) is not None and \
                        self._world.getOrganism(i, j).getName() == 'PineBorscht':
                    distance = abs(self._x - i) + abs(self._y - j)
                    if distance < nearestDistance:
                        nearest = self._world.getOrganism(i, j)
                        nearestDistance = distance
        return nearest
