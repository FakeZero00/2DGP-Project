from pico2d import *

class Background:
    def __init__(self, number):
        if number == 0:
            self.image = load_image('Sprite/Space_Background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(800, 450)