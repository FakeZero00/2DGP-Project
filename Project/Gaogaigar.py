from pico2d import load_image, get_time
from sdl2 import *
from typing import List, Tuple, Optional
from Project.CommandRecognizer import CommandRecognizer
from Project.State_Machine import StateMachine

#커맨드 버퍼 클래스, 인스턴스 생성
class CommandBuffer:
    def __init__(self, BoundTime: float = 1.0):
        self.BoundTime = BoundTime
        self.buffer: List[Tuple[str, float]] = []

    def add(self, token: str, t: Optional[float] = None):
        if t is None:
            t = get_time()
        self.buffer.append((token, t))
        self.pop_old(t)

    def pop_old(self, now: float):
        cutoff = now - self.BoundTime
        self.buffer = [(tok, ts) for tok, ts in self.buffer if ts >= cutoff]

    def tokens(self) -> List[str]:
        return [tok for tok, _ in self.buffer]

    def last_token(self):
        return self.buffer[-1][0] if self.buffer else None

    def clear_last_n(self, n):
        for _ in range(min(n, len(self.buffer))):
            self.buffer.pop()

command_buffer = CommandBuffer()

#커맨드 목록
CommandList = [
    (('DOWN', 'RIGHTDOWN', 'RIGHT', 'ATTACK'), 'PUNCH1')
]
Recognizer = CommandRecognizer(CommandList)

#커맨드, INPUT 이벤트 함수
def cmd_is(name):
    return lambda e, n = name: (e[0] == 'CMD' and e[1] == n)

def left_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a):
        if (command_buffer.last_token() == 'DOWN'):
            command_buffer.add('LEFTDOWN')
        else:
            command_buffer.add('LEFT')
        return True
def left_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a):
        if (command_buffer.last_token() == 'LEFTDOWN'):
            command_buffer.add('DOWN')
        else:
            command_buffer.add('IDLE')
        return True

def right_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d):
        if (command_buffer.last_token() == 'DOWN'):
            command_buffer.add('RIGHTDOWN')
        else:
            command_buffer.add('RIGHT')
        return True
def right_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d):
        if(command_buffer.last_token() == 'RIGHTDOWN'):
            command_buffer.add('DOWN')
        else:
            command_buffer.add('IDLE')
        return True

def down_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s):
        if (command_buffer.last_token() == 'RIGHT'):
            command_buffer.add('RIGHTDOWN')
        elif (command_buffer.last_token() == 'LEFT'):
            command_buffer.add('LEFTDOWN')
        else:
            command_buffer.add('DOWN')
        return True
def down_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s):
        if(command_buffer.last_token() == 'RIGHTDOWN'):
            command_buffer.add('RIGHT')
        elif(command_buffer.last_token() == 'LEFTDOWN'):
            command_buffer.add('LEFT')
        else:
            command_buffer.add('IDLE')
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
        self.gaogaigar.frame = (self.gaogaigar.frame + 1) % 6

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
        cmd_list = Recognizer.match(command_buffer)
        if cmd_list:
            action, used = cmd_list
            command_buffer.clear_last_n(used) # 매칭된 커맨드만큼 버퍼에서 제거
            self.statemachine.handle_state_event(('CMD', action))


    def draw(self):
        self.statemachine.draw()

    def handle_event(self, event):
        self.statemachine.handle_state_event(('INPUT', event))