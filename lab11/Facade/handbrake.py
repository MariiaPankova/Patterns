class Handbrake:
    def __init__(self):
        self.is_up = True

    def press(self):
        print("Pressing handbrake down")
        self.is_up = False

    def lift(self):
        print("Lifting handbrake up")
        self.is_up = True
