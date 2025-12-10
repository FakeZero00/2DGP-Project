from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector
from sdl2 import *
from random import randint
import Global_Object, Game_Framework

class Bot_AI:
    def __init__(self, character):
        self.character = character
        self.bt = None
        self.idle = False
        self.idle_timer = 0

        self.type = None
        self.key = None

        self.build_behavior_tree()

    def update(self):
        if self.idle:
            self.idle_timer -= Game_Framework.frame_time
            if self.idle_timer <= 0.0:
                self.idle = False
                self.idle_timer = 0.0
        self.bt.run()

    def is_look_left(self):
        if self.character.dir[0] == -1: return BehaviorTree.SUCCESS
        else: return BehaviorTree.FAIL

    def input_left(self):
        if self.type == SDL_KEYDOWN and self.key == SDLK_RIGHT:
            self.type = SDL_KEYUP
        elif self.type == SDL_KEYDOWN and self.key == SDLK_LEFT and self.character.behavior_state == self.character.IDLE:
            self.type = SDL_KEYUP
        else:
            self.type, self.key = SDL_KEYDOWN, SDLK_LEFT
        return BehaviorTree.SUCCESS

    def input_right(self):
        if self.type == SDL_KEYDOWN and self.key == SDLK_LEFT:
            self.type = SDL_KEYUP
        elif self.type == SDL_KEYDOWN and self.key == SDLK_RIGHT and self.character.behavior_state == self.character.IDLE:
            self.type = SDL_KEYUP
        else:
            self.type, self.key = SDL_KEYDOWN, SDLK_RIGHT
        return BehaviorTree.SUCCESS

    def is_not_range(self):
        if self.character.collider_state is None:
            return BehaviorTree.SUCCESS
        else: return BehaviorTree.FAIL

    def check_idle_timer(self):
        if self.idle and self.idle_timer > 0.0:
            return BehaviorTree.SUCCESS
        else: return BehaviorTree.FAIL

    def random_Condition(self, probability):
        rand_value = randint(1, 100)
        if rand_value <= probability:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def input_clear(self):
        if self.type == SDL_KEYDOWN:
            self.type = SDL_KEYUP
        self.idle = True
        self.idle_timer = 1.0
        return BehaviorTree.SUCCESS

    def is_other_being_attack(self):
        if Global_Object.p1.behavior_state in [Global_Object.p1.ATTACK1, Global_Object.p1.ATTACK2, Global_Object.p1.ATTACK3]:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_pull_pp_full(self):
        if Global_Object.p2pp.current_point == Global_Object.p2pp.Max:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def input_finisher(self):
        self.type, self.key = SDL_KEYDOWN, SDLK_KP_5
        return BehaviorTree.SUCCESS

    def input_attack(self):
        self.type, self.key = SDL_KEYDOWN, SDLK_KP_4
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        is_look_left = Condition("왼쪽을 보고 있는가?", self.is_look_left)
        input_left = Action("왼쪽 입력", self.input_left)
        move_left = Sequence("왼쪽 이동", is_look_left, input_left)

        input_right = Action("오른쪽 입력", self.input_right)
        move_left_or_right = Selector("왼쪽 또는 오른쪽 이동", move_left, input_right)

        is_not_range = Condition("적이 사정거리 밖에 있는가?", self.is_not_range)
        move = Sequence("이동", is_not_range, move_left_or_right)

        move_right = Sequence("오른쪽 이동", is_look_left, input_right)
        move_right_or_left_for_defend = Selector("오른쪽 또는 왼쪽 이동", move_right, input_left)

        is_other_being_attack = Condition("상대가 공격 중인가?", self.is_other_being_attack)
        defend = Sequence("방어", is_other_being_attack, move_right_or_left_for_defend)

        is_pp_full = Condition("PP가 가득 찼는가?", self.is_pull_pp_full)
        input_finisher = Action("필살기 입력", self.input_finisher)
        finisher = Sequence("필살기", is_pp_full, input_finisher)

        input_attack = Action("공격 입력", self.input_attack)
        finisher_or_attack = Selector("필살기 또는 공격", finisher, input_attack)
        attack_or_defend = Selector("공격 또는 방어", finisher_or_attack, defend)

        behavior = Selector("행동", move, attack_or_defend)

        check_timer = Condition("대기 시간 체크", self.check_idle_timer)
        idle_state = Sequence("대기 상태", check_timer)

        random_Condition_1 = Condition("1% 확률", self.random_Condition, 1)
        input_clear = Action("입력 해제", self.input_clear)
        idle_set = Sequence("대기 설정", random_Condition_1, input_clear)

        idle_or_behavior = Selector("대기 또는 행동", idle_state, idle_set, behavior)

        root = idle_or_behavior
        self.bt = BehaviorTree(root)