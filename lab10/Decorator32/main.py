from beverage import *
from supplement import *

if __name__ == '__main__':
    espresso_with_two_sugar = Espresso()
    espresso_with_two_sugar = SugarDecorator(espresso_with_two_sugar)
    espresso_with_two_sugar = SugarDecorator(espresso_with_two_sugar)
    print(espresso_with_two_sugar)

    black_sour_cream_two_sugar = DarkRoast()
    black_sour_cream_two_sugar = SugarDecorator(black_sour_cream_two_sugar)
    black_sour_cream_two_sugar = SugarDecorator(black_sour_cream_two_sugar)
    black_sour_cream_two_sugar = SweetCreamDecorator(
        black_sour_cream_two_sugar
    )
    print(black_sour_cream_two_sugar)

    black_with_cream_and_sugar = DarkRoast()
    black_with_cream_and_sugar = SugarDecorator(black_with_cream_and_sugar)
    black_with_cream_and_sugar = CreamDecorator(black_with_cream_and_sugar)
    print(black_with_cream_and_sugar)

    decaf_milk_two_sugar = Decaf()
    decaf_milk_two_sugar = MilkDecorator(decaf_milk_two_sugar)
    decaf_milk_two_sugar = SugarDecorator(decaf_milk_two_sugar)
    decaf_milk_two_sugar = SugarDecorator(decaf_milk_two_sugar)
    print(decaf_milk_two_sugar)
