from customer import Customer
from strategies import *

if __name__ == '__main__':
    customer1 = Customer()
    customer1.set_strategy(PayPalPayment())
    customer1.make_payment(1000)

    customer2 = Customer()
    customer2.set_strategy(BankAccountPayment())
    customer2.make_payment(2000)