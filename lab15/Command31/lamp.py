from controller import *

class Lamp:
    def __init__(self, name="default"):
        self.name = name
        self.is_lamp_on = False

    def light_on(self):
        if self.is_lamp_on:
            return
        print(f'{self.name} is on')
        self.is_lamp_on = True

    def light_off(self):
        if not self.is_lamp_on:
            return
        print(f'{self.name} is off')
        self.is_lamp_on = False
