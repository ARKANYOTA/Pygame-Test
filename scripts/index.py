import sys, pygame
from vector2 import *
from perlinnoise import *
from random import randint, uniform
from math import sin, cos, floor
from time import sleep

def get_dir():
    return Vector2(1* pygame.key.get_pressed()[pygame.K_RIGHT] - 1* pygame.key.get_pressed()[pygame.K_LEFT],
                   1* pygame.key.get_pressed()[pygame.K_DOWN]  - 1* pygame.key.get_pressed()[pygame.K_UP])
def randcol():
    return (randint(0,255), randint(0,255), randint(0,255))
def clamp(val, a, b):
    return max(a, min(val, b))

def update_map(map, posy):
    pass
    # blkw=blockw
    # del map[-1]
    # map.insert(0,[0 for b in range(scrwidth // blockw)])
    # for i in range(scrwidth // blockw) :
    #     val = perlin_noise(i/10+0, 1/10+posy)
    #     val = floor( (val+.5) *5)/5
    #     val = clamp( (128*(val+1)), 0, 255)
    #     if 190 < val:
    #         map[0][i] = 255
    #     elif 150 < val:
    #         map[0][i] = 127
    #     else:
    #         map[0][i] = 0
    # for h in range(len(map)) :
    #     for w in range(len(map[0])) :
    #         pygame.draw.rect(DISPLAY, (map[h][w], map[h][w], map[h][w]), (w*blkw, h*blkw, blkw, blkw))


def main():
    # Pygame & screen setup
    pygame.init()
    screensize = scrwidth, scrheight = 1100, 700
    screen = pygame.display.set_mode(screensize)
    DISPLAY = pygame.display.set_mode(screensize, 0, 32)

    # Textures

    # Game constants
    BLOCKWIDTH = 32
    SEED = uniform(-65536, 65535)

    # Game variables
    map = [[0 for k in range(scrwidth)] for i in range(scrheight)]
    noise = PerlinNoise(SEED, 0, 0, 10)
    noiseposy = 0
    scale = 10

    noise.print_perlin_noise(DISPLAY, 0, 0, scrwidth // BLOCKWIDTH, scrheight // BLOCKWIDTH, BLOCKWIDTH)
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        noise.print_perlin_noise(DISPLAY, 0, 0, scrwidth//BLOCKWIDTH, scrheight//BLOCKWIDTH, BLOCKWIDTH)
        noise.y -= 1

        pygame.display.flip()
        pygame.time.delay(500)

main()