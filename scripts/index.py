import sys, pygame
from vector2 import *
from perlinnoise import *
from player import Player
from random import randint, uniform
from math import sin, cos, floor
from input import *


def main():

    # Pygame & screen setup
    pygame.init()
    screensize = scrwidth, scrheight = 1280, 640
    DISPLAY = pygame.display.set_mode(screensize, pygame.RESIZABLE)
    #pygame.display.set_caption("My Game")

    # Game constants
    BLOCKWIDTH = 32
    BLOCKWIDTH_2TUPLE = (BLOCKWIDTH, BLOCKWIDTH)
    SEED = uniform(-65536, 65535)

    # Textures
    player1Texture = pygame.transform.scale(pygame.image.load("textures/redsquare.png"), (32, 32))
    playerTextures = [player1Texture, player1Texture]
    groundTexture = pygame.transform.scale(pygame.image.load("textures/groundTile.png"), BLOCKWIDTH_2TUPLE)
    groundBGTexture = pygame.transform.scale(pygame.image.load("textures/dummyDecoGround.png"), BLOCKWIDTH_2TUPLE)
    blankTexture = pygame.transform.scale(pygame.image.load("textures/blank.png"), BLOCKWIDTH_2TUPLE)
    tileTextures = [blankTexture, groundBGTexture, groundTexture]

    # Game variables
    noise = PerlinNoise(SEED, 0, 0, 10, scrwidth//BLOCKWIDTH, scrheight//BLOCKWIDTH+1)
    noise.create_noisemap_list()
    #camera = Vector2()
    scrollspeed = 0.5

    # Players init
    players = []
    while True:
        DISPLAY.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Noise scrolling
        # TODO: move to seperate update method
        noise.screenpos.y += scrollspeed

        if noise.screenpos.y > BLOCKWIDTH:
            noise.pos.y -= 1
            noise.screenpos.y %= BLOCKWIDTH
            noise.update_map()
        noise.print_perlin_noise(DISPLAY, 0, noise.screenpos.y-BLOCKWIDTH, BLOCKWIDTH, tileTextures)

        if len(players) == 0:
            playerposinit = noise.find_empty_xy(BLOCKWIDTH)
            players.append(Player(DISPLAY, 1, playerposinit[1], playerposinit[0], scrollspeed))

        for player in players:
            DISPLAY.blit(playerTextures[player.playerNumber - 1], (player.pos.x, player.pos.y))
            player.update(noise.map)#noise.get_noisemap_list())
        pygame.display.flip()

    #pygame.time.delay(16)

main()
