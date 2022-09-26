class Dalek :

    def __init__(self):
        self.Dalek = "D"
        self.life = True

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self,x,y):
        self.x = x
        self.y = y
