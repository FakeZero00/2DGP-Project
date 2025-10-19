from pico2d import load_image
from sdl2 import *
from Project.State_Machine import StateMachine


#INPUT 이벤트 함수
def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a
def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a
def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d
def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


# 상태 클래스들
class Idle:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(0, 400, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Run:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self):
        self.gaogaigar.frame = (self.gaogaigar.frame + 1) % 10
        self.gaogaigar.x += 50

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Back:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 1

    def exit(self, e):
        pass

    def do(self):
        self.gaogaigar.x -= 50

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 400, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

# 가오가이거 클래스 본체
class Gaogaigar:
    def __init__(self):
        self.image = load_image('../Sprite/Move_Sprite(temp_resize).png')
        self.x, self.y = 800, 450
        self.frame = 0

        self.IDLE = Idle(self)
        self.RUN = Run(self)
        self.BACK = Back(self)
        self.rules = {
            self.IDLE: {right_down: self.RUN, left_down: self.BACK},
            self.RUN: {right_up: self.IDLE},
            self.BACK: {left_up: self.IDLE}
        }
        self.statemachine = StateMachine(self.IDLE, self.rules)

    def update(self):
        self.statemachine.update()

    def draw(self):
        self.statemachine.draw()

    def handle_event(self, event):
        self.statemachine.handle_state_event(('INPUT', event))