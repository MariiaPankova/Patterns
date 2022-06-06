from beverage import Beverage
from supplement import Supplement


class BlackBeverage(Supplement):
    def __init__(self):
        self.name = "black"

    def add_supplement(self):
        print("Add extra bitterness...")

    def add_cost(self):
        return 3

