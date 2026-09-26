from collections.abc import Callable

def callable_validator(func: Callable) -> bool:
    """
    Takes a function and checks if it is callable or not.
    :param func: provided function
    :return: True if it is callable, raises TypeError if not.
    """
    if not callable(func):
        raise TypeError(f"{func!r} is not a callable!")
    return True