from typing import Any, get_args, get_origin

def quantum_type_validator(value: list[Any]|tuple[Any], TYPE: Any, name: str) -> bool:
    """
    Takes a list of ONE specific element and validates its contents against the expected type
    :param value: list of elements
    :param TYPE: list[expected type]
    :param name: name of value
    :return: True if the contents of value satisfy the expected type
    """

    if not isinstance(value, (list, tuple)):
        raise TypeError("Value must be a list/tuple containing ONE type of object!")

    if get_origin(TYPE) is not list:
        raise TypeError(f"{TYPE} must be a list for a specific type! e.g. list[int]")

    element_type = get_args(TYPE)
    if len(element_type) != 1:
        raise TypeError("TYPE must contain only ONE type!")

    for index, element in enumerate(value):
        if not isinstance(element, element_type):
            raise TypeError(f"{name}[{index}] must be of type {element_type[0].__name__!r}!")

    return True