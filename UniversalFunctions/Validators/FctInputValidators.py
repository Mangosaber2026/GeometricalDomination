from typing import Any, get_args
from collections.abc import Callable
from inspect import signature
from functools import wraps


def validate(value: Any, TYPE: type|tuple[type, ...], name: str = "value") -> None:
    """
    Takes a value and validates it against the given type and name
    :param value: given value
    :param TYPE: given type
    :param name: given parameter
    :return: None
    """
    if get_args(TYPE):
        TYPE = tuple(
            type(None) if t is None else t
            for t in get_args(TYPE)
        )

    if not isinstance(TYPE, (type, tuple)):
        raise TypeError(f"{TYPE!r} is not a valid type!")

    elif not isinstance(value, TYPE):
        if isinstance(TYPE, tuple):
            type_name = " or ".join(t.__name__ for t in TYPE)
        else:
            type_name = TYPE.__name__

        raise TypeError(f"{name!r} must be a {type_name!r} value, not {type(value).__name__!r}!")

def validate_func(func: Callable, *args, **kwargs) -> None:
    """
    Takes a function and it's arguments and validates it against the given type of the arguments
    :param func: given function
    :param args: given arguments
    :param kwargs: given specified arguments
    :return:
    """
    sig = signature(func)
    bound = sig.bind(*args, **kwargs)

    for name, value in bound.arguments.items():
        parameter = sig.parameters[name]

        if parameter.annotation is not parameter.empty:
            validate(value, parameter.annotation, name)

def validation_deco(func) -> Callable:
    """
    DECORATOR: takes a function and validates it's inputs against the given type of the arguments
    :param func: function
    :return: function
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        validate_func(func, *args, **kwargs)
        return func(*args, **kwargs)
    return wrapper