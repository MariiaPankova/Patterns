from printable_string import Component
from base_decorator import BaseDecorator


class PreWordDecorator(BaseDecorator):
    def __init__(self, component: Component, word: str):
        super().__init__(component)
        self.word = word

    def print(self):
        print(self.word, end="")
        super().print()
