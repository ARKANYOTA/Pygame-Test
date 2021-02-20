import sys

from background import *
from constants import *
from input import *
from perlinnoise import *
from player import Player
from block import *


def main():

    # Pygame & screen setup
    pygame.init()
    print("Ca marche askip bis")
    DISPLAY = pygame.display.set_mode(SCREENSIZE, pygame.RESIZABLE)
    pygame.display.set_caption("ChawserofGold")

    # Game constants
    # Moved to file: constants.py

    # Textures
    player1Texture = pygame.transform.scale(pygame.image.load("../textures/redsquare.png"), (32, 32))
    playerTextures = [player1Texture, player1Texture]
    groundTexture = pygame.transform.scale(pygame.image.load("../textures/groundTile.png"), BLOCKWIDTH_2TUPLE)
    mineralTexture = pygame.transform.scale(pygame.image.load("../textures/redsquare.png"), BLOCKWIDTH_2TUPLE)
    groundBGTexture = pygame.transform.scale(pygame.image.load("../textures/dummyDecoGround.png"), BLOCKWIDTH_2TUPLE)
    blankTexture = pygame.transform.scale(pygame.image.load("../textures/blank.png"), BLOCKWIDTH_2TUPLE)

    backgroundTexture = pygame.transform.scale(pygame.image.load("../textures/background_cave.png"), (SCRWIDTH, 2000))

    # Game variables and classes
    noise = PerlinNoise(SEED, 0, 0, 10, SCRWIDTH // BLOCKWIDTH, SCRHEIGHT // BLOCKWIDTH + 1)
    background = Background(backgroundTexture, 0.6)
    scrollspeed = 1
    noise.create_noisemap_list()

    tiles = [
        BlockType(0, 0, blankTexture, False),
        BlockType(0, 0, groundBGTexture, False),
        BlockType(0, 100, groundTexture, True),
        BlockType(1, 500, mineralTexture, True)
    ]

    # Players init
    players = []
    while True:
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
        # TODO: move to separate update method
        noise.screenpos.y += scrollspeed
        background.scroll(scrollspeed)
        background.render(DISPLAY)

        if noise.screenpos.y > BLOCKWIDTH:
            noise.pos.y -= 1
            noise.screenpos.y %= BLOCKWIDTH
            noise.update_map()
        noise.print_perlin_noise(DISPLAY, 0, noise.screenpos.y - BLOCKWIDTH, BLOCKWIDTH, tiles)

        if len(players) == 0:
            playerposinit = noise.find_empty_xy(BLOCKWIDTH)
            players.append(Player(DISPLAY, 1, tiles, playerposinit[1], playerposinit[0], scrollspeed))

        for player in players:
            DISPLAY.blit(playerTextures[player.playerNumber - 1], (player.pos.x, player.pos.y))
            player.update(noise.map)  # noise.get_noisemap_list())
        pygame.display.flip()

    pygame.time.delay(16)


main()
