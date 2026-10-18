"""
This module contains dictionaries which contain all shape functions from the Shapes.py module.
"""

from collections.abc import Callable
from numbers import Real
import TurtleExtension as tx


type shapes_dict_type = dict[str, Callable[[Real, tx.ChainTurtle], None]]

SHAPES_LENGTH: shapes_dict_type

SHAPES_LENGTH_SIDES: dict[str, Callable[[Real, int, tx.ChainTurtle], None]]

SHAPES_RADIUS: shapes_dict_type