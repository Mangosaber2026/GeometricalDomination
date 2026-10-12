"""
This module contains the Shapes class which provides premade drawing functions with ChainTurtle().
"""

import UF as uf
from typing import Final, Literal
from .TurtleHeart import ChainTurtle
from numbers import Real


Positive: Final = uf.Positive

@uf.cls_deco_superposition(staticmethod)
class Shapes:
    """
    This class provides premade shape drawing functions with ChainTurtle().
    """
    def SOD(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a star of David
        :param side: length of star of David
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def SOD_fill(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a filled star of David
        :param side: length of star of David
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def hexagon_ft(side: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a hexagon
        :param side: length of hexagon
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def triangle_ft(side: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a triangle
        :param side: length of triangle
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def triangle_fill(side: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a filled triangle
        :param side: length of triangle
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def triangle_half(side: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a triangle from the middle of a side
        :param side: length of triangle
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def square(side: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a square
        :param side: length of square
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def square_fill(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a filled square
        :param side: length of square
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def square_half(side: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a square from the middle of a side
        :param side: length of square
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def rectangle(length: Real,
                  width: Real,
                  direction: Literal[-1, 1],
                  tls_num: ChainTurtle) -> None:
        """
        Draws a rectangle
        :param length: longer side
        :param width: shorter side
        :param direction: -1 draws to the right, 1 draws to the left
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def rectangle_fill(length: Real,
                       width: Real,
                       direction: Literal[-1,1],
                       tls_num: ChainTurtle) -> None:
        """
        Draws a filled rectangle
        :param length: longer side
        :param width: shorter side
        :param direction: -1 draws to the right, 1 draws to the left
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def hexaflower_tri(length: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a 12 triangled flower
        :param length: side length of triangles
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def hexa_flower(radius: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a 6 petalled flower
        :param radius: radius of flower
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def lotus_flower(radius: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a 12 petalled flower
        :param radius: radius of flower
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def lines(distance: Real, lines_num: int, tls_num: ChainTurtle) -> None:
        """
        Draws a chosen number of lines, evenly spaced apart

        :param distance: length of lines
        :param lines_num: number of lines
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def circle_ft(radius: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a circle with given radius and turtle
        :param radius: radius of circle
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def circle_filler(radius: Real, tls_num) -> None:
        """
        Draws a filled circle with given radius and turtle
        :param radius: radius of circle
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def polygon(length: Real, sides: int, tls_num: ChainTurtle) -> None:
        """
        Draws a polygon with given length and sides
        :param length: length of polygon
        :param sides: number of sides
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def polygon_fill(length: Real, sides: int, tls_num: ChainTurtle) -> None:
        """
        Draws a filled polygon with given length and sides
        :param length: length of polygon
        :param sides: number of sides
        :param tls_num: a given ChainTurtle
        :return: None
        """
        ...

    def _list_shapes() -> dict:
        """
        Creates a dictionary with all Shapes functions and returns it
        :return: dictionary mapping function name to function
        """
        ...