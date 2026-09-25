from typing import Literal
from ..TurtleSkeleton import ChainTurtle
from .HelperFunctions import sine
from .DecoratorArchive import cls_deco_superposition
from .TypingVariables import Real
from .ClassToDict import classes_to_dict
from .Validators.FctInputValidators import validation_deco

class ShapesMeta(type):
    def __new__(mcls, name, bases, namespace) -> type:
        for func_name, func in namespace.items():
            if callable(func) and not func_name.startswith("_"):
                namespace[func_name] = validation_deco(func)

        return super().__new__(mcls, name, bases, namespace)

@cls_deco_superposition(staticmethod)
class Shapes(metaclass=ShapesMeta):
# ====== STAR OF DAVID ======
    def SOD(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a star of David
        :param side: length of star of David
        :param tls_num: a given ChainTurtle
        """
        for _ in range(6):
            tls_num.pu().fd(side).pd().rt(60)
            for _ in range(3): tls_num.fd(side).rt(120)
            tls_num.lt(60).pu().bk(side).pd().lt(60)
# ====== STAR OF DAVID FILL ======
    def SOD_fill(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a filled star of David
        :param side: length of star of David
        :param tls_num: a given ChainTurtle
        """
        for _ in range(6):
            tls_num.pu().fd(side).pd().rt(60).begin_fill()
            for _ in range(3): tls_num.fd(side).rt(120)
            tls_num.end_fill().lt(60).pu().bk(side).pd().lt(60)
# ====== HEXAGON ======
    def hexagon_ft(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a hexagon
        :param side: length of hexagon
        :param tls_num: a given ChainTurtle
        """
        tls_num.pu().fd(side).pd().lt(90).circle(side,360,6)
# ====== TRIANGLE ======
    def triangle_ft(side: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a triangle
        :param side: length of triangle
        :param tls_num: a given ChainTurtle
        """
        for _ in range(3): tls_num.fd(side).lt(120)

    def triangle_fill(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a filled triangle
        :param side: length of triangle
        :param tls_num: a given ChainTurtle
        """
        tls_num.begin_fill(); Shapes.triangle_ft(side,tls_num); tls_num.end_fill()

    def triangle_half(side: Real, tls_num: ChainTurtle) -> None:
        """
        Draws a triangle from the middle of a side
        :param side: length of triangle
        :param tls_num: a given ChainTurtle
        """
        tls_num.fd(side/2).lt(120)
        for _ in range(2): tls_num.fd(side).lt(120)
        tls_num.fd(side/2)
# ====== SQUARE ======
    def square(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a square
        :param side: length of square
        :param tls_num: a given ChainTurtle
        """
        for _ in range(4): tls_num.fd(side).lt(90)

    def square_fill(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a filled square
        :param side: length of square
        :param tls_num: a given ChainTurtle
        """
        tls_num.begin_fill(); Shapes.square(side,tls_num); tls_num.end_fill()

    def square_half(side: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a square from the middle of a side
        :param side: length of square
        :param tls_num: a given ChainTurtle
        """
        tls_num.fd(side/2).lt(90)
        for _ in range(3): tls_num.fd(side).lt(90)
        tls_num.fd(side/2)
# ====== RECTANGLE ======

    def rectangle(length: Real,width: Real,direction: Literal[-1,1],tls_num: ChainTurtle) -> None:
        """
        Draws a rectangle
        :param length: longer side
        :param width: shorter side
        :param direction: -1 draws to the right, 1 draws to the left
        :param tls_num: a given ChainTurtle
        """
        turn = direction * 90
        for _ in range(2): tls_num.fd(length).lt(turn).fd(width).lt(turn)

    def rectangle_fill(length: Real,width: Real,direction: Literal[-1,1],tls_num: ChainTurtle) -> None:
        """
        Draws a filled rectangle
        :param length: longer side
        :param width: shorter side
        :param direction: -1 draws to the right, 1 draws to the left
        :param tls_num: a given ChainTurtle
        """
        tls_num.begin_fill(); Shapes.rectangle(length,width,direction,tls_num); tls_num.end_fill()
# ====== HEXAFLOWER ======

    def hexaflower_tri(length: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a 12 triangled flower
        :param length: side length of triangles
        :param tls_num: a given ChainTurtle
        """
        diagonal = (length*sine(120))/sine(30)
        for _ in range(6):
            tls_num.fd(diagonal).lt(150).fd(length).rt(120).bk(length)
            tls_num.fd(length).lt(60).fd(length).rt(30).bk(diagonal)

    def hexa_flower(radius: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a 6 petalled flower
        :param radius: radius of flower
        :param tls_num: a given ChainTurtle
        """
        for _ in range(6): tls_num.circle(-radius,60).rt(120).circle(-radius,60).rt(60)
# ====== LOTUS FLOWER ======

    def lotus_flower(radius: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a 12 petalled flower
        :param radius: radius of flower
        :param tls_num: a given ChainTurtle
        """
        for n in range(2): Shapes.hexa_flower(radius,tls_num); tls_num.lt((-1)**n*30)
# ====== LINES ======

    def lines(distance: Real,lines_num: int,tls_num: ChainTurtle) -> None:
        """
        Draws a chosen number of lines, evenly spaced apart

        :param distance: length of lines
        :param lines_num: number of lines
        :param tls_num: a given ChainTurtle
        """
        angle = int(360/lines_num)
        for _ in range(lines_num): tls_num.fd(distance).bk(distance).lt(angle)
# ====== CIRCLE ======

    def circle_ft(radius: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a circle with given radius and turtle
        :param radius: radius of circle
        :param tls_num: a given ChainTurtle
        """
        tls_num.circle(radius)

    def circle_filler(radius: Real,tls_num: ChainTurtle) -> None:
        """
        Draws a filled circle with given radius and turtle
        :param radius: radius of circle
        :param tls_num: a given ChainTurtle
        """
        tls_num.begin_fill().circle(radius).end_fill()
# ====== POLYGON ======

    def polygon(length: Real,sides: int,tls_num: ChainTurtle) -> None:
        """
        Draws a polygon with given length and sides
        :param length: length of polygon
        :param sides: number of sides
        :param tls_num: a given ChainTurtle
        """
        radius = length / (2 * sine(180 / sides)); angle_to_right = (180-(180*(sides-2))/sides) / 2
        tls_num.rt(angle_to_right).circle(radius,360,sides).lt(angle_to_right)

    def polygon_fill(length: Real,sides: int,tls_num: ChainTurtle) -> None:
        """
        Draws a filled polygon with given length and sides
        :param length: length of polygon
        :param sides: number of sides
        :param tls_num: a given ChainTurtle
        """
        tls_num.begin_fill(); Shapes.polygon(length,sides,tls_num); tls_num.end_fill()

    def _list_shapes() -> dict:
        """
        Creates a dictionary with all Shapes and returns it
        :return: dictionary
        """
        return classes_to_dict(Shapes)