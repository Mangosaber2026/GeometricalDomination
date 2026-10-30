"""
This module contains the Shapes class which provides premade drawing functions with ChainTurtle().
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import numbers as num  # noqa: I001
import typing as tp

import turtle_extension as tx
import uf


#* 📝 Type for any real number
type RealType = float | int | num.Real


@uf.cls_deco_superposition(staticmethod)
class Shapes:
    """
    This class provides premade shape drawing functions with ChainTurtle().
    """

    @staticmethod
    def SOD(side: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a star of David

        :param side: length of star of David

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def SOD_fill(side: RealType,tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled star of David

        :param side: length of star of David

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def hexagon(side: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a hexagon

        :param side: length of hexagon

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def hexagon_fill(side: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled hexagon

        :param side: length of hexagon

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def triangle(side: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a triangle

        :param side: length of triangle

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def triangle_fill(side: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled triangle

        :param side: length of triangle

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def triangle_half(side: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a triangle from the middle of a side

        :param side: length of triangle

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def square(side: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a square

        :param side: length of square

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def square_fill(side: RealType,tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled square

        :param side: length of square

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def square_half(side: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a square from the middle of a side

        :param side: length of square

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def rectangle(length: RealType,
                  width: RealType,
                  direction: tp.Literal[-1, 1],
                  tls_num: tx.ChainTurtle) -> None:
        """
        Draws a rectangle

        :param length: longer side

        :param width: shorter side

        :param direction: -1 draws to the right, 1 draws to the left

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def rectangle_fill(length: RealType,
                       width: RealType,
                       direction: tp.Literal[-1,1],
                       tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled rectangle

        :param length: longer side

        :param width: shorter side

        :param direction: -1 draws to the right, 1 draws to the left

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def hexaflower_tri(length: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a 12 triangled flower

        :param length: side length of triangles

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def hexaflower_tri_fill(length: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled 12 triangled flower

        :param length: side length of triangles

        :param tls_num: a given ChainTurtle

        :return:
        """


    @staticmethod
    def hexa_flower(radius: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a 6 petalled flower

        :param radius: radius of flower

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def hexa_flower_fill(radius: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled 6 petalled flower

        :param radius: radius of flower

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def lotus_flower(radius: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a 12 petalled flower

        :param radius: radius of flower

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def lotus_flower_fill(radius: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled 12 petalled flower

        :param radius: radius of flower

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def lines(distance: RealType, lines_num: int, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a chosen number of lines, evenly spaced apart

        :param distance: length of lines

        :param lines_num: number of lines

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def circle(radius: RealType, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a circle with given radius and turtle

        :param radius: radius of circle

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def circle_filler(radius: RealType, tls_num) -> None:
        """
        Draws a filled circle with given radius and turtle

        :param radius: radius of circle

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def polygon(length: RealType, sides: int, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a polygon with given length and sides

        :param length: length of polygon

        :param sides: number of sides

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def polygon_fill(length: RealType, sides: int, tls_num: tx.ChainTurtle) -> None:
        """
        Draws a filled polygon with given length and sides

        :param length: length of polygon

        :param sides: number of sides

        :param tls_num: a given ChainTurtle

        :return: None
        """


    @staticmethod
    def list_shapes() -> dict:
        """
        Creates a dictionary with all Shapes functions and returns it
        
        :return: dictionary mapping function name to function
        """