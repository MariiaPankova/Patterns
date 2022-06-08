from base_decorator import BaseDecorator


class PostEndlDeccorator(BaseDecorator):
    def print(self):
        super().print()
        print("\n", end="")
