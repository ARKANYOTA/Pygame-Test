import pygame
from vector2 import Vector2
from random import uniform
from block import *

SCREENSIZE = SCRWIDTH, SCRHEIGHT = 1280, 640
BLOCKWIDTH = 32
BLOCKWIDTH_2TUPLE = (BLOCKWIDTH, BLOCKWIDTH)
SEED = uniform(-65536, 65535)
BACKGROUNDCOLOR = (0x19, 0x14, 0x0a)
scrollspeed = 30

# Textures
player1Texture = pygame.transform.scale(pygame.image.load("../textures/redsquare.png"), (32, 32))
playerTextures = [player1Texture, player1Texture]
groundTexture = pygame.transform.scale(pygame.image.load("../textures/groundTile.png"), BLOCKWIDTH_2TUPLE)
mineralTexture = pygame.transform.scale(pygame.image.load("../textures/redsquare.png"), BLOCKWIDTH_2TUPLE)
groundBGTexture = pygame.transform.scale(pygame.image.load("../textures/dummyDecoGround.png"), BLOCKWIDTH_2TUPLE)
blankTexture = pygame.transform.scale(pygame.image.load("../textures/blank.png"), BLOCKWIDTH_2TUPLE)
backgroundTexture = pygame.transform.scale(pygame.image.load("../textures/background_cave.png"), (SCRWIDTH, 2000))

tiles = [
        BlockType(0, 0, blankTexture, False),
        BlockType(0, 0, groundBGTexture, False),
        BlockType(0, 100, groundTexture, True),
        BlockType(1, 500, mineralTexture, True)
    ]