'''
2.2.2. Мер міста Х, Володя Скічко, вирішив оновити парк муніципального транспорту.
Для цього він видає наказ закупити A автобусів, T трамваїв та Tr – тролейбусів.
Кожен вид транспорту має вартість закупки та орієнтовну вартість експлуатації,
що розраховується на один кілометр пробігу. Для економії часу на підготовку та
 заключення договорів, а також з метою економії запчастин у подальшому,
 керівництво міста вирішує закупити всю техніку у одного з виробників – Volvo або Skoda.
  Тепер перед адміністрацією мера постало серйозне запитання, з ким із виробників
  заключити контракт. Допоможіть адміністрації у цьому питанні, при умові, що
  закуплений транспорт має пройти N тис км. Розгляньте можливість виходу на сцену
  третього виробника транспорту – Hyundai.
'''
from enum import Enum

class Manufacturer(Enum):
    VOLVO = 0,
    SKODA = 1,
    HYUNDAI = 2


class Transport:
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


class VolvoAutobus(Autobus):
    def __init__(self):
        super().__init__(1, 1)


class SkodaAutobus(Autobus):
    def __init__(self):
        super().__init__(1, 2)


class HyundaiAutobus(Autobus):
    def __init__(self):
        super().__init__(1, 3)


class Tram(Transport):
    def __str__(self):
        return "Tram"


class VolvoTram(Tram):
    def __init__(self):
        super().__init__(1, 1)


class SkodaTram(Tram):
    def __init__(self):
        super().__init__(1, 2)


class HyundaiTram(Tram):
    def __init__(self):
        super().__init__(1, 3)


class Trolleybus(Transport):
    def __str__(self):
        return "Trolleybus"

class VolvoTrolleybus(Trolleybus):
    def __init__(self):
        super().__init__(1, 1)


class SkodaTrolleybus(Trolleybus):
    def __init__(self):
        super().__init__(1, 2)


class HyundaiTrolleybus(Trolleybus):
    def __init__(self):
        super().__init__(1, 3)


def factory_method(manufacturer):
    factory_dict = {
        Manufacturer.VOLVO: (VolvoAutobus(), VolvoTram(), VolvoTrolleybus()),
        Manufacturer.HYUNDAI: (HyundaiAutobus(), HyundaiTram(), HyundaiTrolleybus()),
        Manufacturer.SKODA: (SkodaAutobus(), SkodaTram(), SkodaTrolleybus())
    }
    print(factory_dict)
    return factory_dict[manufacturer]


if __name__ == '__main__':
    a = 10
    t = 15
    tr = 20
    N = 1000
    for manufacturer in Manufacturer:
        autopark = factory_method(manufacturer)
        #print(autopark)
        print(f'Manufacturer: {manufacturer},\n '
              f'price for {a} autobuses is {a*autopark[0].get_cost()}, maintenance cost is {autopark[0].get_maintenance((N))} \n'
              f'price for {t} trams is {t*autopark[1].get_cost()}, maintenance cost is {autopark[1].get_maintenance((N))} \n'
              f'price for {tr} trolleybuses id {tr*autopark[2].get_cost()}, maintenance cost is {autopark[2].get_maintenance((N))}')
