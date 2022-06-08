from base_decorator import BaseDecorator


class PostExclaimDecorator(BaseDecorator):
    def print(self):
        super().print()
        print("!", end="")
