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
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

#이동 속도
RUN_SPEED_PPS = 1000
DROP_SPEED_PPS = 100
ATTACK_MOVE_SPEED_PPS = 200

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
            self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)
        else:
            self.gaogaigar.image.clip_composite_draw(0, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

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
        if self.gaogaigar.get_collider('body').get_bb()[2] > 1600:
            self.gaogaigar.x = 1600 - 40

    def draw(self):
        if self.gaogaigar.dir[0] == 1:
            if self.gaogaigar.jump_bool:
                self.gaogaigar.image.clip_composite_draw(2 * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)
            else:
                self.gaogaigar.image.clip_composite_draw(int(self.gaogaigar.frame) * 800, 800, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)
        elif self.gaogaigar.dir[0] == -1:
            self.gaogaigar.image.clip_composite_draw(800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Back:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        if self.gaogaigar.dir[0] == 1:
            self.gaogaigar.frame = 1
        elif self.gaogaigar.dir[0] == -1:
            self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        if not self.gaogaigar.jump_bool and self.gaogaigar.dir[0] == -1:
            self.gaogaigar.frame = (self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time) % 10
        elif self.gaogaigar.dir[0] == 1:
            self.gaogaigar.frame = 1

        self.gaogaigar.x -= RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gaogaigar.get_collider('body').get_bb()[0] < 0:
            self.gaogaigar.x = 40

    def draw(self):
        if self.gaogaigar.dir[0] == 1:
            self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)
        elif self.gaogaigar.dir[0] == -1:
            if self.gaogaigar.jump_bool:
                self.gaogaigar.image.clip_composite_draw(2 * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)
            else:
                self.gaogaigar.image.clip_composite_draw(int(self.gaogaigar.frame) * 800, 800, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

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
        self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

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
        self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

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
        self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Jump:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 4
        if not self.gaogaigar.jump_bool:
            self.gaogaigar.jump_bool = True
            self.gaogaigar.jump_frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        pass

    def draw(self):
        self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Jump_Leftup:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 1
        if not self.gaogaigar.jump_bool:
            self.gaogaigar.jump_bool = True
            self.gaogaigar.jump_frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        self.gaogaigar.x -= RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gaogaigar.get_collider('body').get_bb()[0] < 0:
            self.gaogaigar.x = 40

    def draw(self):
        if self.gaogaigar.dir[0] == 1:
            self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)
        elif self.gaogaigar.dir[0] == -1:
            self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Jump_Rightup:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 2
        if not self.gaogaigar.jump_bool:
            self.gaogaigar.jump_bool = True
            self.gaogaigar.jump_frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        self.gaogaigar.x += RUN_SPEED_PPS * Game_Framework.frame_time
        if self.gaogaigar.get_collider('body').get_bb()[2] > 1600:
            self.gaogaigar.x = 1600 - 40

    def draw(self):
        if self.gaogaigar.dir[0] == 1:
            self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)
        elif self.gaogaigar.dir[0] == -1:
            self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Hit:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar
        self.timer = 0

    def enter(self, e):
        self.gaogaigar.frame = 5
        self.timer = 0

    def exit(self, e):
        pass

    def do(self, e):
        if self.gaogaigar.player == 'p1':
            P1.input_check(e, self.gaogaigar.input_booleans)
        elif self.gaogaigar.player == 'p2':
            P2.input_check(e, self.gaogaigar.input_booleans)

        if self.timer >= 0.1:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)
        self.timer += Game_Framework.frame_time

    def draw(self):
        self.gaogaigar.image.clip_composite_draw(self.gaogaigar.frame * 800, 0, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Attack1:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0
        self.gaogaigar.cooltime_bool = False

    def exit(self, e):
        pass

    def do(self, e):
        if self.gaogaigar.player == 'p1':
            P1.input_check(e, self.gaogaigar.input_booleans)
        elif self.gaogaigar.player == 'p2':
            P2.input_check(e, self.gaogaigar.input_booleans)

        self.gaogaigar.frame = self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gaogaigar.frame) > 7:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)
        elif int(self.gaogaigar.frame) >= 4:
            self.gaogaigar.cooltime_bool = True

        if self.gaogaigar.y <= 250:
            self.gaogaigar.x += ATTACK_MOVE_SPEED_PPS * Game_Framework.frame_time * self.gaogaigar.dir[0]
        if self.gaogaigar.get_collider('body').get_bb()[2] > 1600:
            self.gaogaigar.x = 1600 - 40
        elif self.gaogaigar.get_collider('body').get_bb()[0] < 0:
            self.gaogaigar.x = 40

    def draw(self):
        self.gaogaigar.image.clip_composite_draw(min(int(self.gaogaigar.frame), 5) * 800, 800 * 2, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Attack2:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0
        self.gaogaigar.cooltime_bool = False

    def exit(self, e):
        pass

    def do(self, e):
        if self.gaogaigar.player == 'p1':
            P1.input_check(e, self.gaogaigar.input_booleans)
        elif self.gaogaigar.player == 'p2':
            P2.input_check(e, self.gaogaigar.input_booleans)

        self.gaogaigar.frame = self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gaogaigar.frame) > 6:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)
        elif int(self.gaogaigar.frame) >= 3:
            self.gaogaigar.cooltime_bool = True

        if self.gaogaigar.y <= 250:
            self.gaogaigar.x += ATTACK_MOVE_SPEED_PPS * Game_Framework.frame_time * self.gaogaigar.dir[0]
        if self.gaogaigar.get_collider('body').get_bb()[2] > 1600:
            self.gaogaigar.x = 1600 - 40
        elif self.gaogaigar.get_collider('body').get_bb()[0] < 0:
            self.gaogaigar.x = 40

    def draw(self):
        self.gaogaigar.image.clip_composite_draw(min(int(self.gaogaigar.frame), 4) * 800, 800 * 3, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Attack3:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        pass

    def do(self, e):
        if self.gaogaigar.player == 'p1':
            P1.input_check(e, self.gaogaigar.input_booleans)
        elif self.gaogaigar.player == 'p2':
            P2.input_check(e, self.gaogaigar.input_booleans)

        self.gaogaigar.frame = self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gaogaigar.frame) > 8:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)

        if self.gaogaigar.y <= 250:
            self.gaogaigar.x += ATTACK_MOVE_SPEED_PPS * Game_Framework.frame_time * self.gaogaigar.dir[0]
        if self.gaogaigar.get_collider('body').get_bb()[2] > 1600:
            self.gaogaigar.x = 1600 - 40
        elif self.gaogaigar.get_collider('body').get_bb()[0] < 0:
            self.gaogaigar.x = 40

    def draw(self):
        self.gaogaigar.image.clip_composite_draw(min(int(self.gaogaigar.frame), 5) * 800, 800 * 4, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

class Command_skill: # Test
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self, e):
        self.gaogaigar.frame = 0

    def exit(self, e):
        self.gaogaigar.cooltime_bool = True

    def do(self, e):
        if self.gaogaigar.player == 'p1':
            P1.input_check(e, self.gaogaigar.input_booleans)
        elif self.gaogaigar.player == 'p2':
            P2.input_check(e, self.gaogaigar.input_booleans)

        self.gaogaigar.frame = self.gaogaigar.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time
        if int(self.gaogaigar.frame) > 100:
            self.gaogaigar.statemachine.handle_state_event(('ANIM_END', 0), self.gaogaigar.object_state)

    def draw(self):
        self.gaogaigar.image.clip_composite_draw(min(int(self.gaogaigar.frame), 5) * 800, 800 * 2, 800, 800, 0, self.gaogaigar.dir[1], self.gaogaigar.x, self.gaogaigar.y, 450, 450)

# 가오가이거 클래스 본체
class Gaogaigar:
    def __init__(self, player, x = 300, y = 250):
        self.image = load_image('../Sprite/Gaogaigar_Sprite.png')
        self.x, self.y = x, y
        self.dir = [1, '']
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

        #콜라이더 생성
        self.colliders = {}
        #몸 콜라이더
        if self.dir[0] == 1:
            self.colliders['body'] = Collider(self.x - 40, self.y - 225, 160, 365, self)
        elif self.dir[0] == -1:
            self.colliders['body'] = Collider(self.x - 120, self.y - 225, 160, 365, self)
        #공격 콜라이더
        if self.dir[0] == 1:
            self.colliders['attack'] = Collider(self.x + 80, self.y - 40, 100, 120, self)
        elif self.dir[0] == -1:
            self.colliders['attack'] = Collider(self.x - 180, self.y - 40, 100, 120, self)

        self.IDLE = Idle(self)
        self.RUN = Run(self)
        self.BACK = Back(self)
        self.CROUCH = Crouch(self)
        self.CROUCH_RIGHTDOWN = Crouch_Rightdown(self)
        self.CROUCH_LEFTDOWN = Crouch_Leftdown(self)
        self.JUMP = Jump(self)
        self.JUMP_LEFTUP = Jump_Leftup(self)
        self.JUMP_RIGHTUP = Jump_Rightup(self)
        self.HIT = Hit(self)
        self.ATTACK1 = Attack1(self)
        self.ATTACK2 = Attack2(self)
        self.ATTACK3 = Attack3(self)
        self.COMMAND_SKILL = Command_skill(self)

        self.P1rules = {
            self.IDLE: {P1.right_down: self.RUN, P1.left_down: self.BACK, P1.right_up: self.BACK, P1.left_up: self.RUN,
                        P1.down_down: self.CROUCH, P1.up_down: self.JUMP, P1.up_up: self.IDLE,
                        cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL, P1.attack_down: self.ATTACK1},
            self.RUN: {P1.right_up: self.IDLE, P1.left_down: self.IDLE, P1.right_down: self.IDLE,
                       P1.down_down: self.CROUCH_RIGHTDOWN, P1.up_down: self.JUMP_RIGHTUP,
                       P1.attack_down: self.ATTACK1},
            self.BACK: {P1.left_up: self.IDLE, P1.right_down: self.IDLE, P1.down_down: self.CROUCH_LEFTDOWN,
                        P1.up_down: self.JUMP_LEFTUP},
            self.CROUCH: {P1.down_up: self.IDLE, P1.right_down: self.CROUCH_RIGHTDOWN,
                          P1.left_down: self.CROUCH_LEFTDOWN},
            self.CROUCH_RIGHTDOWN: {P1.down_up: self.RUN, P1.right_up: self.CROUCH},
            self.CROUCH_LEFTDOWN: {P1.down_up: self.BACK, P1.left_up: self.CROUCH},
            self.JUMP: {P1.up_up: self.IDLE, P1.left_down: self.JUMP_LEFTUP, P1.right_down: self.JUMP_RIGHTUP},
            self.JUMP_LEFTUP: {P1.up_up: self.BACK, P1.left_up: self.IDLE},
            self.JUMP_RIGHTUP: {P1.up_up: self.RUN, P1.right_up: self.IDLE},
            self.HIT: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN,
                        P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE},
            self.ATTACK1: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN,
                           P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE,
                           P1.attack_down: self.ATTACK2, cmd_is('COMMAND_SKILL'): self.COMMAND_SKILL},
            self.ATTACK2: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN,
                           P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE,
                           P1.attack_down: self.ATTACK3},
            self.ATTACK3: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN,
                           P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE},
            self.COMMAND_SKILL: {P1.anim_end('BACK'): self.BACK, P1.anim_end('RUN'): self.RUN,
                                 P1.anim_end('CROUCH'): self.CROUCH, P1.anim_end('IDLE'): self.IDLE}
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
            self.HIT: {P2.anim_end('BACK'): self.BACK, P2.anim_end('RUN'): self.RUN,
                       P2.anim_end('CROUCH'): self.CROUCH, P2.anim_end('IDLE'): self.IDLE},
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

        #콜라이더 위치 업데이트
        for name, collider in self.colliders.items():
            if name == 'body':
                if self.dir[0] == 1:
                    collider.x = self.x - 40
                elif self.dir[0] == -1:
                    collider.x = self.x - 120
                collider.y = self.y - 225
            elif name == 'attack':
                if self.dir[0] == 1:
                    collider.x = self.x + 80
                elif self.dir[0] == -1:
                    collider.x = self.x - 180
                collider.y = self.y - 40

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
        cmd_list = None
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
        draw_rectangle(*self.get_collider('attack').get_bb())

    def handle_event(self, event):
        self.statemachine.handle_state_event(('INPUT', event), self.object_state)
        self.cur_input_event = event

    def get_collider(self, name):
        return self.colliders[name]

    def handle_collision(self, group, other):
        if group == 'p1_body:p2_body':
            if not self.behavior_state == self.IDLE:
                self.x -= RUN_SPEED_PPS * Game_Framework.frame_time * self.dir[0]
            if self.get_collider('body').get_bb()[1] >= other.get_bb()[3] - 20:
                if self.get_collider('body').x + self.get_collider('body').width // 2 <= other.x + other.width // 2:
                    self.x = other.object.get_collider('body').get_bb()[0] - 120
                else:
                    self.x = other.object.get_collider('body').get_bb()[2] + 120
        elif group == 'p1_body:p2_attack':
            if other.object.behavior_state in [other.object.ATTACK1, other.object.ATTACK2, other.object.ATTACK3, other.object.COMMAND_SKILL] and other.object.frame >= 2:
                self.statemachine.handle_state_event(('HIT', self.HIT), self.object_state)