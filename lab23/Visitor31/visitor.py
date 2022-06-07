from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_manager(self, manager):
        pass

    @abstractmethod
    def visit_salesperson(self, salesperson):
        pass

    @abstractmethod
    def visit_salesteam(self, salesteam):
        pass

    @abstractmethod
    def visit_itsupport(self, itsupport):
        pass


class SalaryUpVisitor(Visitor):
    def __init__(self, proc):
        self.proc = proc

    def visit_manager(self,manager):
        manager.set_salary(manager.get_salary()*(1+self.proc))

    def visit_salesperson(self,salesperson):
        salesperson.set_salary(salesperson.get_salary()*(1+self.proc))

    def visit_salesteam(self, salesteam):
        salesteam.set_salary(salesteam.get_salary()*(1+self.proc))

    def visit_itsupport(self, itsupport):
        itsupport.set_salary(itsupport.get_salary()*(1+self.proc))



class SalaryDownVisitor(Visitor):
    def __init__(self, proc):
        self.proc = proc

    def visit_manager(self, manager):
        manager.set_salary(manager.get_salary() * (1 - self.proc))

    def visit_salesperson(self, salesperson):
        salesperson.set_salary(salesperson.get_salary()*(1-self.proc))

    def visit_salesteam(self, salesteam):
        salesteam.set_salary(salesteam.get_salary()*(1-self.proc))

    def visit_itsupport(self, itsupport):
        itsupport.set_salary(itsupport.get_salary()*(1-self.proc))