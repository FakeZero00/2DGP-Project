from pico2d import load_image
from sdl2 import *
from Project.State_Machine import StateMachine

command = ['IDLE']

#INPUT 이벤트 함수
def left_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a):
        if (command[-1] == 'DOWN'):
            command.append('LEFTDOWN')
        else:
            command.append('LEFT')
        return True
def left_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a):
        if (command[-1] == 'LEFTDOWN'):
            command.append('DOWN')
        else:
            command.append('IDLE')
        return True

def right_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d):
        if (command[-1] == 'DOWN'):
            command.append('RIGHTDOWN')
        else:
            command.append('RIGHT')
        return True
def right_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d):
        if(command[-1] == 'RIGHTDOWN'):
            command.append('DOWN')
        else:
            command.append('IDLE')
        return True

def down_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s):
        if (command[-1] == 'RIGHT'):
            command.append('RIGHTDOWN')
        elif (command[-1] == 'LEFT'):
            command.append('LEFTDOWN')
        else:
            command.append('DOWN')
        return True
def down_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s):
        if(command[-1] == 'RIGHTDOWN'):
            command.append('RIGHT')
        elif(command[-1] == 'LEFTDOWN'):
            command.append('LEFT')
        else:
            command.append('IDLE')
        return True

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
        self.gaogaigar.image.clip_draw(0, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

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
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 400, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

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
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Crouch:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 3

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Crouch_Rightdown:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 3

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Crouch_Leftdown:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 3

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Punch1:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 400 * 2, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

# 가오가이거 클래스 본체
class Gaogaigar:
    def __init__(self):
        self.image = load_image('../Sprite/Move_Sprite(temp_resize).png')
        self.x, self.y = 800, 450
        self.frame = 0

        self.IDLE = Idle(self)
        self.RUN = Run(self)
        self.BACK = Back(self)
        self.CROUCH = Crouch(self)
        self.CROUCH_RIGHTDOWN = Crouch_Rightdown(self)
        self.CROUCH_LEFTDOWN = Crouch_Leftdown(self)
        self.rules = {
            self.IDLE: {right_down: self.RUN, left_down: self.BACK, right_up: self.BACK, left_up: self.RUN, down_down: self.CROUCH},
            self.RUN: {right_up: self.IDLE, left_down: self.IDLE, right_down: self.IDLE, down_down: self.CROUCH_RIGHTDOWN},
            self.BACK: {left_up: self.IDLE, down_down: self.CROUCH_LEFTDOWN},
            self.CROUCH: {down_up: self.IDLE, right_down: self.CROUCH_RIGHTDOWN, left_down: self.CROUCH_LEFTDOWN},
            self.CROUCH_RIGHTDOWN: {down_up: self.RUN, right_up: self.CROUCH},
            self.CROUCH_LEFTDOWN: {down_up: self.BACK, left_up: self.CROUCH}
        }
        self.statemachine = StateMachine(self.IDLE, self.rules)

    def update(self):
        self.statemachine.update()

    def draw(self):
        self.statemachine.draw()

    def handle_event(self, event):
        self.statemachine.handle_state_event(('INPUT', event))