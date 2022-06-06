from manager import Manager
from salesperson import Salesperson
from salesteam import Salesteam


if __name__ == '__main__':
    manager = Manager("Katya")
    salesperson = Salesperson("Vanya", manager)
    salesperson1 = Salesperson("Valera", manager)
    salesteam = Salesteam([manager, salesperson, salesperson1])
    salesteam1 = Salesteam([manager, salesteam])

    manager.pay_expenses(10)
    salesperson1.pay_expenses(15)
    salesteam.pay_expenses(40)
    salesteam1.pay_expenses(1000)
