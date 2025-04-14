class Organism:
    def __init__(self, x, y, world, initiative, strength, age):
        self._initiative = initiative
        self._strength = strength
        self._age = age
        self._x = x
        self._y = y
        self._world = world

    def action(self): pass

    def actionC(self, char): pass

    def collision(self, attacker, defender): pass

    def getName(self): pass

    def getSymbol(self): pass

    def getInitiative(self): return self._initiative

    def getStrength(self): return self._strength

    def buffStrength(self): self._strength += 3

    def getAge(self): return self._age

    def setAge(self, age): self._age = age

    def getX(self): return self._x

    def setX(self, x): self._x = x

    def getY(self): return self._y

    def setY(self, y): self._y = y

    def getWorld(self): return self._world

    def __repr__(self):
        return "%s(%d, %d)" % (self.getName(), self._x, self._y)
