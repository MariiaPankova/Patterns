from abc import ABC, abstractmethod

class Iterator:
    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def has_more(self):
        pass


class EmployeeIterator:
    def __init__(self, employee_list):
        self.collection = employee_list
        self.iteration_state = 0

    def has_more(self):
        return self.iteration_state < len(self.collection)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_more():
            raise StopIteration
        val = self.collection[self.iteration_state]
        self.iteration_state += 1
        return val
