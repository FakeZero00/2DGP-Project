from pico2d import *

class Bar:
    def __init__(self, player, bar_type, init_point):
        self.background = load_image('../Sprite/Hp_bar_Background.png')
        self.hpbar = load_image('../Sprite/Hp_bar.png')
        self.ppbar = load_image('../Sprite/Power_bar.png')
        self.player = player
        self.bar_type = bar_type
        self.Max = 100
        self.current_point = init_point

    def update(self):
        pass

    def draw(self):
        if self.bar_type == 'HP':
            if self.player == 1:
                self.background.clip_composite_draw(0, 0, 700, 80, 0, '', 400, 820, 700, 80)
                self.hpbar.clip_composite_draw(0, 0, int(700 / self.Max * self.current_point), 80, 0, '', 50 + (int(700 / self.Max * self.current_point) // 2), 820, int(700 / self.Max * self.current_point), 80)
            else:
                self.background.clip_composite_draw(0, 0, 700, 80, 0, 'h', 1600 - 400, 820, 700, 80)
                self.hpbar.clip_composite_draw(0, 0, int(700 / self.Max * self.current_point), 80, 0, 'h', 1600 - (50 + (int(700 / self.Max * self.current_point) // 2)), 820, int(700 / self.Max * self.current_point), 80)
        elif self.bar_type == 'PP':
            if self.player == 1:
                self.background.clip_composite_draw(0, 0, 700, 80, 0, '', 585, 750, 350, 40)
                self.ppbar.clip_composite_draw(0, 0, int(700 / self.Max * self.current_point), 80, 0, '', 410 + (int(350 / self.Max * self.current_point) // 2), 750, int(350 / self.Max * self.current_point), 40)
            else:
                self.background.clip_composite_draw(0, 0, 700, 80, 0, 'h', 1600 - 585, 750, 350, 40)
                self.ppbar.clip_composite_draw(0, 0, int(700 / self.Max * self.current_point), 80, 0, 'h', 1600 - (410 + (int(350 / self.Max * self.current_point) // 2)), 750, int(350 / self.Max * self.current_point), 40)

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        pass