

class Fan:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def turn_up(self):
        self.state.turn_up()

    def turn_down(self):
        self.state.turn_down()
