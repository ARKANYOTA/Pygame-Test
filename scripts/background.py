from vector2 import Vector2
from constants import SCRHEIGHT

class Background:
    def __init__(self, texture, parallaxMultiplier, x=0, y=0):
        self.texture = texture
        self.textureSize = Vector2(1280, 2000)
        self.parallaxMultiplier = parallaxMultiplier
        self.pos = Vector2(x, y)

    def scroll(self, scrollSpeed):
        self.pos += Vector2(0, scrollSpeed * self.parallaxMultiplier)
        #if self.pos.y > self

    def render(self, display):
        display.blit(self.texture , (0, self.pos.y))
        if self.pos.y > 0:
            display.blit(self.texture, (0, self.pos.y - self.textureSize.y))
