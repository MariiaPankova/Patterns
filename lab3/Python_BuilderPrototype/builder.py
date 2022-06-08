from abc import ABC, abstractmethod


class BaseBuilder(ABC):
    @abstractmethod
    def append_substring(self, substring):
        pass

    @abstractmethod
    def insert_substring(self, substring, position):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class StringBuilder(BaseBuilder):
    def __init__(self):
        self.result = None
        self.reset()

    def reset(self):
        self.result = ""
        return self

    def append_substring(self, substring):
        self.result += substring
        return self

    def insert_substring(self, substring, position):
        assert 0 <= position < len(self.result)
        self.result = self.result[:position] + substring + self.result[position:]
        return self

    def get_result(self):
        return self.result
