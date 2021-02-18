import pygame,sys
from vector2 import Vector2
from input import *

class Player:
    def __init__(self, display, playerNumber, x=0, y=0, width=32, speed=0.5, slipperiness=0.9):
        self.display =  display
        self.playerNumber = playerNumber
        self.screenPosition = Vector2(x, y)
        self.pos = Vector2(x, y)
        self.velocity = Vector2()
        self.width = width
        self.speed = speed
        self.slipperiness = slipperiness

        self.isGrounded = False
        self.axe = 0
        self.pickaxe = 0
        self.hand = 0

    def setAxe(self, level):
        self.axe = level
    def setPickaxe(self, level):
        self.pickaxe = level
    def setHand(self, tool):
        self.hand = tool

    def setposition(self, x, y):
        self.pos = Vector2(x, y)
    def setX(self, x):
        self.pos.x = x
    def setY(self, y):
        self.pos.y = y
    def moveX(self, x):
        self.pos.x += x
    def moveY(self, y):
        self.pos.y += y

    def getposition(self):
        return self.pos
    def getX(self):
        return self.pos.x
    def getY(self):
        return self.pos.y

    def getVelocity(self):
        return self.velocity
    def getXVelocity(self):
        return self.velocity.x
    def getYVelocity(self):
        return self.velocity.y

    def addXVelocity(self, xVelocity):
        self.velocity.x += xVelocity
    def setXVelocity(self, xVelocity):
        self.velocity.x = xVelocity
    def addYVelocity(self, yVelocity):
        self.velocity.y += yVelocity
    def setYVelocity(self, yVelocity):
        self.velocity.y = yVelocity

    def getAxe(self):
        return self.axe
    def getPickaxe(self):
        return self.pickaxe
    def getHand(self):
        return self.hand
    def getPlayerNumber(self):
        return self.playerNumber

    def isOnGround(self, map):
        # TODO: make it not a try:except C'est fait bg
        i = int((self.pos.y + self.width) // self.width + 1)
        j = int(self.pos.x // self.width)
        if i< len(map):
            return map[i][j] == 2
        else :
            return False

    def cannotGoX(self, map):
        if self.velocity.x :
            if self.velocity.x>0:
                return map[int(self.pos.y//self.width)][int((self.pos.y+self.width)//self.width)] == 2
            elif self.velocity.x<0:
                return map[int(self.pos.y//self.width)][int((self.pos.y-self.width)//self.width)] == 2
        return False

    # def init(self):
    #     for x in range(0, 1100, 32):
    #         for y in range(0, 700, 32):
    #             # print("X=" + str(x) + " && Y=" + str(y) + ":", display.get_at((x, y)))
    #             try:
    #                 if self.display.get_at((x, y)) == (0, 0, 0, 255) and \
    #                         self.display.get_at((x, y + 32)) == (246, 195, 143, 255):
    #                     self.setposition(Vector2(x, y))
    #             except:
    #                 pass

    def update(self, map):

        #if self.pos.y//self.width>len(map):
            #pygame.quit()
            #sys.exit()

        SCROLLSPEED = 0

        self.velocity *= self.slipperiness
        self.velocity.x += get_input_wasd().x * self.speed
        self.pos += self.velocity
        cannotGoX = self.cannotGoX(map)
        print(self.isGrounded)
        if cannotGoX :
            self.velocity.x=0

        self.isGrounded = self.isOnGround(map)

        # Jumping
        if self.isGrounded and get_input_wasd().y < 0:
            self.velocity.y = -15

        #Scroll
        self.pos.y += SCROLLSPEED
        # Gravity & velocity
        self.velocity.y += 2
        # Collision
        if not self.isGrounded:
            self.velocity.y = 0

        self.pos += self.velocity
        # if not self.isOnGround(map):
        #     if self.getYVelocity() < 4:
        #         self.addYVelocity(1)
        # else:
        #     self.setYVelocity(0)
