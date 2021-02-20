import pygame, sys
from vector2 import Vector2
from input import *
from math import floor
from constants import *


class Player:
    def __init__(self, display, playerNumber, x=0, y=0, width=BLOCKWIDTH, speed=500, slipperiness=0.5, gravity=500):
        self.display = display
        self.playerNumber = playerNumber
        self.screenPosition = Vector2(x, y)
        self.pos = Vector2(x, y)
        self.velocity = Vector2()
        self.gravity = gravity
        self.width = width
        self.speed = speed
        self.jumpspeed = -800
        self.slipperiness = slipperiness
        self.scrollspeed = scrollspeed
        self.isOnGrounded = False
        self.pickaxe = 0
        self.lastDirection = 0  # 0 = Rien, 1= Droite, -1=Gauche
        self.tiles = tiles

    def setPickaxe(self, level):
        self.pickaxe = level

    def setPosition(self, x, y):
        self.pos = Vector2(x, y)

    def setX(self, x):
        self.pos.x = x

    def setY(self, y):
        self.pos.y = y

    def moveX(self, x):
        self.pos.x += x

    def moveY(self, y):
        self.pos.y += y

    def getPosition(self):
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

    def getPickaxe(self):
        return self.pickaxe

    def getPlayerNumber(self):
        return self.playerNumber

    def isOnGround(self, map, x, y):
        # TODO: make it not a try:except C'est fait bg
        i = floor((y + self.width) / BLOCKWIDTH)
        j = floor(x / BLOCKWIDTH)
        if i + 1 < len(map):
            # print(i, j, map[i][j])
            return self.tiles[map[i + 1][j]].collide
        else:
            return False

    def cannotGoX(self, map):
        i = floor((self.pos.y + self.width) / self.width)
        if self.velocity.x and i < len(map):
            if self.velocity.x > 0:
                print(i, int((self.pos.y + self.width + self.width) // self.width),
                      map[i][int((self.pos.y + self.width + self.width) // self.width)])
                return self.tiles[map[i][int((self.pos.y + self.width + self.width) // self.width)]].collide
            elif self.velocity.x < 0:
                print(i, int(self.pos.y // self.width), map[i][int(self.pos.y // self.width)])
                return self.tiles[map[i][int(self.pos.y // self.width)]].collide
        return False

    def tryMining(self, map):
        pass
        # TODO: Detection si y a un block avec self.lastDirection
        # TODO Si y a block le casser et le mettre dans l'inv

    def update(self, delta, map):
        inp = [None, get_input_wasd, get_input_arrows]
        inputVector = inp[self.playerNumber]()
        vel = self.velocity
        pos = self.pos

        # Horizontal movement
        vel.x += inputVector.x * self.speed
        vel.x *= self.slipperiness

        # Gravity
        vel.y += self.gravity

        # Jumping
        if inputVector.y < 0:
            vel.y = self.jumpspeed

        # Collision
        if self.isOnGround(map, pos.x + vel.x, pos.y):
            vel.x -= vel.x
        if self.isOnGround(map, pos.x, pos.y+vel.y):
            vel.y -= vel.y

        # Apply velocity
        self.velocity = vel * delta
        self.pos += self.velocity


        #Scroll
        #self.pos.y += self.scrollspeed


    def update_old(self, map):

        # if self.pos.y//self.width>len(map):
        # pygame.quit()
        # sys.exit()

        self.velocity.x *= self.slipperiness
        self.velocity.x += get_input_wasd().x * self.speed
        cannotGoX = self.cannotGoX(map)
        print(cannotGoX)
        if cannotGoX or -0.01 < self.velocity.x < 0.01:
            self.velocity.x = 0
            if self.velocity.x < 0:
                self.lastDirection = -1
            if self.velocity.x > 0:
                self.lastDirection = 1

        self.isOnGrounded = self.isOnGround(map)
        # print(self.isOnGrounded)
        # Gravity & velocity
        self.velocity.y += 0.4
        # Collision
        if self.isOnGrounded:
            self.velocity.y = 0
            # if self.pos.y%self.width !=0 :s
            #    self.pos.y = floor(self.pos.y/self.width)*self.width

        # Jumping
        if self.isOnGrounded and get_input_wasd().y < 0:
            self.velocity.y = -17

        self.pos += self.velocity
        # Scroll
        self.pos.y += self.scrollspeed

        # MINING
        if get_input_space():
            self.tryMining()

        # if self.isOnGrounded and self.pos.y%self.width !=0 :
        #    self.pos.y = floor(self.pos.y/self.width)*self.width

        # if not self.isOnGround(map):
        #     if self.getYVelocity() < 4:
        #         self.addYVelocity(1)
        # else:
        #     self.setYVelocity(0)

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
