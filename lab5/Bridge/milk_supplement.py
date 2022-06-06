from beverage import Beverage
from supplement import Supplement


class MilkyBeverage(Supplement):
    def __init__(self, milk_volume):
        self.name = "milky"
        self.milk_volume = milk_volume

    def add_supplement(self):
        print(f"Add {self.milk_volume} milk...")

    def add_cost(self):
        return self.milk_volume * 3

