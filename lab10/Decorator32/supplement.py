from beverage import Beverage


class SupplementDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage


class CreamDecorator(SupplementDecorator):
    @property
    def description(self):
        return self.beverage.description + ", Cream"

    @property
    def cost(self):
        return self.beverage.cost + 0.4


class MilkDecorator(SupplementDecorator):
    @property
    def description(self):
        return self.beverage.description + ", Milk"

    @property
    def cost(self):
        return self.beverage.cost + 0.2


class SweetCreamDecorator(SupplementDecorator):
    @property
    def description(self):
        return self.beverage.description + ", Sweet-Cream"

    @property
    def cost(self):
        return self.beverage.cost + 0.4


class SugarDecorator(SupplementDecorator):
    @property
    def description(self):
        return self.beverage.description + ", Sugar"

    @property
    def cost(self):
        return self.beverage.cost + 0.1
