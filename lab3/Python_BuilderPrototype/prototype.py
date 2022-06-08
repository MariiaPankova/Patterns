from abc import ABC, abstractmethod
from builder import StringBuilder


class BasePrototype(ABC):
    def clone(self):
        pass


class ClonableStringBuilder(StringBuilder, BasePrototype):
    def clone(self):
        obj = self.__class__()
        obj.result = self.result
        return obj
