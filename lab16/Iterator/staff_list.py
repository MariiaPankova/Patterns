from staff_list_iterator import EmployeeIterator
from abc import ABC,abstractmethod

class IterableCollection(ABC):
    @abstractmethod
    def create_iteraror(self):
        pass


class StaffList:
    def __init__(self, employees):
        self.employees = employees

    def create_iterator(self):
        return EmployeeIterator(self.employees)
