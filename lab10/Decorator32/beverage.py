from abc import ABC, abstractmethod


class Beverage(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def cost(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Bevrage: {self.description}, ${self.cost:.2f}"


class DarkRoast(Beverage):
    @property
    def description(self) -> str:
        return "DarkRoast"

    @property
    def cost(self) -> float:
        return 1.0


class Decaf(Beverage):
    @property
    def description(self) -> str:
        return "Decaf"

    @property
    def cost(self) -> float:
        return 1.0


class Espresso(Beverage):
    @property
    def description(self) -> str:
        return "Espresso"

    @property
    def cost(self) -> float:
        return 0.75
