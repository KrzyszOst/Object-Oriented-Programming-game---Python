import tkinter as tk

from world.animals import sheep, wolf, fox, turtle, antelope, cyberSheep
from world.plants import grass, dandelion, guarana, nightShade, pineBorscht
from world.world import World


class WorldMap:
    def __init__(self, world):
        self.world = world
        self.window = tk.Tk()
        self.buttons = []
        self.output_text = None

    def createGrid(self):
        for y in range(self.world.getHeight()):
            row = []
            for x in range(self.world.getWidth()):
                button = tk.Button(self.window, width=6, height=3)
                button.grid(row=y, column=x + 1)
                row.append(button)
                button.config(command=lambda i=x, j=y: self.addOrganism(i, j))
            self.buttons.append(row)

    def createOutputText(self):
        self.output_text = tk.Text(self.window, height=self.world.getHeight() * 3, width=20)
        self.output_text.grid(row=0, column=0, rowspan=self.world.getHeight(), padx=5, pady=5)

    def createControlButtons(self):
        roundButton = tk.Button(self.window, text="Next Round", width=18, height=3, command=self.nextRound)
        roundButton.grid(row=1, column=self.world.getWidth() + 3, columnspan=3)

        saveButton = tk.Button(self.window, text="Save", width=18, height=3, command=self.saveGame)
        saveButton.grid(row=2, column=self.world.getWidth() + 3, columnspan=3)

        loadButton = tk.Button(self.window, text="Load", width=18, height=3, command=self.loadGame)
        loadButton.grid(row=3, column=self.world.getWidth() + 3, columnspan=3)

        upButton = tk.Button(self.window, text="Up", width=6, height=3, command=self.up)
        upButton.grid(row=5, column=self.world.getWidth() + 4)

        leftButton = tk.Button(self.window, text="Left", width=6, height=3, command=self.left)
        leftButton.grid(row=6, column=self.world.getWidth() + 3)

        downButton = tk.Button(self.window, text="Down", width=6, height=3, command=self.down)
        downButton.grid(row=6, column=self.world.getWidth() + 4)

        rightButton = tk.Button(self.window, text="Right", width=6, height=3, command=self.right)
        rightButton.grid(row=6, column=self.world.getWidth() + 5)

        specialButton = tk.Button(self.window, text="Special", width=18, height=3, command=self.special)
        specialButton.grid(row=7, column=self.world.getWidth() + 3, columnspan=3)

    def nextRound(self):
        self.world.resolve('n')
        self.updateGrid()

    def saveGame(self):
        self.world.save()
        self.updateGrid()

    def loadGame(self):
        new_world = World.load()
        self.world = new_world
        self.world.draw()
        self.updateGrid()

    def up(self):
        self.world.resolve('w')
        self.updateGrid()

    def left(self):
        self.world.resolve('a')
        self.updateGrid()

    def down(self):
        self.world.resolve('s')
        self.updateGrid()

    def right(self):
        self.world.resolve('d')
        self.updateGrid()

    def special(self):
        self.world.resolve('r')
        self.updateGrid()

    def updateGrid(self):
        for y in range(self.world.getHeight()):
            for x in range(self.world.getWidth()):
                organism = self.world.getOrganism(x, y)
                if organism is not None:
                    symbol = organism.getSymbol()
                else:
                    symbol = '-'
                self.buttons[y][x].config(text=symbol)

    def start(self):
        self.window.title("Krzysztof Ostrzycki 193507")
        self.createOutputText()
        self.createGrid()
        self.createControlButtons()
        self.updateGrid()
        self.window.mainloop()