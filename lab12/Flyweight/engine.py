from enum import Enum


class Fuel(Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    ELECTRIC = "electric"


class Engine:
    def __init__(self, power, fuel):
        self.power = power
        self.fuel = fuel

    def __str__(self):
        return f"Engine (power = {self.power}, fuel = {self.fuel})"
