from pico2d import load_image

class StateMachine:
    def __init__(self, start_state):
        self.cur_state = start_state

    def update(self):
        self.cur_state.do()

    def draw(self):
        self.cur_state.draw()

# 상태 클래스들
class Idle:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self):
        self.gaogaigar.frame = 0

    def exit(self):
        pass

    def do(self):
        pass

    def draw(self):
        self.gaogaigar.image.clip_draw(400, 400, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Run:
    def __init__(self, gaogaigar):
        self.gaogaigar = gaogaigar

    def enter(self):
        self.gaogaigar.frame = 0

    def exit(self):
        pass

    def do(self):
        self.gaogaigar.frame = (self.gaogaigar.frame + 1) % 10

    def draw(self):
        self.gaogaigar.image.clip_draw(self.gaogaigar.frame * 400, 0, 400, 400, self.gaogaigar.x, self.gaogaigar.y)

class Gaogaigar:
    def __init__(self):
        self.image = load_image('../Sprite/Move_Sprite(temp_resize).png')
        self.x, self.y = 800, 450
        self.frame = 0

        self.IDLE = Idle(self)
        self.RUN = Run(self)
        self.statemachine = StateMachine(self.RUN)

    def update(self):
        self.statemachine.update()

    def draw(self):
        self.statemachine.draw()

