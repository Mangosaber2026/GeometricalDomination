"""
This module contains dictionaries which contain all shape functions from the shapes.py module.
"""

from collections.abc import Callable
from numbers import Real

import TurtleExtension as tx


type ShapesDictType = dict[
   str, Callable[[Real, tx.ChainTurtle], None]
]
<<<<<<< HEAD
=======

>>>>>>> experimental

SHAPES_LENGTH: ShapesDictType

SHAPES_LENGTH_SIDES: dict[str, Callable[[Real, int, tx.ChainTurtle], None]]

SHAPES_RADIUS: ShapesDictType