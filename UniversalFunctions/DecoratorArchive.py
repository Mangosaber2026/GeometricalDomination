from typing import Callable


def class_decorator(decorator: Callable) -> Callable:
    """
    DECORATOR!!   Creates a class decorator that applies the given decorator to every user defined function
    :param decorator: provided decorator function
    :return: a class decorator that transforms the class (& it's functions) and returns it
    """
    def inner(cls):
        for name, func in vars(cls).items():
            if callable(func) and not name.startswith("_"):
                setattr(cls, name, decorator(func))
        return cls
    return inner