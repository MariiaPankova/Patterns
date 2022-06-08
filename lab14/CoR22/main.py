from handler import *

if __name__ == '__main__':
    handler = AddHandler()
    handler.set_next(DivHandler())\
            .set_next(MulHandler())\
            .set_next(SubHandler())

    tasks = [
        (1, 1, "+"),
        (2, 2, "*"),
        (10.0, 20.5, "-"),
        (100, 10, "/"),
        (0, 0, "*"),
    ]
    for task in tasks:
        handler.handle(*task)
