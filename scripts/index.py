import sys, pygame
from vector2 import *
from perlinnoise import *
from player import Player
from random import randint, uniform
from math import sin, cos, floor
from time import sleep


def get_dir():
    return Vector2(1 * pygame.key.get_pressed()[pygame.K_RIGHT] - 1 * pygame.key.get_pressed()[pygame.K_LEFT],
                   1 * pygame.key.get_pressed()[pygame.K_DOWN] - 1 * pygame.key.get_pressed()[pygame.K_UP])


def randcol():
    return randint(0, 255), randint(0, 255), randint(0, 255)


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
    player1Texture = pygame.transform.scale(pygame.image.load("../textures/redsquare.png"), (32, 32))
    player2Texture = pygame.image.load("../textures/intro_ball.gif")
    playerTextures = [player1Texture, player2Texture]

    # Game constants
    BLOCKWIDTH = 32
    SEED = uniform(-65536, 65535)

    # Game variables
    map = [[0 for k in range(scrwidth)] for i in range(scrheight)]
    noise = PerlinNoise(SEED, 0, 0, 10)
    groundMovement = 0
    noiseposy = 0
    scale = 10

    # Players init
    players = []

    noise.print_perlin_noise(DISPLAY, 0, 0, scrwidth // BLOCKWIDTH, scrheight // BLOCKWIDTH, BLOCKWIDTH)
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if groundMovement == 250:
            groundMovement = 0
            noise.y -= 1
        else:
            groundMovement += 1
        noise.print_perlin_noise(DISPLAY, 0, 0, scrwidth // BLOCKWIDTH, scrheight // BLOCKWIDTH, BLOCKWIDTH)

        if len(players) == 0:
            players.append(Player(1, pygame, DISPLAY))
            players[0].init()

        for player in players:
            DISPLAY.blit(playerTextures[player.playerNumber - 1], (player.getX(), player.getY()))
            player.update()
        pygame.display.flip()


main()
