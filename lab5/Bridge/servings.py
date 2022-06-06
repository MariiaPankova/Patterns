from abc import ABC, abstractmethod, abstractproperty

class Serving(ABC):

    @abstractmethod
    def serve(self):
        pass