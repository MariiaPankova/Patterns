class GearStick:
    def __init__(self):
        self.gear = 0

    def change_gear(self, gear: int):
        print(f"Changing gear to {gear}")
        self.gear = gear
