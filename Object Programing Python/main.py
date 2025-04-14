import random

from world.graphic import WorldMap
from world import world
from world.animals import sheep, wolf, fox, turtle, antelope, human, cyberSheep
from world.plants import grass, dandelion, guarana, nightShade, pineBorscht

def game(worldX):
    ui = WorldMap(worldX)
    ui.start()
    # while char != 'q' and char != 'Q':
    #     print(char)
    #     if char == 's' or char == 'S':
    #         worldX.save()
    #     elif char == 'l' or char == 'L':
    #         temp = worldX.load()
    #         if temp is not None:
    #             worldX = temp
    #             #worldX.draw()
    #     else:
    #         worldX.resolve(char)
    #         ui.updateGrid()
    #     char = ui.start()

if __name__ == '__main__':                            # y x 0 1 2
    world0 = world.World(5, 5) # width x height       # 0   - - -
    # maxX = world0.getWidth() - 1                    # 1   - - -
    # maxY = world0.getHeight() - 1                   # 2   - - -

    # standard
    world0.addOrganism(sheep.Sheep(0, 0, world0))
    world0.addOrganism(wolf.Wolf(4, 4, world0))

    # turtle test
    world2 = world.World(3, 3)
    world2.addOrganism(sheep.Sheep(0, 0, world2))
    world2.addOrganism(turtle.Turtle(1, 1, world2))

    # human special test
    world3 = world.World(5, 5)
    world3.addOrganism(human.Human(0, 0, world3))
    world3.addOrganism(guarana.Guarana(1, 0, world3))
    world3.addOrganism(sheep.Sheep(2, 2, world3))
    world3.addOrganism(wolf.Wolf(4, 4, world3))

    # cyber sheep test
    world4 = world.World(5, 5)
    world4.addOrganism(cyberSheep.CyberSheep(2, 1, world4))
    world4.addOrganism(pineBorscht.PineBorscht(0, 0, world4))
    world4.addOrganism(pineBorscht.PineBorscht(4, 4, world4))

    # pine borscht test
    world5 = world.World(5, 5)
    world5.addOrganism(pineBorscht.PineBorscht(1, 1, world5))
    world5.addOrganism(pineBorscht.PineBorscht(3, 1, world5))
    world5.addOrganism(pineBorscht.PineBorscht(1, 3, world5))
    world5.addOrganism(pineBorscht.PineBorscht(3, 3, world5))
    world5.addOrganism(sheep.Sheep(2, 2, world5))

    # free
    world6 = world.World(9, 9)
    world6.addOrganism(human.Human(4, 4, world6))
    world6.addOrganism(sheep.Sheep(1, 1, world6))
    world6.addOrganism(sheep.Sheep(7, 1, world6))
    world6.addOrganism(sheep.Sheep(1, 7, world6))
    world6.addOrganism(sheep.Sheep(7, 7, world6))

    world1 = world.World(20, 20)
    maxX = 19
    maxY = 19
    world1.addOrganism(human.Human(0, 0, world1))
    [world1.addOrganism(sheep.Sheep(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in range(5)]
    [world1.addOrganism(wolf.Wolf(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in range(4)]
    [world1.addOrganism(fox.Fox(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in range(2)]
    [world1.addOrganism(turtle.Turtle(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in range(1)]
    [world1.addOrganism(antelope.Antelope(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in
     range(2)]
    [world1.addOrganism(cyberSheep.CyberSheep(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in
     range(1)]
    [world1.addOrganism(grass.Grass(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in range(5)]
    [world1.addOrganism(dandelion.Dandelion(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in
     range(2)]
    [world1.addOrganism(guarana.Guarana(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in
     range(3)]
    [world1.addOrganism(nightShade.NightShade(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in
     range(2)]
    [world1.addOrganism(pineBorscht.PineBorscht(random.randint(0, maxX - 1), random.randint(0, maxY), world1)) for i in
     range(2)]

    game(world3)
