class Collider:
    def __init__(self, x, y, width, height, object):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.object = object

    def get_bb(self):
        left = self.x
        bottom = self.y
        right = self.x + self.width
        top = self.y + self.height
        return left, bottom, right, top

    def handle_collision(self, group, other):
        self.object.handle_collision(group, other)

    def update_no_collision(self):
        self.object.update_no_collision()