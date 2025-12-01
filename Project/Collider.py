class Collider:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_bb(self):
        left = self.x
        bottom = self.y
        right = self.x + self.width
        top = self.y + self.height
        return left, bottom, right, top