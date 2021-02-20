import sys

from background import *
from constants import *
import time
from input import *
from perlinnoise import *
from player import Player
from block import *


def main():

    # Pygame & screen setup
    pygame.init()
    print("Ca marche askip bis")
    DISPLAY = pygame.display.set_mode(SCREENSIZE, pygame.RESIZABLE)
    pygame.display.set_caption("EscaperOfWater")

    # Game constants & textures
    # Moved to file: constants.py



    # Game variables and classes
    noise = PerlinNoise(SEED, 0, 0, 10, SCRWIDTH // BLOCKWIDTH, SCRHEIGHT // BLOCKWIDTH + 1)
    background = Background(backgroundTexture, 0.6)
    noise.create_noisemap_list()

    # Players
    players = [Player(DISPLAY, 1, 0, 0)]#, Player(DISPLAY, 2, 0, 0)]

    delta = .1

    for i in noise.map:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            elif j == 1:
                print(".", end=" ")
            else:
                print("#", end=" ")
        print()
    print("\n --------------------------------------------- \n")

    while True:
        lastTime = time.time()

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
        noise.print_perlin_noise(DISPLAY, 0, noise.screenpos.y - BLOCKWIDTH, BLOCKWIDTH, tiles)

        delta = time.time() - lastTime

        if len(players) < 1:
            playerposinit = noise.find_empty_xy(BLOCKWIDTH)
            players.append(Player(DISPLAY, len(players)+1, tiles, playerposinit[1], playerposinit[0], scrollspeed))

        for player in players:
            DISPLAY.blit(playerTextures[player.playerNumber - 1], (player.pos.x, player.pos.y))
            player.update(delta, noise.map)  # noise.get_noisemap_list())
        pygame.display.flip()

    pygame.time.delay(16)


main()
