from enum import Enum


class WheelMaterial(Enum):
    STEEL = "steel"
    ALLOY = "alloy"


class Wheel:
    def __init__(self, diameter, material):
        self.diameter = diameter
        self.material = material

    def __str__(self):
        return f'Wheel (material = {self.material}, diameter = {self.diameter})'
