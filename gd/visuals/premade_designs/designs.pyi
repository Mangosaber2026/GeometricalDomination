"""
This module contains an arsenal of premade geometrical designs/patterns and decorators for them.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

from collections.abc import Callable  # noqa: I001

import turtle_extension as tx

from . import (
   one_turtle,
   two_turtles, 
   three_turtles, 
   four_turtles,
   six_turtles,
   self_contained_turtles,
   variable_turtles,
)


 #* 📝 The type used for a list of ChainTurtle
type TlsType = list[tx.ChainTurtle]

 #* 📝 The type used for one of Designs functions
type DesignFuncType = Callable[[TlsType], None]

type WrapperFuncType = Callable[[], TlsType]

 #* 📝 The type returned from a wrapper that wraps the Designs functions
type TurtlesReturnType = Callable[[DesignFuncType], WrapperFuncType]

 #* 📝 The type for the dictionary retrieved from Designs
type PATTERNSType = dict[
str,
Callable[[list[tx.ChainTurtle]], list[tx.ChainTurtle]]
| Callable[[], list[tx.ChainTurtle]]
| Callable[[], PATTERNSType]
]

class Designs(
   one_turtle.TurtleOne,
   two_turtles.TurtleTwo,
   three_turtles.TurtleThree,
   four_turtles.TurtleFour,
   six_turtles.TurtleSix,
   self_contained_turtles.TurtleSelfMade,
   variable_turtles.TurtleToChoose
):
    """
    This class contains classes which are names after how many turtles the functions in those classes need.
    """

# ========= NO TURTLES REQUIRED =========

    @staticmethod
    def change_shape() -> None:
        """
        Changes the shape of the turtle according to user input.

        :return: None
        """


    @staticmethod
    def list_designs() -> PATTERNSType:
        """
        Creates a dictionary with all the designs and returns it.

        :return: dictionary
        """


def get_Patterns_dict() -> PATTERNSType:
    """
    PATTERNS dictionary launcher.
    
    :return: dictionary mapping function names with the actual function
    """

PATTERNS: PATTERNSType