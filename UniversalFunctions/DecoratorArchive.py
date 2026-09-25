from collections.abc import Callable
from .Validators.FctInputValidators import validation_deco


@validation_deco
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

def deco_superposition(*decorators) -> Callable:
    """
    DECORATOR! this decorator takes multiple decorators and applies them to the given function the same way python would naturally
    :param decorators: decorator functions
    :return: supplied function
    """

    if not all(callable(decorator) for decorator in decorators):
        raise TypeError("All decorators must be callable")
    def inner_deco(func):
        for decorator in reversed(decorators):
            func = decorator(func)

        return func
    return inner_deco