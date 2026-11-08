"""
This module contains dictionaries which contain all shape functions from the shapes.py module.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import collections.abc as cabc
import numbers as num

import turtle_extension as tx

#* 📝 Type for any real number
type RealType = float | int | num.Real

 #* 📝 The type used for Shapes dictionaries which contain functions
 #* 📝 which take a Real number and ChainTurtle and return None
type ShapesDictType = dict[
   str, cabc.Callable[[RealType, tx.ChainTurtle], None]
]


def shapes_length_dict() -> ShapesDictType:
   """
   Creates and returns a dictionary mapping all functions from the Shapes class 
   which require the length and tls_num as parameters.

   :return: dictionary with function names -> function
   """


def shapes_length_sides_dict() -> dict[
   str,
   cabc.Callable[
      [RealType, int, tx.ChainTurtle],
      None
      ]
   ]:
   """
   Creates and returns a dictionary mapping all functions from the Shapes class 
   which require length, number of sides and turtle as parameters.

   :return: dictionary with function names -> function
   """


def shapes_radius_dict() -> ShapesDictType:
   """
   Creates and returns a dictionary mapping all functions from the Shapes class 
   which require radius and turtle as parameters.

   :return: dictionary with function names -> function
   """