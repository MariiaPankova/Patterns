from controller import *
from abc import ABC,abstractmethod

class Switchable(ABC):
    @abstractmethod
    def light_on(self):
        pass

    @abstractmethod
    def light_off(self):
        pass


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



class HomeLights(Switchable):
    def __init__(self, lamps=[]):
        self.lamps = lamps

    def light_off(self):
        for lamp in self.lamps:
            lamp.light_off()

    def light_on(self):
        for lamp in self.lamps:
            lamp.light_on()



