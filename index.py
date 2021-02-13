import sys, pygame
from vector2 import *
from random import *
pygame.init()

size = width, height = 1100, 700
speed = [2, 2]
black = 0, 0, 0
circlepos = [width/2, height/2]
screen = pygame.display.set_mode(size)

ball = pygame.image.load("redsquare.png")
ballrect = ball.get_rect()
def get_dir():
    return (1* pygame.key.get_pressed()[pygame.K_RIGHT] - 1* pygame.key.get_pressed()[pygame.K_LEFT],
            1* pygame.key.get_pressed()[pygame.K_DOWN]  - 1* pygame.key.get_pressed()[pygame.K_UP])

def randcol():
    return (randint(0,255), randint(0,255), randint(0,255))

def smoothstep(a0, a1, w):
    #return (a1 - a0) * w + a0; # linear interpolation (ugly but optimized)
    return (a1 - a0) * (3.0 - w * 2.0) * w * w + a0 # cubic

def smoothstep2(a0, a1, w):
    # pas de différence notable, utilisez smoothstep() à la place
    # no noticable difference, use smoothstep() instead
    return (a1-a0) * ((w* (w*6.0 - 15.0) + 10.0) * w*w*w) + a0 # smoothest

def randomGrid(ix, iy):
    # Random float. No precomputed gradients mean this works for any number of grid coordinates
    # Readapted from source C code: https://en.wikipedia.org/wiki/Perlin_noise
    random = 2920.0 * sin(ix * 21942.0 + iy * 171324.0 + 8912.0) * cos(ix * 23157.0 * iy * 217832.0 + 9758.0);
    return Vector2(cos(random), sin(random))

def pnoise(x, y):
    #  (x0,y0) - (x1,y0)
    #  |         |
    #  (x0,y1) - (x1,y1)
    x0 = floor(x)
    x1 = x0 + 1
    y0 = floor(y)
    y1 = y0 + 1

    # Compute weights for interpolation for later on
    sx = x-x0
    sy = y-y0

    # Compute dot products of vectors in nearby grids
    v0 = randomGrid(x0, y0)
    d0 = Vector2(x - x0, y - y0)
    dot0 = v0.dot(d0)

    v1 = randomGrid(x1, y0)
    d1 = Vector2(x - x1, y - y0)
    dot1 = v1.dot(d1)

    s0 = smoothstep(dot0, dot1, sx)

    v0 = randomGrid(x0, y1)
    dot0 = v0.x * (x-x0) + v0.y * (y-y1)
    v1 = randomGrid(x1, y1)
    dot1 = v1.x * (x-x1) + v1.y * (y-y1)

    s1 = smoothstep(dot0, dot1, sx)
    val = smoothstep(s0, s1, sy)

    return val

def perlinnoise(display, grid, color, pixw, cellw):
    # old version; do not use
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            col = randcol()
            for ci in range(cellw):
                for cj in range(cellw):
                    dist = Vector2((ci-(cellw/2))/cellw, (cj-(cellw/2))/cellw)
                    dot = dist.dot(grid[i][j])
                    sdot = (dot+1)*255/2
                    pygame.draw.rect(display, (sdot,sdot,sdot),
                                     (i*pixw*cellw + (ci*pixw), j*pixw*cellw + (cj*pixw), pixw, pixw))

def clamp(val, a, b):
    return max(a, min(val, b))

def printpnoise(x, y, w, h, s):
    for i in range(w):
        for j in range(h):
            val = pnoise(i/s, j/s)
            val = val
            val = clamp( (128*(val+1)), 0, 255)
            pygame.draw.rect(DISPLAY, (val, val, val), (i+x, j+y, 1, 1))

DISPLAY = pygame.display.set_mode((width, height), 0, 32)
def main():
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    pygame.init()
    printpnoise(0, 0, 400, 400, 30)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            pass
            if event.type == pygame.QUIT:
                sys.exit()



main()
pique_nique_sa_mère = "oui"
