import sys, pygame
from vector2 import *
from perlinnoise import *
from player import Player
from random import randint, uniform
from math import sin, cos, floor
from input import *
from background import *
from constants import *
import time

def main():

    # Pygame & screen setup
    pygame.init()
    print("Ca marche askip bis")
    DISPLAY = pygame.display.set_mode(SCREENSIZE, pygame.RESIZABLE)
    pygame.display.set_caption("EscaperOfWater")

    # Game constants
    # Moved to file: constants.py

    # Textures
    player1Texture = pygame.transform.scale(pygame.image.load("../textures/redsquare.png"), (32, 32))
    playerTextures = [player1Texture, player1Texture]
    groundTexture = pygame.transform.scale(pygame.image.load("../textures/groundTile.png"), BLOCKWIDTH_2TUPLE)
    groundBGTexture = pygame.transform.scale(pygame.image.load("../textures/dummyDecoGround.png"), BLOCKWIDTH_2TUPLE)
    blankTexture = pygame.transform.scale(pygame.image.load("../textures/blank.png"), BLOCKWIDTH_2TUPLE)
    tileTextures = [blankTexture, groundBGTexture, groundTexture]

    backgroundTexture = pygame.transform.scale(pygame.image.load("../textures/background_cave.png"), (SCRWIDTH, 2000))

    # Game variables and classes
    noise = PerlinNoise(SEED, 0, 0, 10, SCRWIDTH//BLOCKWIDTH, SCRHEIGHT//BLOCKWIDTH+1)
    background = Background(backgroundTexture, 0.6)
    noise.create_noisemap_list()

    # Players
    players = [Player(DISPLAY, 1, 0, 0), Player(DISPLAY, 2, 0, 0)]

    delta = .1
    while True:
        lastTime = time.time()
        print(delta)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        DISPLAY.fill(BACKGROUNDCOLOR)

        # Noise scrolling
        # TODO: move to seperate update method
        # background.scroll(scrollspeed)
        # background.render(DISPLAY)

        #noise.screenpos.y += scrollspeed * delta
        if noise.screenpos.y > BLOCKWIDTH:
            noise.pos.y -= 1
            noise.screenpos.y %= BLOCKWIDTH
            noise.update_map()
        noise.print_perlin_noise(DISPLAY, 0, noise.screenpos.y-BLOCKWIDTH, BLOCKWIDTH, tileTextures)

        for player in players:
            DISPLAY.blit(playerTextures[player.playerNumber - 1], (player.pos.x, player.pos.y))
            player.update(delta, noise.map)#noise.get_noisemap_list())
        pygame.display.flip()

        delta = time.time() - lastTime



main()
