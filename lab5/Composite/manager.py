from expenses_payer import ExpensesPayer

class Manager(ExpensesPayer):
    def __init__(self, name):
        self.name = name

    def pay_expenses(self, amount):
        print(self.name + f' has been paid $ {amount}')
