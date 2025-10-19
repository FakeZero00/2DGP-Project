class StateMachine:
    def __init__(self, start_state, rules):
        self.cur_state = start_state
        self.cur_state.enter(('START', 0))
        self.rules = rules

    def update(self):
        self.cur_state.do()

    def draw(self):
        self.cur_state.draw()

    def handle_state_event(self, state_event):
        for events in self.rules[self.cur_state]:
            if events(state_event):
                next_state = self.rules[self.cur_state][events]
                self.cur_state.exit(state_event)
                next_state.enter(state_event)
                self.cur_state = next_state
                return
