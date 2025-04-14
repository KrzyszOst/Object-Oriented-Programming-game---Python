import pickle

class World:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._world = {}
        self._humanAlive = True
        self._specialActive = False
        self._specialDuration = 0  # 10 rounds
        self._cooldownActive = False
        self._cooldownDuration = 0  # 5 rounds
        self._turn = 0

    def addOrganism(self, organism):
        if self._world.get((organism.getX(), organism.getY())) is None:
            self._world[(organism.getX(), organism.getY())] = organism

    def resolve(self, char):
        self.nextTurn()

        print('Turn:', str(self._turn))
        print('Organisms:', str(len(self._world)), '\n')

        if self.findHuman() is None:
            self.killHuman()

        if self._humanAlive:
            if char == 'r' or char == 'R':
                if self._humanAlive and not self._specialActive and not self._cooldownActive:
                    self._specialActive = True
                    self._specialDuration = 10
                    self.findHuman().empower()
                else:
                    print('Wait before you can use special again')

            if self._specialActive:
                self._specialDuration -= 1
                self.findHuman().looseStrength()
                if self._specialDuration == 0:
                    self._specialActive = False
                    self._cooldownActive = True
                    self._cooldownDuration = 5
            elif self._cooldownActive:
                self._cooldownDuration -= 1
                if self._cooldownDuration == 0:
                    self._cooldownActive = False
            if self._specialActive:
                print('Special ability duration:', str(self._specialDuration), 'rounds\n')
            elif self._cooldownActive:
                print('Special ability cooldown:', str(self._cooldownDuration), 'rounds\n')
            else:
                print('Special ability ready to use (R)\n')

        for y in range(self._height):
            for x in range(self._width):
                if (x, y) in self._world and self.getOrganism(x, y).getName() != 'Human':
                    self._world[(x, y)].action()
                elif (x, y) in self._world and self.getOrganism(x, y).getName() == 'Human':
                    self._world[(x, y)].actionC(char)

        self.draw()

    def draw(self):
        #todo: remove debug
        """for organism in self._world.values():
            print(organism.getSymbol(), organism.getX(), organism.getY(), end='\n')
        print()"""

        for i in range(self._width):
            for j in range(self._height):
                if (i, j) in self._world:
                    organism = self._world[(i, j)]
                    x = organism.getX()
                    y = organism.getY()
                    if x != i or y != j:
                        temp = self.getOrganism(i, j)
                        self.setOrganism(x, y, temp)
                        self.removeOrganism(i, j)

        for y in range(self._height):
            for x in range(self._width):
                if (x, y) in self._world:
                    print(self._world[(x, y)].getSymbol(), end=' ')
                else:
                    print('-', end=' ')
            print()

    def nextTurn(self):
        for organism in self._world.values():
            organism.setAge(organism.getAge() + 1)
        self._turn += 1

    def getTurn(self):
        return self._turn

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getWorld(self):
        return self._world

    def getOrganism(self, x, y):
        return self._world.get((x, y))

    def setOrganism(self, x, y, organism):
        self._world[(x, y)] = organism

    def removeOrganism(self, x, y):
        if (x, y) in self._world:
            del self._world[(x, y)]

    def isHumanAlive(self):
        return self._humanAlive

    def killHuman(self):
        self._humanAlive = False

    def findHuman(self):
        for organism in self._world.values():
            if organism.getName() == 'Human':
                return organism
        return None

    def useSpecial(self):
        self._specialActive = True
        self._specialDuration = 10

    def getSpecialActive(self):
        return self._specialActive

    def getSpecialDuration(self):
        return self._specialDuration

    def getCooldownActive(self):
        return self._cooldownActive

    def getCooldownDuration(self):
        return self._cooldownDuration

    def countOrganisms(self):
        return len(self._world)

    def save(self):
        print('Saving...')
        with open('world.sav', 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load():
        print('Loading...')
        with open('world.sav', 'rb') as file:
            savedWorld = pickle.load(file)
        return savedWorld
