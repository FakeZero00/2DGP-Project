from pico2d import load_image, draw_rectangle
from Project.CommandRecognizer import CommandBuffer, CommandRecognizer
from Project.State_Machine import StateMachine
from Project.Event_Function import *
import Game_Framework

#커맨드 버퍼
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

def cmdskill_start(e, object_state):
    return e[0] == 'CMD' and e[1] == 'COMMAND_SKILL'

#기준 프레임
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

#이동 속도
RUN_SPEED_PPS = 1000
DROP_SPEED_PPS = 100

# 상태 클래스들
class Idle:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 4

    def exit(self, e):
        pass

    def do(self, e):
        pass

    def draw(self):
        if self.gaogaigar.jump_bool:
            self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)
        else:
            self.gaogaigar.image.clip_draw(0, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Run:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        if not self.gaogaigar.jump_bool:
            self.gaogaigar.frame = (self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time) % 10

        self.gaogaigar.x += RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gaogaigar.x + 225 > 1600:
            self.gaogaigar.x = 1600 - 225

    def draw(self):
        if self.gaogaigar.jump_bool:
            self.gaogaigar.image.clip_draw(2 * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)
        else:
            self.gaogaigar.image.clip_draw(int(self.gaogaigar.frame) * 400, 400, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Back:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 1

    def exit(self, e):
        pass

    def do(self, e):
        self.gaogaigar.x -= RUN_SPEED_PPS * Game_Framework.frame_time
        if(self.gaogaigar.x - 225 < 0):
            self.gaogaigar.x = 225

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

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
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

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
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

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
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Jump:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 4
        if not self.gaogaigar.jump_bool:
            self.gaogaigar.jump_bool = True
            self.gaogaigar.yv = 10

    def exit(self, e):
        pass

    def do(self, e):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Jump_Leftup:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 1
        if not self.gaogaigar.jump_bool:
            self.gaogaigar.jump_bool = True
            self.gaogaigar.yv = 10

    def exit(self, e):
        pass

    def do(self, e):
        self.gaogaigar.x -= RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gaogaigar.x + 225 > 1600:
            self.gaogaigar.x = 1600 - 225

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Jump_Rightup:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 2
        if not self.gaogaigar.jump_bool:
            self.gaogaigar.jump_bool = True
            self.gaogaigar.yv = 10

    def exit(self, e):
        pass

    def do(self, e):
        self.gaogaigar.x += RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gaogaigar.x + 225 > 1600:
            self.gaogaigar.x = 1600 - 225

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Attack1:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0
        self.gaogaigar.cooltime_bool = False

    def exit(self, e):
        pass

    def do(self, e):
        input_check(e, input_booleans)
        self.gaogaigar.frame = self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gaogaigar.frame) > 7:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)
        elif int(self.gaogaigar.frame) >= 4:
            self.gaogaigar.cooltime_bool = True


    def draw(self):
        self.gaogaigar.image.clip_draw(min(int(self.gaogaigar.frame), 5) * 400, 400 * 2, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Attack2:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0
        self.gaogaigar.cooltime_bool = False

    def exit(self, e):
        pass

    def do(self, e):
        input_check(e, input_booleans)
        self.gaogaigar.frame = self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gaogaigar.frame) > 6:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)
        elif int(self.gaogaigar.frame) >= 3:
            self.gaogaigar.cooltime_bool = True

    def draw(self):
        self.gaogaigar.image.clip_draw(min(int(self.gaogaigar.frame), 4) * 400, 400 * 3, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Attack3:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        input_check(e, input_booleans)
        self.gaogaigar.frame = self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gaogaigar.frame) > 8:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)

    def draw(self):
        self.gaogaigar.image.clip_draw(min(int(self.gaogaigar.frame), 5) * 400, 400 * 4, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Command_skill: # Test
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        input_check(e, input_booleans)
        self.gaogaigar.frame = self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gaogaigar.frame) > 100:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)

    def draw(self):
        self.gaogaigar.image.clip_draw(min(int(self.gaogaigar.frame), 5) * 400, 400 * 2, 400, 400, self.gaogaigar.x, self.gaogaigar.y, 450, 450)

# 가오가이거 클래스 본체
class Gaogaigar:
    def __init__(self):
        self.image = load_image('../Sprite/Move_Sprite(temp_resize).png')
        self.x, self.y = 300, 250
        self.yv = 0
        self.frame = 0
        self.cur_input_event = None
        self.cooltime_bool = True
        self.jump_bool = False
        self.object_state = (command_buffer, input_booleans, self.cooltime_bool, self.jump_bool)

        self.IDLE = Idle(self)
        self.RUN = Run(self)
        self.BACK = Back(self)
        self.CROUCH = Crouch(self)
        self.CROUCH_RIGHTDOWN = Crouch_Rightdown(self)
        self.CROUCH_LEFTDOWN = Crouch_Leftdown(self)
        self.JUMP = Jump(self)
        self.JUMP_LEFTUP = Jump_Leftup(self)
        self.JUMP_RIGHTUP = Jump_Rightup(self)
        self.ATTACK1 = Attack1(self)
        self.ATTACK2 = Attack2(self)
        self.ATTACK3 = Attack3(self)
        self.COMMAND_SKILL = Command_skill(self)
        self.rules = {
            self.IDLE: {right_down: self.RUN, left_down: self.BACK, right_up: self.BACK, left_up: self.RUN, down_down: self.CROUCH, up_down: self.JUMP, up_up: self.IDLE,
                        cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL, attack_down: self.ATTACK1},
            self.RUN: {right_up: self.IDLE, left_down: self.IDLE, right_down: self.IDLE, down_down: self.CROUCH_RIGHTDOWN, up_down: self.JUMP_RIGHTUP,
                       attack_down: self.ATTACK1},
            self.BACK: {left_up: self.IDLE, right_down: self.IDLE, down_down: self.CROUCH_LEFTDOWN, up_down: self.JUMP_LEFTUP},
            self.CROUCH: {down_up: self.IDLE, right_down: self.CROUCH_RIGHTDOWN, left_down: self.CROUCH_LEFTDOWN},
            self.CROUCH_RIGHTDOWN: {down_up: self.RUN, right_up: self.CROUCH},
            self.CROUCH_LEFTDOWN: {down_up: self.BACK, left_up: self.CROUCH},
            self.JUMP: {up_up: self.IDLE, left_down: self.JUMP_LEFTUP, right_down: self.JUMP_RIGHTUP},
            self.JUMP_LEFTUP: {up_up: self.BACK, left_up: self.IDLE},
            self.JUMP_RIGHTUP: {up_up: self.RUN, right_up: self.IDLE},
            self.ATTACK1: {anim_end('BACK'): self.BACK, anim_end('RUN'): self.RUN, anim_end('CROUCH'): self.CROUCH, anim_end('IDLE'): self.IDLE,
                           attack_down: self.ATTACK2, cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL},
            self.ATTACK2: {anim_end('BACK'): self.BACK, anim_end('RUN'): self.RUN, anim_end('CROUCH'): self.CROUCH, anim_end('IDLE'): self.IDLE,
                           attack_down: self.ATTACK3},
            self.ATTACK3: {anim_end('BACK'): self.BACK, anim_end('RUN'): self.RUN, anim_end('CROUCH'): self.CROUCH, anim_end('IDLE'): self.IDLE},
            self.COMMAND_SKILL: {anim_end('BACK'): self.BACK, anim_end('RUN'): self.RUN, anim_end('CROUCH'): self.CROUCH, anim_end('IDLE'): self.IDLE}
        }
        self.statemachine = StateMachine(self.IDLE, self.rules)

    def update(self):
        #객체 상태 업데이트
        self.object_state = (command_buffer, input_booleans, self.cooltime_bool, self.jump_bool)

        #중력 적용
        if self.yv != 0:
            self.yv +=  Game_Framework.GRAVITY * Game_Framework.frame_time
            self.y += DROP_SPEED_PPS * self.yv * Game_Framework.frame_time

        # 현재 입력 이벤트로 상태 머신 업데이트
        self.statemachine.update(('INPUT', self.cur_input_event))
        cmd_list = Recognizer.match(command_buffer)
        if cmd_list:
            action, used = cmd_list
            command_buffer.clear_last_n(used) # 매칭된 커맨드만큼 버퍼에서 제거
            print(f'커맨드 인식: {action}')
            self.statemachine.handle_state_event(('CMD', action), self.object_state)


    def draw(self):
        self.statemachine.draw()
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        self.statemachine.handle_state_event(('INPUT', event), self.object_state)
        self.cur_input_event = event

    def get_bb(self):
        return self.x - 225, self.y - 225, self.x + 225, self.y + 225

    def handle_collision(self, group, other):
        if group == 'gaogaigar:ground':
            self.y = 250
            self.yv = 0
            self.jump_bool = False