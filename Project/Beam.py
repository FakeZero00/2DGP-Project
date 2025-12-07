from pico2d import *
from Project.Collider import Collider
import Game_Framework, PlayScene_world

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

RUN_SPEED_PPS = 1500

class Beam:
    def __init__(self, x, y, parent_object):
        self.image = load_image('../Sprite/Beam.png')
        self.x = x
        self.y = y
        self.parent_object = parent_object
        self.dir = self.parent_object.dir[0]

        self.timer = 0.0
        self.state = 'launch'

        self.colliders = {}
        self.colliders['beam'] = Collider(self.x - 100, self.y - 10, 200, 30, self)

    def update(self):
        self.x = self.x + RUN_SPEED_PPS * Game_Framework.frame_time * self.dir
        self.colliders['beam'].x = self.x - 100

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(0, 0, 800, 800, 0, '', self.x, self.y, 200, 200)
        elif self.dir == -1:
            self.image.clip_composite_draw(0, 0, 800, 800, 0, 'h', self.x, self.y, 200, 200)
        draw_rectangle(*self.get_collider('beam').get_bb())

    def get_collider(self, name):
        return self.colliders[name]

    def handle_collision(self, group, other):
        if group == 'p1_body:beam':
            PlayScene_world.remove_collision_object(self)
            PlayScene_world.remove_object(self)

        elif group == 'p2_body:beam':
            PlayScene_world.remove_collision_object(self)
            PlayScene_world.remove_object(self)