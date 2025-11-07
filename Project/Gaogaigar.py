from pico2d import load_image, get_time
from sdl2 import *
from Project.CommandRecognizer import CommandBuffer, CommandRecognizer
from Project.State_Machine import StateMachine



command_buffer = CommandBuffer()

#커맨드 목록
CommandList = [
    (('DOWN', 'RIGHTDOWN', 'RIGHT', 'ATTACK'), 'COMMAND_SKILL'),
    (('DOWN', 'RIGHTDOWN', 'RIGHT', 'IDLE', 'ATTACK'), 'COMMAND_SKILL')
]
Recognizer = CommandRecognizer(CommandList)

#커맨드, INPUT 등 이벤트 함수
input_booleans = {input_key : False for input_key in ['w', 'a', 's', 'd']}
def cmd_is(name):
    if name == 'COMMAND_SKILL':
        return cmdskill_start

def cmdskill_start(e):
    return e[0] == 'CMD' and e[1] == 'COMMAND_SKILL'

def anim_end(behavior):
    if behavior == 'RUN': return anim_end_to_run
    elif behavior == 'BACK': return anim_end_to_back
    elif behavior == 'CROUCH': return anim_end_to_crouch
    elif behavior == 'IDLE': return anim_end_to_idle

def anim_end_to_run(e):
    return e[0] == 'ANIM_END' and input_booleans['d'] == True
def anim_end_to_back(e):
    return e[0] == 'ANIM_END' and input_booleans['a'] == True
def anim_end_to_crouch(e):
    return e[0] == 'ANIM_END' and input_booleans['s'] == True
def anim_end_to_idle(e):
    return e[0] == 'ANIM_END' and input_booleans['a'] == False and input_booleans['d'] == False and input_booleans['s'] == False

def input_check(e):
    if(e[0] == 'INPUT'):
        if(e[1].type == SDL_KEYDOWN):
            if e[1].key == SDLK_w:
                input_booleans['w'] = True
            elif e[1].key == SDLK_a:
                input_booleans['a'] = True
            elif e[1].key == SDLK_s:
                input_booleans['s'] = True
            elif e[1].key == SDLK_d:
                input_booleans['d'] = True
        elif(e[1].type == SDL_KEYUP):
            if e[1].key == SDLK_w:
                input_booleans['w'] = False
            elif e[1].key == SDLK_a:
                input_booleans['a'] = False
            elif e[1].key == SDLK_s:
                input_booleans['s'] = False
            elif e[1].key == SDLK_d:
                input_booleans['d'] = False

def left_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a and input_booleans['a'] == False):
        if (command_buffer.last_token() == 'DOWN'):
            command_buffer.add('LEFTDOWN')
        else:
            command_buffer.add('LEFT')
        input_booleans['a'] = True
        return True
def left_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a and input_booleans['a'] == True):
        if (command_buffer.last_token() == 'LEFTDOWN'):
            command_buffer.add('DOWN')
        else:
            command_buffer.add('IDLE')
        input_booleans['a'] = False
        return True

def right_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d and input_booleans['d'] == False):
        if (command_buffer.last_token() == 'DOWN'):
            command_buffer.add('RIGHTDOWN')
        else:
            command_buffer.add('RIGHT')
        input_booleans['d'] = True
        return True
def right_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d and input_booleans['d'] == True):
        if(command_buffer.last_token() == 'RIGHTDOWN'):
            command_buffer.add('DOWN')
        else:
            command_buffer.add('IDLE')
        input_booleans['d'] = False
        return True

def down_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s and input_booleans['s'] == False):
        if (command_buffer.last_token() == 'RIGHT'):
            command_buffer.add('RIGHTDOWN')
        elif (command_buffer.last_token() == 'LEFT'):
            command_buffer.add('LEFTDOWN')
        else:
            command_buffer.add('DOWN')
        input_booleans['s'] = True
        return True
def down_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s and input_booleans['s'] == True):
        if(command_buffer.last_token() == 'RIGHTDOWN'):
            command_buffer.add('RIGHT')
        elif(command_buffer.last_token() == 'LEFTDOWN'):
            command_buffer.add('LEFT')
        else:
            command_buffer.add('IDLE')
        input_booleans['s'] = False
        return True

def attack_down(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j):
        command_buffer.add('ATTACK')
        return True
def attack_up(e):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j):
        return True

# 상태 클래스들
class Idle:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self, e):
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

    def do(self, e):
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

    def do(self, e):
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

    def do(self, e):
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

    def do(self, e):
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

    def do(self, e):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Attack1:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        input_check(e)
        self.gaogaigar.frame += 1
        if self.gaogaigar.frame > 7:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0))

    def draw(self):
        self.gaogaigar.image.clip_draw(min(self.gaogaigar.frame, 5) * 400, 400 * 2, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Attack2:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        input_check(e)
        self.gaogaigar.frame += 1
        if self.gaogaigar.frame > 6:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0))

    def draw(self):
        self.gaogaigar.image.clip_draw(min(self.gaogaigar.frame, 4) * 400, 400 * 3, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Attack3:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        input_check(e)
        self.gaogaigar.frame += 1
        if self.gaogaigar.frame > 7:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0))

    def draw(self):
        self.gaogaigar.image.clip_draw(min(self.gaogaigar.frame, 5) * 400, 400 * 4, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Command_skill: # Test
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        input_check(e)
        self.gaogaigar.frame += 1
        if self.gaogaigar.frame > 100:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0))

    def draw(self):
        self.gaogaigar.image.clip_draw(min(self.gaogaigar.frame, 5) * 400, 400 * 2, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

# 가오가이거 클래스 본체
class Gaogaigar:
    def __init__(self):
        self.image = load_image('../Sprite/Move_Sprite(temp_resize).png')
        self.x, self.y = 800, 450
        self.frame = 0
        self.cur_input_event = None

        self.IDLE = Idle(self)
        self.RUN = Run(self)
        self.BACK = Back(self)
        self.CROUCH = Crouch(self)
        self.CROUCH_RIGHTDOWN = Crouch_Rightdown(self)
        self.CROUCH_LEFTDOWN = Crouch_Leftdown(self)
        self.ATTACK1 = Attack1(self)
        self.ATTACK2 = Attack2(self)
        self.ATTACK3 = Attack3(self)
        self.COMMAND_SKILL = Command_skill(self)
        self.rules = {
            self.IDLE: {right_down: self.RUN, left_down: self.BACK, right_up: self.BACK, left_up: self.RUN, down_down: self.CROUCH,
                        cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL, attack_down: self.ATTACK1},
            self.RUN: {right_up: self.IDLE, left_down: self.IDLE, right_down: self.IDLE, down_down: self.CROUCH_RIGHTDOWN,
                       attack_down: self.ATTACK1},
            self.BACK: {left_up: self.IDLE, right_down: self.IDLE, down_down: self.CROUCH_LEFTDOWN},
            self.CROUCH: {down_up: self.IDLE, right_down: self.CROUCH_RIGHTDOWN, left_down: self.CROUCH_LEFTDOWN},
            self.CROUCH_RIGHTDOWN: {down_up: self.RUN, right_up: self.CROUCH},
            self.CROUCH_LEFTDOWN: {down_up: self.BACK, left_up: self.CROUCH},
            self.ATTACK1: {anim_end('BACK'): self.BACK, anim_end('RUN'): self.RUN, anim_end('CROUCH'): self.CROUCH, anim_end('IDLE'): self.IDLE,  attack_down: self.ATTACK2, cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL},
            self.ATTACK2: {anim_end('BACK'): self.BACK, anim_end('RUN'): self.RUN, anim_end('CROUCH'): self.CROUCH, anim_end('IDLE'): self.IDLE, attack_down: self.ATTACK3},
            self.ATTACK3: {anim_end('BACK'): self.BACK, anim_end('RUN'): self.RUN, anim_end('CROUCH'): self.CROUCH, anim_end('IDLE'): self.IDLE},
            self.COMMAND_SKILL: {anim_end('BACK'): self.BACK, anim_end('RUN'): self.RUN, anim_end('CROUCH'): self.CROUCH, anim_end('IDLE'): self.IDLE}
        }
        self.statemachine = StateMachine(self.IDLE, self.rules)

    def update(self):
        self.statemachine.update(('INPUT', self.cur_input_event))
        cmd_list = Recognizer.match(command_buffer)
        if cmd_list:
            action, used = cmd_list
            command_buffer.clear_last_n(used) # 매칭된 커맨드만큼 버퍼에서 제거
            print(f'커맨드 인식: {action}')
            self.statemachine.handle_state_event(('CMD', action))


    def draw(self):
        self.statemachine.draw()

    def handle_event(self, event):
        self.statemachine.handle_state_event(('INPUT', event))
        self.cur_input_event = event