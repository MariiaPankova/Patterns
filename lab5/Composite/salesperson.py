from expenses_payer import ExpensesPayer


class Salesperson(ExpensesPayer):
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

    def pay_expenses(self, amount):
        print(self.name + f' has been paid $ {amount}')
