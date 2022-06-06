from coffee import Coffee
from black_supplement import BlackBeverage
from milk_supplement import MilkyBeverage
from tee import Tee
from chocolate import Chocolate
from indoors_serving import IndoorsServing
from outdoors_serving import OutdoorsServing

def beverage_info(beverage):
    print('----------')
    beverage.prepare()
    print("Cost of beverage:", beverage.cost())
    beverage.drink()


if __name__ == '__main__':
    extra_black = BlackBeverage()
    extra_milk = MilkyBeverage(3)

    black_coffee = Coffee(3, extra_black, 1, IndoorsServing())
    beverage_info(black_coffee)

    milk_coffee = Coffee(3, extra_milk, 1, IndoorsServing())
    beverage_info(milk_coffee)

    black_tee = Tee(3, extra_black, 2, IndoorsServing())
    beverage_info(black_tee)

    milk_tee = Tee(3, extra_milk, 2, OutdoorsServing())
    beverage_info(milk_tee)

    black_chocolate = Chocolate(3, extra_black, 3, OutdoorsServing())
    beverage_info(black_chocolate)

    milk_chocolate = Chocolate(3, extra_milk, 3, OutdoorsServing())
    beverage_info(milk_chocolate)