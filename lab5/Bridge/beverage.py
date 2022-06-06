from abc import ABC, abstractmethod, abstractproperty

class Beverage(ABC):
    def __init__(self, sugar: int, supplement, water_volume: int, serving):
        self.sugar = sugar
        self.supplement = supplement
        self.water_volume = water_volume
        self.serving = serving


    def prepare(self):
        if self.supplement:
            self.supplement.add_supplement()
        print(f"Put {self.water_volume} hot water...")
        if self.sugar > 0:
            print(f"Put {self.sugar} pieces of sugar...")
        self.serving.serve()

    @abstractmethod
    def drink(self):
        pass

    @abstractproperty
    def cost(self):
        pass
