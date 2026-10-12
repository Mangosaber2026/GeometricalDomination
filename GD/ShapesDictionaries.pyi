"""
This module contains dictionaries which contain all shape functions from the Shapes.py module.
"""

from collections.abc import Callable
from numbers import Real
from .TurtleHeart import ChainTurtle


type shapes_dict_type = dict[str, Callable[[Real, ChainTurtle], None]]

SHAPES_LENGTH: shapes_dict_type

SHAPES_LENGTH_SIDES: dict[str, Callable[[Real, int, ChainTurtle], None]]

SHAPES_RADIUS: shapes_dict_type