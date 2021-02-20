class BlockType:
    def __init__(self, hardness, breakingTime, texture, collide):
        self.hardness = hardness
        self.breakingTime = breakingTime
        self.texture = texture
        self.collide = collide


class Block:
    def __init__(self, blockType, position):
        self.blockType = blockType
        self.position = position
