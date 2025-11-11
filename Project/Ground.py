from pico2d import *

class Ground:
    def __init__(self, number):
        if number == 0:
            self.image = load_image('../Sprite/Stone_Ground.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(800, 450)