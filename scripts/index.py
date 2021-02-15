import sys, pygame
from vector2 import *
from perlinnoise import perlin_noise, print_perlin_oise
from random import randint, uniform
from math import sin, cos, floor

def get_dir():
    return Vector2(1* pygame.key.get_pressed()[pygame.K_RIGHT] - 1* pygame.key.get_pressed()[pygame.K_LEFT],
                   1* pygame.key.get_pressed()[pygame.K_DOWN]  - 1* pygame.key.get_pressed()[pygame.K_UP])

def randcol():
    return (randint(0,255), randint(0,255), randint(0,255))

def clamp(val, a, b):
    return max(a, min(val, b))

pygame.init()
worldseed = uniform(-65536,65535)
screensize = scrwidth, scrheight = 1100, 700
screen = pygame.display.set_mode(screensize)
DISPLAY = pygame.display.set_mode(screensize, 0, 32)

speed = [2, 2]
noiseposy = 0
blockw = 32
scale = 10
thresh = .5

groundImg = pygame.image.load("dummyGround.png")
groundImg = pygame.transform.scale(groundImg, (blockw, blockw))

def main():
    #WHITE = (255, 255, 255)
    #BLUE = (0, 0, 255)

    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            pass
            if event.type == pygame.QUIT:
                sys.exit()
        dirr = get_dir()
        update = False
        if dirr.x == 1:
            scale += 0.05
        elif dirr.x == -1:
            scale -= 0.05
        if dirr.y == -1:
            noiseposy -= .1
        elif dirr.y == 1:
            noiseposy += .1
        if pygame.key.get_pressed()[pygame.K_b]:
            update = True
            thresh -= 0.01
            print(thresh)
        if pygame.key.get_pressed()[pygame.K_n]:
            update = True
            thresh += 0.01
            print(thresh)
        print_perlin_noise(0, 0, 0, noiseposy, scrwidth // blockw, scrheight // blockw, scale, blockw)
        pygame.display.flip()


main()
