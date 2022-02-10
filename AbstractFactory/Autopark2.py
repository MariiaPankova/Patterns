from abc import ABCMeta

class Transport(metaclass=ABCMeta):
    def __init__(self, cost, maintenance_cost):
        self.cost = cost
        self.maintenance_cost = maintenance_cost

    def __repr__(self):
        return self.__str__()

    def get_cost(self):
        return self.cost

    def get_maintenance(self, N):
        return self.maintenance_cost*N


class Autobus(Transport):
    def __str__(self):
        return "Autobus"


class Tram(Transport):
    def __str__(self):
        return "Tram"


class Trolleybus(Transport):
    def __str__(self):
        return "Trolleybus"


class Manufacturer(metaclass=ABCMeta):
    def __init__(self, name, bus_prices, tram_prices, trolleybus_prices):
        self.name = name
        self.bus_prices = bus_prices
        self.tram_prices = tram_prices
        self.trolleybus_prices = trolleybus_prices

    def sell_bus(self) -> Transport:
        return Autobus(*self.bus_prices)

    def sell_trolley(self):
        return Trolleybus(*self.trolleybus_prices)

    def sell_tram(self):
        return Tram(*self.tram_prices)

    def get_name(self):
        return self.name

class Volvo(Manufacturer):
    def __init__(self):
        super().__init__("Volvo",
                         (10, 1),
                         (12, 2),
                         (13, 3))


class Skoda(Manufacturer):
    def __init__(self):
        super().__init__("Skoda",
                         (11,1),
                         (18,3),
                         (20,1))


class Hyundai(Manufacturer):
    def __init__(self):
        super().__init__("Hyundai",
                         (8,5),
                         (9,9),
                         (3,12))


if __name__ == '__main__':
    a = 10
    t = 12
    tr = 20
    N = 1000
    for man in (Volvo(), Skoda(), Hyundai()):
        print(f'Contract with {man.name}: \n'
              f'{a} buses will cost {man.sell_bus().get_cost()*a}, maintenance for {N} km will cost {man.sell_bus().get_maintenance(N)}\n'
              f'{t} trolleybuses will cost {man.sell_trolley().get_cost()*t}, with maintenance {man.sell_trolley().get_maintenance(N)}\n'
              f'{tr} trams will cost {man.sell_tram().get_cost()*tr}, maintenance {man.sell_tram().get_maintenance(N)}\n'
              f'TOTAL PRICE {man.sell_bus().get_cost()*a+man.sell_trolley().get_cost()*t+man.sell_tram().get_cost()*tr}')

