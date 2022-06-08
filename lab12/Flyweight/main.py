from car import *
from wheel import *
from engine import *
from random import choice, randint

def create_random_car():
    fuel = choice(list(Fuel))
    wheel_diameter = randint(17, 20)
    wheel_material = choice(list(WheelMaterial))
    power = randint(11, 15) * 10
    color = choice(list(Color))
    builder = CarBuilder()

    car = builder.reset()\
        .set_color(color)\
        .set_engine(power, fuel)\
        .set_wheel(wheel_diameter, wheel_material)\
        .build()
    print(car)

if __name__== '__main__':
    for _ in range(100):
        create_random_car()
