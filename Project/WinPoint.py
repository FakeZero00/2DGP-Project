from pico2d import *

class WinPoint:
    def __init__(self, player):
        self.blank = load_image('../Sprite/WinPoint_Blank.png')
        self.fill = load_image('../Sprite/WinPoint_Fill.png')
        self.player = player
        self.current_point = 0

    def update(self):
        pass

    def draw(self):
        if self.player == 1:
            if self.current_point == 0:
                self.blank.clip_composite_draw(0, 0, 378, 378, 0, '', 90, 750, 50, 50)
                self.blank.clip_composite_draw(0, 0, 378, 378, 0, '', 130, 750, 50, 50)
            elif self.current_point == 1:
                self.fill.clip_composite_draw(0, 0, 378, 378, 0, '', 90, 750, 50, 50)
                self.blank.clip_composite_draw(0, 0, 378, 378, 0, '', 130, 750, 50, 50)
            elif self.current_point == 2:
                self.fill.clip_composite_draw(0, 0, 378, 378, 0, '', 90, 750, 50, 50)
                self.fill.clip_composite_draw(0, 0, 378, 378, 0, '', 130, 750, 50, 50)
        if self.player == 2:
            if self.current_point == 0:
                self.blank.clip_composite_draw(0, 0, 378, 378, 0, 'h', 1600 - 90, 750, 50, 50)
                self.blank.clip_composite_draw(0, 0, 378, 378, 0, 'h', 1600 - 130, 750, 50, 50)
            elif self.current_point == 1:
                self.fill.clip_composite_draw(0, 0, 378, 378, 0, 'h', 1600 - 90, 750, 50, 50)
                self.blank.clip_composite_draw(0, 0, 378, 378, 0, 'h', 1600 - 130, 750, 50, 50)
            elif self.current_point == 2:
                self.fill.clip_composite_draw(0, 0, 378, 378, 0, 'h', 1600 - 90, 750, 50, 50)
                self.fill.clip_composite_draw(0, 0, 378, 378, 0, 'h', 1600 - 130, 750, 50, 50)

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        pass