from beverage import Beverage
from supplement import Supplement


class Chocolate(Beverage):

    def prepare(self):
        print("Put some cacao...")
        super().prepare()

    def drink(self):
        print(f"Drink {self.supplement.name} chocolate!")

    def cost(self):
        return 15 + self.supplement.add_cost()