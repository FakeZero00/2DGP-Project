from pico2d import load_image

class StateMachine:
    def __init__(self, start_state):
        self.cur_state = start_state

    def update(self):
        self.cur_state.do()

    def draw(self):
        self.cur_state.draw()

class Idle:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self):
        pass

    def exit(self):
        pass

    def do(self):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(400, 400, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Gaogaigar:
    def __init__(self):
        self.image = load_image('../Sprite/Move_Sprite(temp_resize).png')
        self.x, self.y = 800, 450
        self.frame = 0

        self.IDLE = Idle(self)
        self.statemachine = StateMachine(self.IDLE)

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 400, 400, 400, self.x, self.y)
