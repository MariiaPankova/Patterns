from abc import ABC,abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_base(self, base):
        pass

    @abstractmethod
    def visit_staff(self, staff):
        pass

class SecretAgent(Visitor):
    def visit_staff(self, staff):
        print("Secret papers are stolen")

    def visit_base(self, base):
        print("Collecting information")

class Saboteur(Visitor):
    def visit_base(self, base):
        print("Soldiers are wounded")


    def visit_staff(self, staff):
        print("Secret papers are destroyed")
