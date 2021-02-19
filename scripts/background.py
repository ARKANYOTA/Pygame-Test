from vector2 import Vector2

class Background:
    def __init__(self, texture, parallaxMultiplier, x=0, y=0):
        self.texture = texture
        self.parallaxMultiplier = parallaxMultiplier
        self.pos = Vector2(x, y)

    def scroll(self, scrollSpeed):
        self.pos += Vector2(0, scrollSpeed * self.parallaxMultiplier)

    def render(self, display):
        display.blit(self.texture , self.pos.get_tuple())