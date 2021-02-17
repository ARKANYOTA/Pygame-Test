import sys, pygame
from vector2 import *
from perlinnoise import *
from player import Player
from random import randint, uniform
from math import sin, cos, floor
from time import sleep

def randcol():
    return randint(0, 255), randint(0, 255), randint(0, 255)

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
    player1Texture = pygame.transform.scale(pygame.image.load(r"../textures/redsquare.png"), (32, 32))
    player2Texture = pygame.image.load(r"../textures/intro_ball.gif")
    playerTextures = [player1Texture, player2Texture]

    # Game constants
    BLOCKWIDTH = 32
    SEED = uniform(-65536, 65535)

    # Game variables
    noise = PerlinNoise(SEED, 0, 0, 10, scrwidth//BLOCKWIDTH, scrheight//BLOCKWIDTH+1)
    camera = Vector2()
    scrollspeed = 3

    # Players init
    players = []

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass

        screen.fill((0,0,0))
        # Noise scrolling
        noise.screenpos.y += scrollspeed
        if noise.screenpos.y > BLOCKWIDTH:
            noise.pos.y -= 1
            noise.screenpos.y %= BLOCKWIDTH
            noise.update_map()
        noise.print_perlin_noise(DISPLAY, 0, noise.screenpos.y-BLOCKWIDTH, scrwidth//BLOCKWIDTH, scrheight//BLOCKWIDTH, BLOCKWIDTH)

        if len(players) == 0:
            players.append(Player(DISPLAY, 1, 0, 0))
            players[0].init()

        for player in players:
            DISPLAY.blit(playerTextures[player.playerNumber - 1], (player.getX(), player.getY()))
            player.update()#noise.get_noisemap_list())
        pygame.display.flip()

    pygame.time.delay(0.0166)

main()
