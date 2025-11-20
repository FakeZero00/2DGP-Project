from pico2d import *
from sdl2 import *

ButtonDict = {
    'Start_Button.png' : 0,
    'Exit_Button.png' : 1
}

class Button:
    def __init__(self, image, width, height, x, y, init_state = 0):
        self.id = ButtonDict[image]
        self.image = load_image('../Sprite/' + image)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.state = init_state

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.state * self.width, 0, self.width, self.height, self.x, self.y, self.width, self.height)

    def handle_event(self, event):
        if self.id == 0:  # Start Button
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.state = 1
                elif event.key == SDLK_RIGHT:
                    self.state = 0
        elif self.id == 1:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.state = 0
                elif event.key == SDLK_RIGHT:
                    self.state = 1

    def handle_collision(self, group, other):
        pass