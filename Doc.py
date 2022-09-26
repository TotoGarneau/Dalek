import random
from controlleursMenu import JeuController
from Cellule import Grille


class Doc:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.life = True
        self.Docteur = "W"

    def move(self,x,y):
        self.x = x
        self.y = y

    def death(self):
        self.life = False

    def zappeur(self):
        zap = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                zap.append([self.x + x, self.y + y])
            if self.x == self.x+x and self.y == self.y+y:
                zap.pop()

        return zap

    def teleport(self):
        y = random.randrange(0, 8)
        x = random.randrange(0, 6)
        return x, y
