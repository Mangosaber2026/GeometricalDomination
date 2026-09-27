"""
This module contains validators from the CTM Dimension.
"""

from typing import Any, get_args


def ctm_validate(value: Any, TYPE: type | tuple[type, ...], name: str = "value") -> bool:
    """
    Takes a value and validates it against the given type and name
    :param value: given value
    :param TYPE: given type
    :param name: name of the value
    :return: bool if value meets expected type
    :raises TypeError: if TYPE is invalid or value does not match TYPE
    """
    if get_args(TYPE):
        TYPE = tuple(
            type(None) if t is None else t
            for t in get_args(TYPE)
        )

    if not isinstance(TYPE, (type, tuple)):
        raise TypeError(f"{TYPE!r} is not a valid type!")

    if not isinstance(value, TYPE):
        if isinstance(TYPE, tuple):
            type_name = " or ".join(t.__name__ for t in TYPE)
        else:
            type_name = TYPE.__name__

        raise TypeError(f"{name!r} must be a {type_name!r} value, not {type(value).__name__!r}!")
    return True