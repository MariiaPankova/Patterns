from base_decorator import BaseDecorator
from post_comma import PostCommaDecorator
from post_endl import PostEndlDeccorator
from post_exclaim import PostExclaimDecorator
from post_word import PostWordDecorator
from pre_word import PreWordDecorator
from printable_string import PrintableStrings


if __name__ == "__main__":
    hello = PrintableStrings("")
    hello = PostCommaDecorator(hello)
    hello = PostWordDecorator(hello, "World")
    hello = PostExclaimDecorator(hello)
    hello = PostEndlDeccorator(hello)
    hello = PreWordDecorator(hello, "Hello")
    hello.print()
