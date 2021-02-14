
class player:
    def __init__(self, playerNumber):
        self.player_number = playerNumber
        self.x = 0
        self.y = 0

        self.axe = 0
        self.pickaxe = 0
        self.hand = 0

    def setLocation(self, location):
        self.x = location[0]
        self.y = location[1]

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def moveX(self, x):
        self.x += x

    def moveY(self, y):
        self.y += y

    def setAxe(self, level):
        self.axe = level

    def setPickaxe(self, level):
        self.pickaxe = level

    def setHand(self, tool):
        self.hand = tool

    def getLocation(self):
        return self.x, self.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getAxe(self):
        return self.axe

    def getPickaxe(self):
        return self.pickaxe

    def getHand(self):
        return self.hand

    def getPlayerNumber(self):
        return self.player_number
