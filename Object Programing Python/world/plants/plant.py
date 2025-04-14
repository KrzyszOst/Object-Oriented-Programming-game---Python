from world import organism

class Plant(organism.Organism):
    def __init__(self, x, y, world, initiative, strength, age):
        super().__init__(x, y, world, initiative, strength, age)

    def getName(self): pass

    def getSymbol(self): pass
