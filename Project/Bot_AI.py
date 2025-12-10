from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector
from sdl2 import *
import Global_Object

class Bot_AI:
    def __init__(self, character):
        self.character = character
        self.bt = None

        self.type = None
        self.key = None

        self.build_behavior_tree()

    def update(self):
        self.bt.run()

    def is_look_left(self):
        if self.character.dir[0] == -1: return BehaviorTree.SUCCESS
        else: return BehaviorTree.FAIL

    def input_left(self):
        self.type, self.key = SDL_KEYDOWN, SDLK_LEFT
        return BehaviorTree.SUCCESS

    def input_right(self):
        self.type, self.key = SDL_KEYDOWN, SDLK_RIGHT
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        is_look_left = Condition("왼쪽을 보고 있는가?", self.is_look_left)
        input_left = Action("왼쪽 입력", self.input_left)
        move_left = Sequence("왼쪽 이동", is_look_left, input_left)

        input_right = Action("오른쪽 입력", self.input_right)
        move_left_or_right = Selector("왼쪽 또는 오른쪽 이동", move_left, input_right)

        root = move_left_or_right
        self.bt = BehaviorTree(root)