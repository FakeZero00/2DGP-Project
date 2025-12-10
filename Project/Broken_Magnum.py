from pico2d import *
from Collider import Collider
import Game_Framework, PlayScene_world

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

RUN_SPEED_PPS = 1500

class Broken_Magnum:
    def __init__(self, x, y, parent_object):
        self.image = load_image('Sprite/Broken_Magnum.png')
        self.x = x
        self.y = y
        self.count = 0
        self.frame = 0
        self.parent_object = parent_object
        self.dir = self.parent_object.dir[0]

        self.timer = 0.0
        self.state = 'launch'

        self.colliders = {}
        self.colliders['broken_magnum'] = Collider(self.x - 50, self.y - 40, 120, 80, self)
        self.collider_state = None

    def update(self):
        if self.state == 'hit':
            self.timer += Game_Framework.frame_time
            if self.timer >= 0.5:
                self.state = 'launch'
        self.frame = (self.frame + 10 * ACTION_PER_TIME * Game_Framework.frame_time) % 10
        self.x = self.x + RUN_SPEED_PPS * Game_Framework.frame_time * self.dir
        self.colliders['broken_magnum'].x = self.x - 50

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 800, 0, 800, 800, 0, '', self.x, self.y, 200, 200)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 800, 0, 800, 800, 0, 'h', self.x, self.y, 200, 200)
        draw_rectangle(*self.get_collider('broken_magnum').get_bb())

    def get_collider(self, name):
        return self.colliders[name]

    def handle_collision(self, group, other):
        if group == 'p1_body:broken_magnum':
            if self.dir == 1:
                self.x = other.get_bb()[0] - 70
            elif self.dir == -1:
                self.x = other.get_bb()[2] + 70
            if self.state == 'launch':
                self.state = 'hit'
                self.timer = 0.0
                self.count += 1
                if self.count >= 3:
                    PlayScene_world.remove_collision_object(self)
                    PlayScene_world.remove_object(self)

        elif group == 'p2_body:broken_magnum':
            if self.dir == 1:
                self.x = other.get_bb()[0] - 70
            elif self.dir == -1:
                self.x = other.get_bb()[2] + 70
            if self.state == 'launch':
                self.state = 'hit'
                self.timer = 0.0
                self.count += 1
                if self.count >= 3:
                    PlayScene_world.remove_collision_object(self)
                    PlayScene_world.remove_object(self)

    def update_no_collision(self):
        self.collider_state = None