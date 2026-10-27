"""
This module contains an arsenal of premade geometrical designs/patterns and decorators for them.
"""

from collections.abc import Callable

import turtle_extension as tx


 #* 📝 The type used for a list of [[ChainTurtle]]
type TlsType = list[tx.ChainTurtle]

 #* 📝 The type used for one of [[Designs]] functions
type DesignFuncType = Callable[[TlsType], None]

type WrapperFuncType = Callable[[], TlsType]

 #* 📝 The type returned from a wrapper that wraps the [[Designs]] functions
type TurtlesReturnType = Callable[[DesignFuncType], WrapperFuncType]

 #* 📝 The type for the dictionary retrieved from [[Designs]]
type PATTERNSType = dict[
str,
Callable[[list[tx.ChainTurtle]], list[tx.ChainTurtle]]
| Callable[[], list[tx.ChainTurtle]]
| Callable[[], PATTERNSType]
]


def turtles(amount: int) -> TurtlesReturnType:
    """
    DECORATOR:
    Takes a given number of turtles, gets their colors from the user and executes the function.

    :param amount: number of turtles > 0

    :return: list of turtles
    """

class Designs:
    """
    This class contains classes which are names after how many turtles the functions in those classes need.
    """

# ========= TURTLE 1 =========

    @staticmethod
    def hexaflower(tls: TlsType) -> None:
        """
        Draws flowers with 12 triangle petals in a horizontal + vertical pattern.

        :param tls: list of 1 chainable turtle

        :return: None
        """

    @staticmethod
    def star_of_david(tls: TlsType) -> None:
        """
        Draws a star of David.

        :param tls: list of 1 chainable turtle

        :return: None
        """

    @staticmethod
    def diamond_pattern(tls: TlsType) -> None:
        """
        Draws a diamond pattern.

        :param tls: list of 1 chainable turtle

        :return: None
        """

    @staticmethod
    def hidden_sds(tls: TlsType) -> None:
        """
        Draws stars of David in the same orientation (1 turtle).

        :param tls: list of 1 chainable turtle

        :return: None
        """

    @staticmethod
    def gd_reference(tls: TlsType) -> None:
        """
        Draws a square icon that resembles a gd icon.

        :param tls: list of 1 chainable turtle

        :return: None
        """

    @staticmethod
    def tri_wheel(tls: TlsType) -> None:
        """
        Draws a wheel made with triangles on the sides.

        :param tls: list of 1 chainable turtle

        :return: None
        """
    
    @staticmethod
    def lotus_pattern(tls: TlsType) -> None:
        """
        Draws a lotus pattern (12 petals).

        :param tls: list of 1 chainable turtle

        :return: None
        """
    
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

# ========= TURTLE 3 =========

    @staticmethod
    def squares10(tls: TlsType) -> None:
        """
        Draws 4 squares on each corner, with 4 squares tilted by 45° in between them + Star of David (fill) in the middle.
        
        :param tls: list of 3 chainable turtles

        :return: None
        """

    @staticmethod
    def sd_flower(tls: TlsType) -> None:
        """
        Draws a 6 petalled flower inside a star of David inside a hexagon.
        
        :param tls: list of 3 chainable turtles

        :return: None
        """

# ========= TURTLE 4 =========

    @staticmethod
    def flower_4petals(tls: TlsType) -> None:
        """
        Draws a flower with 4 petals.

        :param tls: list of 4 chainable turtles

        :return: None
        """

    @staticmethod
    def square4(tls: TlsType) -> None:
        """
        Draws 4 squares where the axes slice the squares in half.

        :param tls: list of 4 chainable turtles

        :return: None
        """

    @staticmethod
    def quadrant_square(tls: TlsType) -> None:
        """
        Draws squares in each quadrant.

        :param tls: list of 4 chainable turtles

        :return: None
        """

    @staticmethod
    def multi_square_grid(tls: TlsType) -> None:
        """
        Draws a 45° tilted grid with 4 turtles => 4 colors.

        :param tls: list of 4 chainable turtles

        :return: None
        """

# ======== TURTLE 6 =========

    @staticmethod
    def circles6(tls: TlsType) -> None:
        """
        Draws 6 circles (with 6 turtles) 'simultaneously' with each being 60° to the left of the last one.
        
        :param tls: list of 6 chainable turtles

        :return: None
        """

# ========= TURTLE UNDEFINED =========

    @staticmethod
    def duo_triforce() -> TlsType:
        """
        Draws a duo triforce (Zelda reference), triangles have corresponding colors.
        
        :return: list of 6 chainable turtles
        """

    @staticmethod
    def flower_infinite() -> TlsType:
        """
        Draws a customized flower: petals + circles number.

        :return: list of a chosen number of turtles
        """

# ========= NO TURTLES REQUIRED =========

    @staticmethod
    def change_shape() -> None:
        """
        Changes the shape of the turtle according to user input.

        :return: None
        """

    @classmethod
    def _list_designs(cls) -> PATTERNSType:
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