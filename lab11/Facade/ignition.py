class Ignition:
    def __init__(self):
        self.is_up = True

    def turn_off(self):
        print("Turning ignition off")
        self.is_up = False

    def turn_on(self):
        print("Turning ignition on")
        self.is_up = True
