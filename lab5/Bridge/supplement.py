from abc import ABC, abstractmethod, abstractproperty

class Supplement(ABC):

    def __init__(self, name, cost):
        self.name = name

    @abstractmethod
    def add_supplement(self):
        pass

    @abstractproperty
    def add_cost(self):
        pass

