from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass

class Manager(Employee):
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_manager(self)


class SalesPerson(Employee):
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_salesperson(self)

class ITSupport(Employee):
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_itsupport(self)


class StaffList(Employee):
    def __init__(self, salaries=[]):
        self.salaries = salaries

    def add_employee(self, employee):
        self.salaries.append(employee)

    def get_salary(self):
        sum = 0
        for employee in self.salaries:
            sum += employee.get_salary()
        return sum

    def accept(self, visitor):
        for person in self.salaries:
            person.accept(visitor)
