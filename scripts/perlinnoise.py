from vector2 import *
from random import randint, uniform
from math import sin, cos, floor

def randcol():
    return (randint(0,255), randint(0,255), randint(0,255))

def smoothstep(a0, a1, w):
    #return (a1 - a0) * w + a0; # linear interpolation >> (uglier result but faster)
    return (a1 - a0) * (3.0 - w * 2.0) * w * w + a0 # cubic

def smoothstep2(a0, a1, w):
    # no noticable difference with smoothstep(), only use this if more smoothness is needed
    return (a1-a0) * ((w* (w*6.0 - 15.0) + 10.0) * w*w*w) + a0

def randomGrid(ix, iy):
    # Random float. No precomputed gradients mean this works for any number of grid coordinates
    # Readapted from source C code: https://en.wikipedia.org/wiki/Perlin_noise
    random = 2920.0 * sin(ix * 21942.0 + iy * 171324.0 + 8912.0 + worldseed) * cos(ix * 23157.0 * worldseed * iy * 217832.0 + 9758.0);
    return Vector2(cos(random), sin(random))

def perlin_noise(x, y):
    # Returns perlin noise value for (x, y)

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

def clamp(val, a, b):
    return max(a, min(val, b))

def print_perlin_noise(screen_x, screen_y, noise_x, noise_y, width, height, scale, blockw):
    # width and neight in blocks
    for col in range(width):
        for row in range(height):
            noise = perlin_noise(col/scale + noise_x, row/scale + noise_y)
            noise = (noise + 1) / 2
            if .7 < noise:
                DISPLAY.blit(groundImg, (col * blockw, row * blockw))
            elif .5 < noise:
                pass
            else:
                pass
    return True