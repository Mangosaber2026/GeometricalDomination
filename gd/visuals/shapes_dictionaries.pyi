"""
This module contains dictionaries which contain all shape functions from the shapes.py module.
"""

from collections.abc import Callable
from numbers import Real

import turtle_extension as tx


 #* 📝 The type used for [[Shapes]] dictionaries which contain functions
 #* 📝 which take a Real number and ChainTurtle and return None
type ShapesDictType = dict[
   str, Callable[[Real, tx.ChainTurtle], None]
]

SHAPES_LENGTH: ShapesDictType

SHAPES_LENGTH_SIDES: dict[str, Callable[[Real, int, tx.ChainTurtle], None]]

SHAPES_RADIUS: ShapesDictType