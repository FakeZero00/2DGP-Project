from pico2d import *
from Project.CommandRecognizer import CommandBuffer, CommandRecognizer
from Project.State_Machine import StateMachine
from Project.Collider import Collider
import Project.P1_Event_Function as P1
import Project.P2_Event_Function as P2
import Game_Framework, Global_Object

#커맨드 목록
LeftCommandList = [
    (('DOWN', 'RIGHTDOWN', 'RIGHT', 'ATTACK'), 'COMMAND_SKILL'),
    (('DOWN', 'RIGHTDOWN', 'RIGHT', 'IDLE', 'ATTACK'), 'COMMAND_SKILL')
]
LeftRecognizer = CommandRecognizer(LeftCommandList)

RightCommandList = [
    (('DOWN', 'LEFTDOWN', 'LEFT', 'ATTACK'), 'COMMAND_SKILL'),
    (('DOWN', 'LEFTDOWN', 'LEFT', 'IDLE', 'ATTACK'), 'COMMAND_SKILL')
]
RightRecognizer = CommandRecognizer(RightCommandList)

#커맨드, INPUT 등 이벤트 함수
def cmd_is(name):
    if name == 'COMMAND_SKILL':
        return cmdskill_start

def cmdskill_start(e, object_state):
    return e[0] == 'CMD' and e[1] == 'COMMAND_SKILL'

#기준 프레임
TIME_PER_ACTION = 0.6
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

#이동 속도
RUN_SPEED_PPS = 1000
DROP_SPEED_PPS = 100
ATTACK_MOVE_SPEED_PPS = 200

# 상태 클래스들
class Idle:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 4

    def exit(self, e):
        pass

    def do(self, e):
        pass

    def draw(self):
        if self.gundam.jump_bool:
            self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 40 * self.gundam.dir[0], self.gundam.y - 80, 450, 450)
        else:
            self.gundam.image.clip_composite_draw(0, 0, 700, 700, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y - 30, 400, 400)

class Run:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        if not self.gundam.jump_bool:
            self.gundam.frame = (self.gundam.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time) % 10

        self.gundam.x += RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gundam.get_collider('body').get_bb()[2] > 1600:
            self.gundam.x = 1600

    def draw(self):
        if self.gundam.dir[0] == 1:
            if self.gundam.jump_bool:
                self.gundam.image.clip_composite_draw(2 * 800, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 80 * self.gundam.dir[0], self.gundam.y, 450, 450)
            else:
                self.gundam.image.clip_composite_draw(int(self.gundam.frame) * 800, 800, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 80 * self.gundam.dir[0], self.gundam.y, 450, 450)
        elif self.gundam.dir[0] == -1:
            self.gundam.image.clip_composite_draw(800, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)


class Back:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        if self.gundam.dir[0] == 1:
            self.gundam.frame = 1
        elif self.gundam.dir[0] == -1:
            self.gundam.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        if not self.gundam.jump_bool and self.gundam.dir[0] == -1:
            self.gundam.frame = (self.gundam.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time) % 10
        elif self.gundam.dir[0] == 1:
            self.gundam.frame = 1

        self.gundam.x -= RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gundam.get_collider('body').get_bb()[0] < 0:
            self.gundam.x = 0

    def draw(self):
        if self.gundam.dir[0] == 1:
            self.gundam.image.clip_composite_draw(self.gundam.frame * 800, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)
        elif self.gundam.dir[0] == -1:
            if self.gundam.jump_bool:
                self.gundam.image.clip_composite_draw(2 * 800, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 80 * self.gundam.dir[0], self.gundam.y, 450, 450)
            else:
                self.gundam.image.clip_composite_draw(int(self.gundam.frame) * 800, 800, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 80 * self.gundam.dir[0], self.gundam.y, 450, 450)

class Crouch:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 3

    def exit(self, e):
        pass

    def do(self, e):
        pass

    def draw(self):
        self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)

class Crouch_Rightdown:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 3

    def exit(self, e):
        pass

    def do(self, e):
        pass

    def draw(self):
        self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)

class Crouch_Leftdown:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 3

    def exit(self, e):
        pass

    def do(self, e):
        pass

    def draw(self):
        self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)

class Jump:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 4
        if not self.gundam.jump_bool:
            self.gundam.jump_bool = True
            self.gundam.jump_frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        pass

    def draw(self):
        self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 40 * self.gundam.dir[0], self.gundam.y - 80, 450, 450)

class Jump_Leftup:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 1
        if not self.gundam.jump_bool:
            self.gundam.jump_bool = True
            self.gundam.jump_frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        self.gundam.x -= RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gundam.get_collider('body').get_bb()[0] < 0:
            self.gundam.x = 0

    def draw(self):
        if self.gundam.dir[0] == 1:
            self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)
        elif self.gundam.dir[0] == -1:
            self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)

class Jump_Rightup:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 2
        if not self.gundam.jump_bool:
            self.gundam.jump_bool = True
            self.gundam.jump_frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        self.gundam.x += RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gundam.get_collider('body').get_bb()[2] > 1600:
            self.gundam.x = 1600

    def draw(self):
        if self.gundam.dir[0] == 1:
            self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)
        elif self.gundam.dir[0] == -1:
            self.gundam.image.clip_composite_draw(self.gundam.frame * 820, 0, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)

class Attack1:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 0
        self.gundam.cooltime_bool = False

    def exit(self, e):
        pass

    def do(self, e):
        if self.gundam.player == 'p1':
            P1.input_check(e, self.gundam.input_booleans)
        elif self.gundam.player == 'p2':
            P2.input_check(e, self.gundam.input_booleans)

        self.gundam.frame = self.gundam.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gundam.frame) > 4:
            self.gundam.statemachine.handle_state_event(('ANIM_END', 0), self.gundam.object_state)
        elif int(self.gundam.frame) >= 3:
            self.gundam.cooltime_bool = True

        if self.gundam.y <= 250:
            self.gundam.x += ATTACK_MOVE_SPEED_PPS * Game_Framework.frame_time * self.gundam.dir[0]
        if self.gundam.get_collider('body').get_bb()[0] < 0:
            self.gundam.x = 0
        elif self.gundam.get_collider('body').get_bb()[2] > 1600:
            self.gundam.x = 1600

    def draw(self):
        if int(self.gundam.frame) == 3 or int(self.gundam.frame) == 4:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 850, 800 * 2, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 170 * self.gundam.dir[0], self.gundam.y, 450, 450)
        else:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 800, 800 * 2, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)

class Attack2:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 0
        self.gundam.cooltime_bool = False

    def exit(self, e):
        pass

    def do(self, e):
        if self.gundam.player == 'p1':
            P1.input_check(e, self.gundam.input_booleans)
        elif self.gundam.player == 'p2':
            P2.input_check(e, self.gundam.input_booleans)

        self.gundam.frame = self.gundam.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gundam.frame) > 5:
            self.gundam.statemachine.handle_state_event(('ANIM_END', 0), self.gundam.object_state)
        elif int(self.gundam.frame) >= 3:
            self.gundam.cooltime_bool = True

        if self.gundam.y <= 250:
            self.gundam.x += ATTACK_MOVE_SPEED_PPS * Game_Framework.frame_time * self.gundam.dir[0]
        if self.gundam.get_collider('body').get_bb()[0] < 0:
            self.gundam.x = 0
        elif self.gundam.get_collider('body').get_bb()[2] > 1600:
            self.gundam.x = 1600

    def draw(self):
        if int(self.gundam.frame) == 0:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 800, 830 * 3, 800, 760, 0, self.gundam.dir[1], self.gundam.x + 120 * self.gundam.dir[0], self.gundam.y - 20, 400, 400)
        elif int(self.gundam.frame) == 2:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 800, 800 * 3, 830, 800, 0, self.gundam.dir[1], self.gundam.x + 120 * self.gundam.dir[0], self.gundam.y - 20, 500, 400)
        elif int(self.gundam.frame) == 3:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 830, 800 * 3, 700, 800, 0, self.gundam.dir[1], self.gundam.x + 120 * self.gundam.dir[0], self.gundam.y - 20, 400, 400)
        elif int(self.gundam.frame) >= 4:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 800, 800 * 3, 1000, 800, 0, self.gundam.dir[1], self.gundam.x - 120 * self.gundam.dir[0], self.gundam.y, 600, 400)
        else:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 800, 800 * 3, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 120 * self.gundam.dir[0], self.gundam.y, 400, 400)

class Attack3:
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        if self.gundam.player == 'p1':
            P1.input_check(e, self.gundam.input_booleans)
        elif self.gundam.player == 'p2':
            P2.input_check(e, self.gundam.input_booleans)

        self.gundam.frame = self.gundam.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gundam.frame) > 5:
            self.gundam.statemachine.handle_state_event(('ANIM_END', 0), self.gundam.object_state)

        if self.gundam.y <= 250:
            self.gundam.x += ATTACK_MOVE_SPEED_PPS * Game_Framework.frame_time * self.gundam.dir[0]
        if self.gundam.get_collider('body').get_bb()[0] < 0:
            self.gundam.x = 0
        elif self.gundam.get_collider('body').get_bb()[2] > 1600:
            self.gundam.x = 1600

    def draw(self):
        if int(self.gundam.frame) == 1:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 3) * 800, 800 * 4, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 170 * self.gundam.dir[0], self.gundam.y, 450, 450)
        elif int(self.gundam.frame) == 2:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 3) * 800, 800 * 4, 880, 800, 0, self.gundam.dir[1], self.gundam.x + 130 * self.gundam.dir[0], self.gundam.y + 20, 500, 450)
        elif int(self.gundam.frame) >= 3:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 3) * 840, 800 * 4, 880, 800, 0, self.gundam.dir[1], self.gundam.x + 200 * self.gundam.dir[0], self.gundam.y + 20, 500, 450)
        else:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 3) * 800, 800 * 4, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)

class Command_skill: # Test
    def __init__(self, gundam):
        self.gundam = gundam

    def enter(self, e):
        self.gundam.frame = 0

    def exit(self, e):
        self.gundam.cooltime_bool = True

    def do(self, e):
        if self.gundam.player == 'p1':
            P1.input_check(e, self.gundam.input_booleans)
        elif self.gundam.player == 'p2':
            P2.input_check(e, self.gundam.input_booleans)

        self.gundam.frame = self.gundam.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gundam.frame) > 100:
            self.gundam.statemachine.handle_state_event(('ANIM_END', 0), self.gundam.object_state)

    def draw(self):
        if int(self.gundam.frame) == 3 or int(self.gundam.frame) >= 4:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 850, 800 * 2, 800, 800, 0, self.gundam.dir[1], self.gundam.x + 70 * self.gundam.dir[0], self.gundam.y, 450, 450)
        else:
            self.gundam.image.clip_composite_draw(min(int(self.gundam.frame), 4) * 800, 800 * 2, 800, 800, 0, self.gundam.dir[1], self.gundam.x, self.gundam.y, 450, 450)

# 건담 클래스 본체
class Gundam:
    def __init__(self, player, x = 1300, y = 250):
        self.image = load_image('../Sprite/Gundam_Sprite.png')
        self.x, self.y = x, y
        self.dir = [-1, 'h']
        self.frame = 0
        self.cur_input_event = None
        self.cooltime_bool = True
        self.jump_bool = False
        self.jump_frame = 0
        #점프 높이 테이블 (프레임별 y 오프셋)
        self.jump_table = [0, 20, 50, 90, 140, 200, 270, 300, 330, 350, 380, 400, 400, 400, 400, 400, 400, 380, 350, 330, 300, 270, 200, 140, 90, 50, 20, 0]
        self.other = None

        #객체 상태 초기화
        self.player = player
        if self.player == 'p1':
            self.input_booleans = {input_key: False for input_key in ['w', 'a', 's', 'd']}
        elif self.player == 'p2':
            self.input_booleans = {input_key: False for input_key in ['UP', 'LEFT', 'DOWN', 'RIGHT']}
        self.command_buffer = CommandBuffer()
        self.object_state = (self.command_buffer, self.input_booleans, self.cooltime_bool, self.jump_bool)

        # 콜라이더 생성
        self.colliders = {}
        # 몸 콜라이더
        if self.dir[0] == 1:
            self.colliders['body'] = Collider(self.x, self.y - 225, 150, 365, self)
        elif self.dir[0] == -1:
            self.colliders['body'] = Collider(self.x - 150, self.y - 225, 150, 365, self)

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

        self.P1rules = {
            self.IDLE: {P1.right_down: self.RUN, P1.left_down: self.BACK, P1.right_up: self.BACK, P1.left_up: self.RUN, P1.down_down: self.CROUCH, P1.up_down: self.JUMP, P1.up_up: self.IDLE,
                        cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL, P1.attack_down: self.ATTACK1},
            self.RUN: {P1.right_up: self.IDLE, P1.left_down: self.IDLE, P1.right_down: self.IDLE, P1.down_down: self.CROUCH_RIGHTDOWN, P1.up_down: self.JUMP_RIGHTUP,
                       P1.attack_down: self.ATTACK1},
            self.BACK: {P1.left_up: self.IDLE, P1.right_down: self.IDLE, P1.down_down: self.CROUCH_LEFTDOWN, P1.up_down: self.JUMP_LEFTUP},
            self.CROUCH: {P1.down_up: self.IDLE, P1.right_down: self.CROUCH_RIGHTDOWN, P1.left_down: self.CROUCH_LEFTDOWN},
            self.CROUCH_RIGHTDOWN: {P1.down_up: self.RUN, P1.right_up: self.CROUCH},
            self.CROUCH_LEFTDOWN: {P1.down_up: self.BACK, P1.left_up: self.CROUCH},
            self.JUMP: {P1.up_up: self.IDLE, P1.left_down: self.JUMP_LEFTUP, P1.right_down: self.JUMP_RIGHTUP},
            self.JUMP_LEFTUP: {P1.up_up: self.BACK, P1.left_up: self.IDLE},
            self.JUMP_RIGHTUP: {P1.up_up: self.RUN, P1.right_up: self.IDLE},
            self.ATTACK1: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN, P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE,
                           P1.attack_down: self.ATTACK2, cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL},
            self.ATTACK2: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN, P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE,
                           P1.attack_down: self.ATTACK3},
            self.ATTACK3: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN, P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE},
            self.COMMAND_SKILL: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN, P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE}
        }
        self.P2rules = {
            self.IDLE: {P2.right_down: self.RUN, P2.left_down: self.BACK, P2.right_up: self.BACK, P2.left_up: self.RUN,
                        P2.down_down: self.CROUCH, P2.up_down: self.JUMP, P2.up_up: self.IDLE,
                        cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL, P2.attack_down: self.ATTACK1},
            self.RUN: {P2.right_up: self.IDLE, P2.left_down: self.IDLE, P2.right_down: self.IDLE,
                       P2.down_down: self.CROUCH_RIGHTDOWN, P2.up_down: self.JUMP_RIGHTUP,
                       P2.attack_down: self.ATTACK1},
            self.BACK: {P2.left_up: self.IDLE, P2.right_down: self.IDLE, P2.down_down: self.CROUCH_LEFTDOWN,
                        P2.up_down: self.JUMP_LEFTUP},
            self.CROUCH: {P2.down_up: self.IDLE, P2.right_down: self.CROUCH_RIGHTDOWN,
                          P2.left_down: self.CROUCH_LEFTDOWN},
            self.CROUCH_RIGHTDOWN: {P2.down_up: self.RUN, P2.right_up: self.CROUCH},
            self.CROUCH_LEFTDOWN: {P2.down_up: self.BACK, P2.left_up: self.CROUCH},
            self.JUMP: {P2.up_up: self.IDLE, P2.left_down: self.JUMP_LEFTUP, P2.right_down: self.JUMP_RIGHTUP},
            self.JUMP_LEFTUP: {P2.up_up: self.BACK, P2.left_up: self.IDLE},
            self.JUMP_RIGHTUP: {P2.up_up: self.RUN, P2.right_up: self.IDLE},
            self.ATTACK1: {P2.anim_end('BACK'): self.BACK, P2.anim_end('RUN'): self.RUN,
                           P2.anim_end('CROUCH'): self.CROUCH, P2.anim_end('IDLE'): self.IDLE,
                           P2.attack_down: self.ATTACK2, cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL},
            self.ATTACK2: {P2.anim_end('BACK'): self.BACK, P2.anim_end('RUN'): self.RUN,
                           P2.anim_end('CROUCH'): self.CROUCH, P2.anim_end('IDLE'): self.IDLE,
                           P2.attack_down: self.ATTACK3},
            self.ATTACK3: {P2.anim_end('BACK'): self.BACK, P2.anim_end('RUN'): self.RUN,
                           P2.anim_end('CROUCH'): self.CROUCH, P2.anim_end('IDLE'): self.IDLE},
            self.COMMAND_SKILL: {P2.anim_end('BACK'): self.BACK, P2.anim_end('RUN'): self.RUN,
                                 P2.anim_end('CROUCH'): self.CROUCH, P2.anim_end('IDLE'): self.IDLE}
        }
        if self.player == 'p1':
            self.statemachine = StateMachine(self.IDLE, self.P1rules)
        if self.player == 'p2':
            self.statemachine = StateMachine(self.IDLE, self.P2rules)
        self.behavior_state = self.statemachine.cur_state

    def update(self):
        #객체 상태 업데이트
        self.object_state = (self.command_buffer, self.input_booleans, self.cooltime_bool, self.jump_bool)
        self.behavior_state = self.statemachine.cur_state
        if self.player == 'p1':
            self.other = Global_Object.p2
        elif self.player == 'p2':
            self.other = Global_Object.p1
        if self.x > self.other.x:
            self.dir[0] = -1
            self.dir[1] = 'h'
        elif self.x < self.other.x:
            self.dir[0] = 1
            self.dir[1] = ''

        # 콜라이더 위치 업데이트
        for name, collider in self.colliders.items():
            if self.dir[0] == 1:
                collider.x = self.x
            elif self.dir[0] == -1:
                collider.x = self.x - 150
            collider.y = self.y - 225

        #점프 프레임 테이블 적용
        if self.jump_bool:
            self.jump_frame += 20 * ACTION_PER_TIME * Game_Framework.frame_time
            if int(self.jump_frame) < len(self.jump_table):
                self.y = 250 + self.jump_table[int(self.jump_frame)]
            else:
                self.jump_bool = False
                self.y = 250

        # 현재 입력 이벤트로 상태 머신 업데이트
        self.statemachine.update(('INPUT', self.cur_input_event))
        cmd_list =  None
        if self.dir[0] == 1:
            cmd_list = LeftRecognizer.match(self.command_buffer)
        elif self.dir[0] == -1:
            cmd_list = RightRecognizer.match(self.command_buffer)
        if cmd_list:
            action, used = cmd_list
            self.command_buffer.clear_last_n(used) # 매칭된 커맨드만큼 버퍼에서 제거
            print(f'커맨드 인식: {action}')
            self.statemachine.handle_state_event(('CMD', action), self.object_state)


    def draw(self):
        self.statemachine.draw()
        draw_rectangle(*self.get_collider('body').get_bb())

    def handle_event(self, event):
        self.statemachine.handle_state_event(('INPUT', event), self.object_state)
        self.cur_input_event = event

    def get_collider(self, name):
        return self.colliders[name]

    def handle_collision(self, group, other):
        if group == 'p1_body:p2_body':
            if other.object.behavior_state == other.object.IDLE:
                self.x -= RUN_SPEED_PPS * Game_Framework.frame_time * self.dir[0]
            elif self.behavior_state == self.RUN and other.object.behavior_state == other.object.RUN:
                self.x -= RUN_SPEED_PPS * Game_Framework.frame_time * self.dir[0]
            elif self.behavior_state == self.RUN and other.object.behavior_state == other.object.BACK:
                self.x -= RUN_SPEED_PPS * Game_Framework.frame_time * self.dir[0]
            elif self.behavior_state == self.BACK and other.object.behavior_state == other.object.RUN:
                self.x -= RUN_SPEED_PPS * Game_Framework.frame_time * self.dir[0]
            elif self.behavior_state == self.BACK and other.object.behavior_state == other.object.BACK:
                self.x -= RUN_SPEED_PPS * Game_Framework.frame_time * self.dir[0]