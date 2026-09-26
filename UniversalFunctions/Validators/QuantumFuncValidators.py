from collections.abc import Callable
from inspect import signature
from typing import get_origin
from .QuantumValidators import qtm_lt_validator
from .FctInputValidators import validate
from functools import wraps
from .SimpleValidators import callable_validator


def qtm_func_validator(func: Callable, *args, **kwargs) -> bool:
    """
    Belongs to the Quantum Dimension!

    Takes a function and compares the entered value with the expected type
    :param func: given function
    :param args: arguments
    :param kwargs: keyword arguments
    :return: True if the provided argument matches the expected type, raises an error if not
    """
    callable_validator(func)
    sig = signature(func)
    bound = sig.bind(*args, **kwargs)

    for name, value in bound.arguments.items():
        parameter = sig.parameters[name]
        type_ = parameter.annotation

        if type_ is parameter.empty:
            continue

        origin = get_origin(type_)

        if origin in (list, tuple):
            qtm_lt_validator(value, type_, name)
        else:
            validate(value, type_, name)

    return True

def qtm_validation_decorator(func: Callable) -> Callable:
    """
    DECORATOR! Belongs to the Quantum Dimension!

    Decorates a function with the quantum function validator and returns the function
    :param func: provided function
    :return: validated function
    """
    callable_validator(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        qtm_func_validator(func, *args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
