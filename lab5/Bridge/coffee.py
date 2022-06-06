from beverage import Beverage
from supplement import Supplement


class Coffee(Beverage):

    def prepare(self):
        print("Put some coffee...")
        super().prepare()

    def drink(self):
        print(f"Drink {self.supplement.name} coffee!")

    def cost(self):
        return 10 + self.supplement.add_cost()