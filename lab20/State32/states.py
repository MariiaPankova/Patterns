from abc import ABC, abstractmethod
from fan import Fan


class State(ABC):
    def __init__(self, fan):
        self.fan = fan

    @abstractmethod
    def turn_up(self):
        pass

    @abstractmethod
    def turn_down(self):
        pass


class LowState(State):
    def turn_up(self):
        self.fan.set_state(MediumState(self.fan))
        print("Set on medium")

    def turn_down(self):
        pass


class MediumState(State):
    def turn_up(self):
        self.fan.set_state(HighState(self.fan))
        print("Set on high")

    def turn_down(self):
        self.fan.set_state(LowState(self.fan))
        print("Set on low")


class HighState(State):
    def turn_up(self):
        pass

    def turn_down(self):
        self.fan.set_state(MediumState(self.fan))
        print("Set on medium")
