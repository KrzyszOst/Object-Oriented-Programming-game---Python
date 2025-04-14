import random

from world import organism

class Animal(organism.Organism):
    def __init__(self, x, y, world, initiative, strength, age):
        super().__init__(x, y, world, initiative, strength, age)

    def action(self):
        d = random.randint(0, 3)
        if d == 0:
            if self._x > 0:
                if self._world.getOrganism(self._x - 1, self._y) is not None:
                    self.collision(self, self._world.getOrganism(self._x - 1, self._y))
                else:
                    self._x -= 1
        elif d == 1:
            if self._x < self._world.getWidth() - 1:
                if self._world.getOrganism(self._x + 1, self._y) is not None:
                    self.collision(self, self._world.getOrganism(self._x + 1, self._y))
                else:
                    self._x += 1
        elif d == 2:
            if self._y > 0:
                if self._world.getOrganism(self._x, self._y - 1) is not None:
                    self.collision(self, self._world.getOrganism(self._x, self._y - 1))
                else:
                    self._y -= 1
        elif d == 3:
            if self._y < self._world.getHeight() - 1:
                if self._world.getOrganism(self._x, self._y + 1) is not None:
                    self.collision(self, self._world.getOrganism(self._x, self._y + 1))
                else:
                    self._y += 1

    def collision(self, attacker, defender):
        if defender.getInitiative() == 0:
            if defender.getName() == 'Guarana':
                print(attacker.getName(), 'ate', defender.getName(), 'and gained +3 strength')
                attacker.buffStrength()
            elif defender.getName() == 'Nightshade':
                print(attacker.getName(), 'ate', defender.getName(), 'and died')
                if attacker.getName() == 'Human':
                    self._world.killHuman()
                self._world.removeOrganism(attacker.getX(), attacker.getY())
                self._world.removeOrganism(defender.getX(), defender.getY())
            elif defender.getName() == 'PineBorscht':
                if attacker.getName() == 'CyberSheep':
                    print(attacker.getName(), 'ate', defender.getName())
                    x = defender.getX()
                    y = defender.getY()
                    self._world.removeOrganism(x, y)
                    attacker.setX(x)
                    attacker.setY(y)
                else:
                    print(attacker.getName(), 'tried to eat', defender.getName(), 'and died')
                    if attacker.getName() == 'Human':
                        self._world.killHuman()
                    self._world.removeOrganism(attacker.getX(), attacker.getY())
            else:
                print(attacker.getName(), 'ate', defender.getName())
                self._world.removeOrganism(defender.getX(), defender.getY())
        elif attacker.getName() == 'Turtle':
            if defender.checkdefence(attacker):
                print(attacker.getName(), 'tried to attack', defender.getName(), 'but failed')
        elif defender.getName() == 'Antelope':
            if attacker.getStrength() >= defender.getStrength():
                if defender.rollEscape():
                    print(defender.getName(), 'escaped from', attacker.getName())
                else:
                    print(attacker.getName(), 'killed', defender.getName())
                    if defender.getName() == 'Human':
                        self._world.killHuman()
                    self._world.setOrganism(attacker, defender.getX(), defender.getY())
                    self._world.removeOrganism(attacker.getX(), attacker.getY())
            else:
                print(defender.getName(), 'killed', attacker.getName())
                if attacker.getName() == 'Human':
                    self._world.killHuman()
                self._world.removeOrganism(attacker.getX(), attacker.getY())
        else:
            if attacker.getStrength() >= defender.getStrength():
                print(attacker.getName(), 'killed', defender.getName())
                if defender.getName() == 'Human':
                    self._world.killHuman()
                self._world.setOrganism(attacker, defender.getX(), defender.getY())
                self._world.removeOrganism(attacker.getX(), attacker.getY())
            else:
                print(defender.getName(), 'killed', attacker.getName())
                if attacker.getName() == 'Human':
                    self._world.killHuman()
                self._world.removeOrganism(attacker.getX(), attacker.getY())

    def getName(self): pass

    def getSymbol(self): pass

    def checkDefence(self, attacker): pass

    def rollEscape(self): pass

    def goUp(self):
        if self._y > 0:
            if self._world.getOrganism(self._x, self._y - 1) is not None:
                self.collision(self, self._world.getOrganism(self._x, self._y - 1))
            else:
                self._y -= 1

    def goDown(self):
        if self._y < self._world.getHeight() - 1:
            if self._world.getOrganism(self._x, self._y + 1) is not None:
                self.collision(self, self._world.getOrganism(self._x, self._y + 1))
            else:
                self._y += 1

    def goLeft(self):
        if self._x > 0:
            if self._world.getOrganism(self._x - 1, self._y) is not None:
                self.collision(self, self._world.getOrganism(self._x - 1, self._y))
            else:
                self._x -= 1

    def goRight(self):
        if self._x < self._world.getWidth() - 1:
            if self._world.getOrganism(self._x + 1, self._y) is not None:
                self.collision(self, self._world.getOrganism(self._x + 1, self._y))
            else:
                self._x += 1