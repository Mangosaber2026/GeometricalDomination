"""
This module contains the class `TurtleTwo` which contains functions
which need 2 turtles.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import turtle_extension as tx

#* 📝 The type used for a list of ChainTurtle instances
type TlsType = list[tx.ChainTurtle]

class TurtleTwo:

    # ========= TURTLE 2 =========

    @staticmethod
    def duo_spiral(tls: TlsType) -> None:
        """
        Draws 2 overlapping spirals, one to the right and one to the left.

        :param tls: list of 2 chainable turtles

        :return: None
        """

    @staticmethod
    def squares8(tls: TlsType) -> None:
        """
        Draws 4 squares on each corner, with 4 squares tilted by 45° in between them + square pattern in between.
        
        :param tls: list of 2 chainable turtles

        :return: None
        """

    @staticmethod
    def tri_hexaflower(tls: TlsType) -> None:
        """
        Draws flowers with 12 triangle petals with lines in the middle in a horizontal + vertical pattern.
        
        :param tls: list of 2 chainable turtles

        :return: None
        """

    @staticmethod
    def sd_pattern(tls: TlsType) -> None:
        """
        Draws stars of David in a horizontal + vertical pattern.

        :param tls: list of 2 chainable turtles

        :return: None
        """

    @staticmethod
    def sd_spiral(tls: TlsType) -> None:
        """
        Draws stars of David in a spiral pattern inside a main star with 2 turtles.

        :param tls: list of 2 chainable turtles

        :return: None
        """

    @staticmethod
    def sd_triflower(tls: TlsType) -> None:
        """
        Draws three 6 petalled flowers in triangular shape in a star of David in an external structure.
        
        :param tls: list of 2 chainable turtles

        :return: None
        """

    @staticmethod
    def hexaflower_sd(tls: TlsType) -> None:
        """
        Draws six 6 petalled flowers in a hexagon pattern, with lines in between the petals, all inside a star of David.
        
        :param tls: list of 2 chainable turtles

        :return: None
        """