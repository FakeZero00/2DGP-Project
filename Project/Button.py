from pico2d import *
from sdl2 import *
import Global_Object

ButtonDict = {
    'Start_Button.png' : 0,
    'Exit_Button.png' : 1,
    'Gaogaigar.jpg' : 2,
    'Gundam.jpg' : 3,
    'Training_Button.png' : 4
}

class Button:
    select_sfx = None

    def __init__(self, image, width, height, x, y, init_state = 0):
        self.id = ButtonDict[image]
        self.image = load_image('../Sprite/' + image)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.state = init_state

        if Button.select_sfx is None:
            Button.select_sfx = load_wav('../Sound/Button_Select.wav')
            Button.select_sfx.set_volume(10)

    def update(self):
        pass

    def draw(self):
        if self.id == 2:
            self.image.clip_draw(self.state * self.width, 0, self.width, self.height, self.x, self.y, self.width // 2 , self.height // 2)
        else:
            self.image.clip_draw(self.state * self.width, 0, self.width, self.height, self.x, self.y, self.width, self.height)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key in [SDLK_LEFT, SDLK_RIGHT]:
                Button.select_sfx.play()
        if self.id == 0:  # Start Button
            if Global_Object.Current_mode_number == 0:
                self.state = 1
            else:
                self.state = 0
        elif self.id == 1:
            if Global_Object.Current_mode_number == 2:
                self.state = 1
            else:
                self.state = 0
        if self.id == 2:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.state = 0
                elif event.key == SDLK_RIGHT:
                    self.state = 1
        elif self.id == 3:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.state = 1
                elif event.key == SDLK_RIGHT:
                    self.state = 0
        elif self.id == 4:
            if Global_Object.Current_mode_number == 1:
                self.state = 1
            else:
                self.state = 0

    def handle_collision(self, group, other):
        pass