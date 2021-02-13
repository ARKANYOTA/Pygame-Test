from math import *
class Vector2:
    def __init__(self, x=0, y=0):
        self.xy = self.x, self.y = x, y
    def __add__(self, v):
        return Vector2(self.x + v.x, self.y + v.y)
    def __iadd__(self, other):
        return self + other
    def __sub__(self, v):
        return Vector2(self.x - v.x, self.y - v.y)
    def __isub__(self, other):
        return self - other
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    def __mul__(self, a):
        return Vector2(self.x * a, self.y * a)
    def __imul__(self, a):
        return self * a
    def __truediv__(self, a):
        return Vector2(self.x / a, self.y / a)
    def __itruediv__(self, a):
        return self / a
    def __floordiv__(self, a):
        return Vector2(self.x // a, self.y // a)
    def __ifloordiv__(self, a):
        return self // a
    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
    def __len__(self):
        return norm(self)

    def norm(self):
        return sqrt(self.x * self.x + self.y * self.y)
    def normalized(self):
        return self / self.norm()
    def normsq(self):
        return self.x * self.x + self.y * self.y
    def dot(self, v):
        return self.x * v.x + self.y * v.y
