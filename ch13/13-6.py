import math


class Line(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def __repr__(self):
        return repr(((self.x1, self.y1), (self.x2, self.y2)))

    def __str__(self):
        return str(((self.x1, self.y1), (self.x2, self.y2)))

    def length(self):
        return math.sqrt(pow(self.y2 - self.y1, 2) + pow(self.x2 - self.x1, 2))

    def slope(self):
        if self.y2 == self.y1 or self.x2 == self.x1:
            return None
        return (self.y2 - self.y1) / (self.x2 - self.x1)


l1 = Line(1, 1, 2, 2)
print(l1)
print(l1.length())
print(l1.slope())
