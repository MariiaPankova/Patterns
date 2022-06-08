from accelerator import  *
from clutch import *
from gear_stick import *
from handbrake import *
from ignition import *

class Facade:
    def __init__(self):
        self.ignition = Ignition()
        self.clutch = Clutch()
        self.accelerator = Accelerator()
        self.gear_stick = GearStick()
        self.hand_brake = Handbrake()

    def drive(self):
        self.ignition.turn_on()
        self.hand_brake.press()
        self.clutch.press()
        self.gear_stick.change_gear(1)
        self.clutch.lift()
        self.hand_brake.lift()
        self.accelerator.press()
