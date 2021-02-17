import pygame
from vector2 import *

def get_input_arrows():
    left = pygame.key.get_pressed()[pygame.K_LEFT]
    up = pygame.key.get_pressed()[pygame.K_UP]
    down = pygame.key.get_pressed()[pygame.K_DOWN]
    right = pygame.key.get_pressed()[pygame.K_RIGHT]
    return Vector2(right - left, down - up)

def get_input_wasd():
    left  = pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_q]
    up    = pygame.key.get_pressed()[pygame.K_z] or pygame.key.get_pressed()[pygame.K_w]
    down  = pygame.key.get_pressed()[pygame.K_s]
    right = pygame.key.get_pressed()[pygame.K_d]
    return Vector2(right - left, down - up)