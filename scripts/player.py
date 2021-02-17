from vector2 import Vector2


class Player:
    def __init__(self, playerNumber, pygame, display):
        self.playerNumber = playerNumber
        self.location = Vector2()
        self.yVelocity = 0
        self.pygame = pygame
        self.display = display

        self.axe = 0
        self.pickaxe = 0
        self.hand = 0

    def setLocation(self, location):
        self.location = location

    def setX(self, x):
        self.location.x = x

    def setY(self, y):
        self.location.y = y

    def setYVelocity(self, yVelocity):
        self.yVelocity = yVelocity

    def addYVelocity(self, yVelocity):
        self.yVelocity += yVelocity

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

    def getYVelocity(self):
        return self.yVelocity

    def getAxe(self):
        return self.axe

    def getPickaxe(self):
        return self.pickaxe

    def getHand(self):
        return self.hand

    def getPlayerNumber(self):
        return self.playerNumber

    def isOnGround(self):
        try:
            return self.display.get_at((self.getX() + 1, self.getY() + 33)) != (0, 0, 0, 255) or \
                   self.display.get_at((self.getX() + 31, self.getY() + 33)) != (0, 0, 0, 255)
        except:
            return False

    def init(self):
        for x in range(0, 1100, 32):
            for y in range(0, 700, 32):
                # print("X=" + str(x) + " && Y=" + str(y) + ":", display.get_at((x, y)))
                try:
                    if self.display.get_at((x, y)) == (0, 0, 0, 255) and \
                            self.display.get_at((x, y + 32)) == (246, 195, 143, 255):
                        self.setLocation(Vector2(x, y))
                except:
                    pass

    def update(self):
        try:
            if self.pygame.key.get_pressed()[self.pygame.K_d] and \
                    self.display.get_at((self.getX() + 35, self.getY())) == (0, 0, 0, 255):
                self.moveX(3)
            if self.pygame.key.get_pressed()[self.pygame.K_a] and \
                    self.display.get_at((self.getX() - 3, self.getY())) == (0, 0, 0, 255):
                self.moveX(-3)
            if self.pygame.key.get_pressed()[self.pygame.K_w] and self.isOnGround():
                self.addYVelocity(-35)
            if self.pygame.key.get_pressed()[self.pygame.K_s]:
                self.moveY(3)
            self.moveY(self.getYVelocity())

            if not self.isOnGround():
                if self.getYVelocity() < 4:
                    self.addYVelocity(1)
            else:
                self.setYVelocity(0)
        except:
            pass
