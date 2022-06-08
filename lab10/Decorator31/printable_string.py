from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def print(self):
        pass


class PrintableStrings(Component):
    def __init__(self, base: str):
        self.base = base

    def print(self):
        print(self.base, end="")
