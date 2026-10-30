"""
This module contains dictionaries which contain all shape functions from the shapes.py module.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import collections.abc as cabc  # noqa: I001
import numbers as num

import turtle_extension as tx


#* 📝 Type for any real number
type RealType = float | int | num.Real

 #* 📝 The type used for Shapes dictionaries which contain functions
 #* 📝 which take a Real number and ChainTurtle and return None
type ShapesDictType = dict[
   str, cabc.Callable[[RealType, tx.ChainTurtle], None]
]

SHAPES_LENGTH: ShapesDictType

SHAPES_LENGTH_SIDES: dict[str, cabc.Callable[[RealType, int, tx.ChainTurtle], None]]

SHAPES_RADIUS: ShapesDictType