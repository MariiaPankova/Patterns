from beverage import Beverage
from supplement import Supplement


class Tee(Beverage):

    def prepare(self):
        print("Put some tee leaves...")
        super().prepare()

    def drink(self):
        print(f"Drink {self.supplement.name} tee!")

    def cost(self):
        return 7 + self.supplement.add_cost()