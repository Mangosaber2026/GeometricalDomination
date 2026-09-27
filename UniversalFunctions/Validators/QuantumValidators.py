"""
This module contains type validators for list and tuple which belong to the QTM Dimension.
"""

from typing import Any, get_args, get_origin


def qtm_lt_validator(value: list[Any] | tuple[Any, ...], TYPE: Any, name: str) -> bool:
    """
    Takes a list of ONE specific element and validates its contents against the expected type
    :param value: list of elements
    :param TYPE: list[expected type]
    :param name: name of value
    :return: True if the contents of value satisfy the expected type
    """
    origin = get_origin(TYPE)
    if origin not in (list, tuple):
        raise TypeError(f"{TYPE} must be a list or tuple for a specific type! e.g. list[int]")

    if not isinstance(value, origin):
        raise TypeError(f"{name} must be of type {origin.__name__!r}!")

    element_type = get_args(TYPE)
    if origin is list:
        if len(element_type) != 1:
            raise TypeError("TYPE must contain only ONE type!")

    elif origin is tuple:
        if len(element_type) != 2 or element_type[1] is not Ellipsis:
            raise TypeError("tuple TYPE must contain only ONE type with the form tuple[T, ...]!")

    for index, element in enumerate(value):
        if not isinstance(element, element_type[0]):
            raise TypeError(f"{name}[{index}] must be of type {element_type[0].__name__!r}!")

    return True