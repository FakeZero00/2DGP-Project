from pico2d import *
import Game_Framework

class Timer:
    def __init__(self, init_time):
        self.image = load_image('../Sprite/numbers.png')
        self.time = init_time

    def update(self):
        self.time -= Game_Framework.frame_time

    def draw(self):
        total_seconds = int(self.time)
        tenseconds = total_seconds // 10
        oneseconds = total_seconds % 10

        if self.time >= 0.1:
            self.image.clip_draw(tenseconds * 512, 0, 512, 512, 1600 // 2 - 22, 900 - 75, 64, 64)  # 십의 자리
            self.image.clip_draw(oneseconds * 512, 0, 512, 512, 1600 // 2 + 22, 900 - 75, 64, 64)  # 일의 자리
        else:
            self.image.clip_draw(0 * 512, 0, 512, 512, 1600 // 2 - 22, 900 - 75, 64, 64)  # 십의 자리
            self.image.clip_draw(0 * 512, 0, 512, 512, 1600 // 2 + 22, 900 - 75, 64, 64)  # 일의 자리

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        pass