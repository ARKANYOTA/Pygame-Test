import pygame
from vector2 import *
from random import randint, uniform
from math import sin, cos, floor

class PerlinNoise:
    def __init__(self, seed=uniform(-65536, 65535), x=0, y=0, scale=5, width=15, height=25):
        self.seed = seed
        self.scale = scale
        self.pos = Vector2(x, y)
        self.screenpos = Vector2(0, 0)
        self.width = width
        self.height = height
        self.map = []
        self.groundImg = pygame.image.load("../textures/dummyGround.png")
        self.groundBGImg = pygame.image.load("../textures/dummyDecoGround.png")

    def smoothstep(self, a0, a1, w):
        #return (a1 - a0) * w + a0; # linear interpolation >> (uglier result but faster)
        return (a1 - a0) * (3.0 - w * 2.0) * w * w + a0 # cubic

    def smoothstep2(self, a0, a1, w):
        # no noticable difference with smoothstep(), only use this if more smoothness is needed
        return (a1-a0) * ((w* (w*6.0 - 15.0) + 10.0) * w*w*w) + a0

    def randomGrid(self, ix, iy):
        # Random float. No precomputed gradients mean this works for any number of grid coordinates
        # Readapted from source C code: https://en.wikipedia.org/wiki/Perlin_noise
        random = 2920.0 * sin(ix * 21942.0 + iy * 171324.0 + 8912.0 + self.seed) * cos(ix * 23157.0 * self.seed * iy * 217832.0 + 9758.0)
        return Vector2(cos(random), sin(random))

    def perlin_noise(self, x, y, scale=1):
        # Returns perlin noise value for (x, y)
        x /= scale
        y /= scale

        #  (x0,y0) - (x1,y0)
        #  |         |
        #  (x0,y1) - (x1,y1)
        x0 = floor(x)
        x1 = x0 + 1
        y0 = floor(y)
        y1 = y0 + 1

        # Compute weights for interpolation for later on
        sx = x-x0
        sy = y-y0

        # Compute dot products of vectors in nearby grids
        v0 = self.randomGrid(x0, y0)
        d0 = Vector2(x - x0, y - y0)
        dot0 = v0.dot(d0)

        v1 = self.randomGrid(x1, y0)
        d1 = Vector2(x - x1, y - y0)
        dot1 = v1.dot(d1)

        s0 = self.smoothstep(dot0, dot1, sx)

        v0 = self.randomGrid(x0, y1)
        dot0 = v0.x * (x-x0) + v0.y * (y-y1)
        v1 = self.randomGrid(x1, y1)
        dot1 = v1.x * (x-x1) + v1.y * (y-y1)

        s1 = self.smoothstep(dot0, dot1, sx)
        val = self.smoothstep(s0, s1, sy)

        return (val+1)/2

    def clamp(self, val, a, b):
        return max(a, min(val, b))

    def create_noisemap_list(self):
        li = [[0] * self.width] * self.height
        for row in range(self.height):
            li2 = [0] * self.width
            for col in range(self.width):
                noise = self.perlin_noise(col+self.pos.x, row+self.pos.y, self.scale)
                if .56 < noise:
                    noise = 2
                elif .45 < noise:
                    noise = 1
                else:
                    noise = 0
                li2[col] = noise
            li[row] = li2
        self.map = li

    def update_map(self):
        del self.map[-1]
        li2 = [0] * self.width
        for col in range(self.width):
            noise = self.perlin_noise(col+self.pos.x, 0+self.pos.y, self.scale)
            if .56 < noise:
                noise = 2
            elif .45 < noise:
                noise = 1
            else:
                noise = 0
            li2[col] = noise
        self.map.insert(0,li2)


    def print_perlin_noise(self, display, screen_x, screen_y, blockwidth, tileTextures):
        for row in range(self.height):
            for col in range(self.width):
                noise = self.map[row][col]
                display.blit(tileTextures[noise], (col*blockwidth + screen_x, row*blockwidth + screen_y))
        return True

    def find_empty_xy(self, blockw):
        y=len(self.map)//2
        x=len(self.map[0])//2
        for i in range(1,int(len(self.map))) :
            for k in range(1,i+1):
                if self.map[y][x]!=2 and self.map[y+1][x]==2: #check if emplacement is clear (replace by 0 in next update)
                    return (y-1)*blockw,x*blockw
                else :
                    if i%2==0:
                        x-=1
                    else :
                        x+=1
            for l in range(1,i+1):
                if self.map[y][x]!=2 and self.map[y+1][x]==2: #check if emplacement is clear (replace by 0 in next update)
                    return (y-1)*blockw,x*blockw
                else :
                    if i%2==0:
                        y+=1
                    else :
                        y-=1

