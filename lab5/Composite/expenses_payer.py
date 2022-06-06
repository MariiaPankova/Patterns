from  abc import ABC, abstractmethod

class ExpensesPayer(ABC):

    @abstractmethod
    def pay_expenses(self,amount):
        pass