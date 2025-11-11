from pico2d import *

class Ground:
    def __init__(self, number):
        if number == 0:
            self.image = load_image('../Sprite/Stone_Ground.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(800, 450)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 1600, 25

    def handle_collision(self, group, other):
        pass