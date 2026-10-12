"""
This module contains a dictionary (UV) which contains important info about turtles and user_drawing_ft().

Other functions:

t_now() -> lets users take the current UV turtle

t_shape() -> lets users take the current turtle shape
"""

from typing import Any
from .TurtleHeart import ChainTurtle


UV: dict[str, Any]

def t_now() -> ChainTurtle:
    """
    This function returns the current UV turtle

    >>> turtle = ChainTurtle()
    >>> UV["tls"].append(turtle)
    >>> t_now()
    ChainTurtle()

    :return: ChainTurtle
    """
    ...

def t_shape() -> str:
    """
    This function returns the current UV turtle shape

    >>> UV['tls_shape'] = 'turtle'
    >>> t_shape()
    'turtle'

    :return: string
    """
    ...