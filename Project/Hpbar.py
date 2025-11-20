from pico2d import *

class Hpbar:
    def __init__(self, player):
        self.background = load_image('../Sprite/Hp_bar_Background.png')
        self.hpbar = load_image('../Sprite/Hp_bar.png')
        self.player = player
        self.Maxhp = 100
        self.hp = 100

    def update(self):
        pass

    def draw(self):
        if self.player == 1:
            self.background.clip_composite_draw(0, 0, 700, 80, 0, '', 400, 820, 700, 80)
            self.hpbar.clip_composite_draw(0, 0, int(700 / self.Maxhp * self.hp), 80, 0, '', 50 + (int(700 / self.Maxhp * self.hp) // 2), 820, int(700 / self.Maxhp * self.hp), 80)
        else:
            self.background.clip_composite_draw(0, 0, 700, 80, 0, 'h', 1600 - 400, 820, 700, 80)
            self.hpbar.clip_composite_draw(0, 0, int(700 / self.Maxhp * self.hp), 80, 0, 'h', 1600 - (50 + (int(700 / self.Maxhp * self.hp) // 2)), 820, int(700 / self.Maxhp * self.hp), 80)


    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        pass