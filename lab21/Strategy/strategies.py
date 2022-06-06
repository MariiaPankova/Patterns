from abc import ABC,abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, amount):
        pass

class PayPalPayment(Strategy):
    def execute(self, amount):
        print(f'Payment of {amount} $ made from PayPal.')


class BankAccountPayment(Strategy):
    def execute(self, amount):
        print(f'Payment of {amount} $ made from bank account.')
