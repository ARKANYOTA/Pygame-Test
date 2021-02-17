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

def main():
    # Pygame & screen setup
    pygame.init()
    screensize = scrwidth, scrheight = 1280, 640
    screen = pygame.display.set_mode(screensize)
    DISPLAY = pygame.display.set_mode(screensize, pygame.RESIZABLE)

#    screen = pygame.display.set_mode(size, RESIZABLE)
#    pygame.display.set_caption("My Game")

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass

        screen.fill((0,0,0))
        # Noise scrolling
        noiseposy += 5
        if noiseposy > BLOCKWIDTH:
            noise.y -= 1
            noiseposy %= BLOCKWIDTH
        noise.print_perlin_noise(DISPLAY, 0, noiseposy, scrwidth//BLOCKWIDTH, scrheight//BLOCKWIDTH, BLOCKWIDTH)
        print(noise.get_noisemap_list())

        pygame.display.flip()

main()