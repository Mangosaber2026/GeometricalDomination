"""
This module contains a dictionary (UV) which contains important info about turtles and user_drawing_ft().

Other functions:

t_now() -> lets users take the current UV turtle

t_shape() -> lets users take the current turtle shape
"""

from .TurtleSkeleton import ChainTurtle
from typing import Any

# UV = UNIVERSAL VARIABLES
UV: dict[str, Any] = {
    "delay": None,            # Delay for user_drawing_ft()
      "t": 0,                   # user_drawing_ft's current turtle
      "tls": [],                # user_drawing_ft's turtle list
      "tls_shape": "arrow",     # user_drawing_ft's turtle's current shape
      "shape_library": [],      # user_drawing_ft's turtle shapes list
}
def t_now() -> ChainTurtle:
    """
    This function returns the current UV turtle
    :return: ChainTurtle
    """
    return UV["tls"][UV["t"]]

def t_shape() -> str:
    """
    This function returns the current UV turtle shape
    :return: string
    """
    return UV["tls_shape"]

