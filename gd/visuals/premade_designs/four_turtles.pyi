"""
This module contains the class `TurtleFour` which contains 
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import turtle_extension as tx

#* 📝 The type used for a list of ChainTurtle instances
type TurtleListType = list[tx.ChainTurtle]

class TurtleFour:

    # ========= TURTLE 4 =========

    @staticmethod
    def flower_4petals(tls: TurtleListType) -> None:
        """
        Draws a flower with 4 petals.

        :param tls: list of 4 chainable turtles

        :return: None
        """


    @staticmethod
    def square4(tls: TurtleListType) -> None:
        """
        Draws 4 squares where the axes slice the squares in half.

        :param tls: list of 4 chainable turtles

        :return: None
        """


    @staticmethod
    def quadrant_square(tls: TurtleListType) -> None:
        """
        Draws squares in each quadrant.

        :param tls: list of 4 chainable turtles

        :return: None
        """


    @staticmethod
    def multi_square_grid(tls: TurtleListType) -> None:
        """
        Draws a 45° tilted grid with 4 turtles => 4 colors.

        :param tls: list of 4 chainable turtles

        :return: None
        """