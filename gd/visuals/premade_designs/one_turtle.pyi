"""
This module contains the `TurtleOne` class which contains premade drawing functions 
which need only one turtle.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.


import turtle_extension as tx

#* 📝 The type used for a list of ChainTurtle instances
type TurtleListType = list[tx.ChainTurtle]

class TurtleOne:

    # ========= TURTLE 1 =========

    @staticmethod
    def hexaflower(tls: TurtleListType) -> None:
        """
        Draws flowers with 12 triangle petals in a horizontal + vertical pattern.

        :param tls: list of 1 chainable turtle

        :return: None
        """


    @staticmethod
    def star_of_david(tls: TurtleListType) -> None:
        """
        Draws a star of David.

        :param tls: list of 1 chainable turtle

        :return: None
        """


    @staticmethod
    def diamond_pattern(tls: TurtleListType) -> None:
        """
        Draws a diamond pattern.

        :param tls: list of 1 chainable turtle

        :return: None
        """


    @staticmethod
    def hidden_sds(tls: TurtleListType) -> None:
        """
        Draws stars of David in the same orientation (1 turtle).

        :param tls: list of 1 chainable turtle

        :return: None
        """


    @staticmethod
    def gd_reference(tls: TurtleListType) -> None:
        """
        Draws a square icon that resembles a gd icon.

        :param tls: list of 1 chainable turtle

        :return: None
        """


    @staticmethod
    def tri_wheel(tls: TurtleListType) -> None:
        """
        Draws a wheel made with triangles on the sides.

        :param tls: list of 1 chainable turtle

        :return: None
        """
        
    
    @staticmethod
    def lotus_pattern(tls: TurtleListType) -> None:
        """
        Draws a lotus pattern (12 petals).

        :param tls: list of 1 chainable turtle

        :return: None
        """