from vector2 import Vector2


class Player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.location = Vector2()

        self.axe = 0
        self.pickaxe = 0
        self.hand = 0

    def setLocation(self, location):
        self.location = location

    def setX(self, x):
        self.location.x = x

    def setY(self, y):
        self.location.y = y

    def moveX(self, x):
        self.location.x += x

    def moveY(self, y):
        self.location.y += y

    def setAxe(self, level):
        self.axe = level

    def setPickaxe(self, level):
        self.pickaxe = level

    def setHand(self, tool):
        self.hand = tool

    def getLocation(self):
        return self.location.x, self.location.y

    def getX(self):
        return self.location.x

    def getY(self):
        return self.location.y

    def getAxe(self):
        return self.axe

    def getPickaxe(self):
        return self.pickaxe

    def getHand(self):
        return self.hand

    def getPlayerNumber(self):
        return self.playerNumber
