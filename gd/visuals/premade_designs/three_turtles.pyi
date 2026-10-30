"""
This module contains the class `TurtleThree` which contains premade drawing functions
which need a list of 3 turtles.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import turtle_extension as tx

#* 📝 The type used for a list of ChainTurtle instances
type TurtleListType = list[tx.ChainTurtle]

class TurtleThree:

    # ========= TURTLE 3 =========

    @staticmethod
    def squares10(tls: TurtleListType) -> None:
        """
        Draws 4 squares on each corner, with 4 squares tilted by 45° in between them + Star of David (fill) in the middle.
        
        :param tls: list of 3 chainable turtles

        :return: None
        """

    @staticmethod
    def sd_flower(tls: TurtleListType) -> None:
        """
        Draws a 6 petalled flower inside a star of David inside a hexagon.
        
        :param tls: list of 3 chainable turtles

        :return: None
        """
