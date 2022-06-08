from enum import Enum
from wheel import *
from engine import *


class Color(Enum):
    WHITE = "white"
    BLACK = "black"
    RED = "red"
    GRAY = "gray"


class CarType(Enum):
    SEDAN = "sedan"
    HATCHBACK = "hatchback"
    SUV = "SUV"


class Car:
    def __init__(self, car_type, car_color, engine, wheel):
        self.car_type = car_type
        self.color = car_color
        self.engine = engine
        self.wheel = wheel

    def __str__(self):
        return f"Car (Car type = {self.car_type}, color = {self.color}," \
            f"engine = {self.engine}, wheels = {self.wheel})"


class CarBuilder:
    def __init__(self):
        self.car_type = None
        self.color = None
        self.engine = None
        self.wheel = None

        self.engine_cache = {}
        self.wheel_cache = {}
        self.reset()

    def reset(self):
        self.car_type = CarType.SEDAN
        self.color = Color.BLACK
        self.set_engine(10, Fuel.DIESEL)
        self.set_wheel(10, WheelMaterial.ALLOY)
        return self

    def set_type(self, car_type):
        self.car_type = car_type
        return self

    def set_color(self, color):
        self.color = color
        return self

    def set_engine(self, power: int, fuel):
        engine_hash = hash((power, fuel))
        self.engine = self.engine_cache.get(engine_hash)
        if self.engine is None:
            self.engine = Engine(power, fuel)
            print(f"Creating new engine. {self.engine}")
            self.engine_cache[engine_hash] = self.engine
        return self

    def set_wheel(self, diameter: int, material):
        wheel_hash = hash((diameter, material))
        self.wheel = self.wheel_cache.get(wheel_hash)
        if self.wheel is None:
            self.wheel = Wheel(diameter, material)
            print(f"Creating new wheel. {self.wheel}")
            self.wheel_cache[wheel_hash] = self.wheel
        return self

    def build(self) -> Car:
        if (
            self.car_type is None
            or self.color is None
            or self.engine is None
            or self.wheel is None
        ):
            raise ValueError()
        return Car(self.car_type, self.color, self.engine, self.wheel)
