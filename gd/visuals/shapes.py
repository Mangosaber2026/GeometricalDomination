from numbers import Real
from typing import Final

import turtle_extension as tx
import uf


def side_tls_num(side: Real, tls_num: tx.ChainTurtle) -> None:
    """
    This function validates the parameters side and tls_num of all Shapes functions.

    :param side: real number

    :param tls_num: ChainTurtle instance
    
    :return: None
    """
    side_name: Final = "side"
    tls_num_name: Final = "tls_num"

    uf.ComboValidate(side, name=side_name)(uf.real_validate(), uf.Positive())
    uf.TypeValidate(tx.ChainTurtle)(tls_num, name=tls_num_name)

#* Contains predefined shapes which are used all throughout the software
@uf.cls_deco_superposition(staticmethod)
class Shapes:
#* ====== STAR OF DAVID ======
    def SOD(side, tls_num):

        side_tls_num(side, tls_num)

        for _ in range(6):
            (
                tls_num
                . pu()
                . fd(side)
                . pd()
                . rt(60)
            )
            for _ in range(3):
                tls_num.fd(side).rt(120)
            (
                tls_num
                . lt(60)
                . pu()
                . bk(side)
                . pd()
                . lt(60)
            )

#* [[Shapes#SOD]] with fill color
    def SOD_fill(side,tls_num):

        side_tls_num(side, tls_num)

        for _ in range(6):
            (
                tls_num
                . pu()
                . fd(side)
                . pd()
                . rt(60)
                . begin_fill()
            )
            for _ in range(3):
                tls_num.fd(side).rt(120)
            (
                tls_num
                . end_fill()
                . lt(60)
                . pu()
                . bk(side)
                . pd()
                . lt(60)
            )

#* ====== HEXAGON ======
    def hexagon(side, tls_num):

        side_tls_num(side, tls_num)
        (
            tls_num
            . pu()
            . fd(side)
            . pd()
            . lt(90)
            . circle(side,360,6)
        )

# * [[Shapes#hexagon]] with fill color
    def hexagon_fill(side, tls_num):

        side_tls_num(side, tls_num)

        tls_num.begin_fill()
        Shapes.hexagon(
            side = side,
            tls_num = tls_num,
        )
        tls_num.end_fill()

#* ====== TRIANGLE ======
    def triangle(side, tls_num):

        side_tls_num(side, tls_num)

        for _ in range(3):
            tls_num.fd(side).lt(120)

# * [[Shapes#triangle]] with fill color
    def triangle_fill(side, tls_num):

        side_tls_num(side, tls_num)

        tls_num.begin_fill()
        Shapes.triangle(
            side = side,
            tls_num = tls_num,
        )
        tls_num.end_fill()

#* Triangle starting in the middle of a side
    def triangle_half(side, tls_num):

        side_tls_num(side, tls_num)
        side_50 = uf.pct50(side)

        tls_num.fd(side_50).lt(120)

        for _ in range(2):
            tls_num.fd(side).lt(120)

        tls_num.fd(side_50)

#* ====== SQUARE ======
    def square(side, tls_num):

        side_tls_num(side, tls_num)

        for _ in range(4):
            tls_num.fd(side).lt(90)

#* [[Shapes#square]] with fill color
    def square_fill(side, tls_num):

        side_tls_num(side, tls_num)

        tls_num.begin_fill()
        Shapes.square(
            side = side,
            tls_num = tls_num,
        )
        tls_num.end_fill()

#* Square starting in the middle of a side
    def square_half(side, tls_num):

        side_tls_num(side, tls_num)
        side_50 = uf.pct50(side)

        tls_num.fd(side_50).lt(90)

        for _ in range(3):
            tls_num.fd(side).lt(90)

        tls_num.fd(side_50)

#* ====== RECTANGLE ======
    def rectangle(length, width, direction, tls_num):

        for item in (length, width):
            side_tls_num(item, tls_num)

        if direction not in (-1, 1):
            uf.ErrorDedent(ValueError)(f"""
                Function: Shapes.rectangle()
                Parameter direction must be either -1 or 1
                Expected: -1 or 1
                Received: {direction}
                """)

        turn = direction * 90
        for _ in range(2):
            (
                tls_num
                . fd(length)
                . lt(turn)
                . fd(width)
                . lt(turn)
            )

#* [[Shapes#rectangle]] with fill color
    def rectangle_fill(length, width, direction, tls_num):

        uf.TypeValidate(tx.ChainTurtle)(tls_num, name="tls_num")

        tls_num.begin_fill()
        Shapes.rectangle(
            length = length,
            width = width,
            direction = direction,
            tls_num = tls_num)
        tls_num.end_fill()

#* ====== HEXAFLOWER TRIANGLE VERSION ======
    def hexaflower_tri(length, tls_num):

        side_tls_num(length, tls_num)

        diagonal = (length*uf.sine(120))/uf.sine(30)

        for _ in range(6):
            (
                tls_num
                . fd(diagonal)
                . lt(150)
                . fd(length)
                . rt(120)
                . bk(length)

                .fd(length)
                .lt(60)
                .fd(length)
                .rt(30)
                .bk(diagonal)
            )

#* [[Shapes#hexaflower_tri]] with fill color
    def hexaflower_tri_fill(length, tls_num):

        side_tls_num(length, tls_num)

        tls_num.begin_fill()
        Shapes.hexaflower_tri(
            length = length,
            tls_num = tls_num,
        )
        tls_num.end_fill()

#* ====== HEXAFLOWER CIRCLE VERSION ======
    def hexa_flower(radius, tls_num):

        side_tls_num(radius, tls_num)

        for _ in range(6):
            (
                tls_num
                . circle(-radius,60)
                . rt(120)
                . circle(-radius,60)
                . rt(60)
            )

#* [[Shapes#hexa_flower]] with fill color
    def hexa_flower_fill(radius, tls_num):

        side_tls_num(radius, tls_num)

        tls_num.begin_fill()
        Shapes.hexa_flower(
            radius = radius,
            tls_num = tls_num,
        )
        tls_num.end_fill()

#* ====== LOTUS FLOWER ======
    def lotus_flower(radius, tls_num):

        side_tls_num(radius, tls_num)

        for n in range(2):
            Shapes.hexa_flower(
                radius = radius,
                tls_num = tls_num,
            )
            tls_num.lt((-1)**n*30)

#* [[Shapes#lotus_flower]] with fill color
    def lotus_flower_fill(radius, tls_num):

        side_tls_num(radius, tls_num)

        tls_num.begin_fill()
        Shapes.lotus_flower(
            radius = radius,
            tls_num = tls_num,
        )
        tls_num.end_fill()

#* ====== LINES ======
#* Draws evenly spaced lines in a circular pattern
    def lines(distance, lines_num, tls_num):

        uf.real_validate()(distance, name="distance")
        uf.ComboValidate(lines_num, name="lines_num")(uf.int_validate(), uf.Positive())
        uf.TypeValidate(tx.ChainTurtle)(tls_num, name="tls_num")

        angle = int(360/lines_num)

        for _ in range(lines_num):
            tls_num.fd(distance).bk(distance).lt(angle)

#* ====== CIRCLE ======
    def circle(radius, tls_num):

        side_tls_num(radius, tls_num)

        tls_num.circle(radius)

#* [[Shapes#circle]] with fill color
    def circle_filler(radius, tls_num):

        side_tls_num(radius, tls_num)

        tls_num.begin_fill().circle(radius).end_fill()

#* ====== POLYGON ======
#* Draws a regular polygon with an arbitrary number of sides
    def polygon(length, sides, tls_num):

        side_tls_num(length, tls_num)
        uf.ComboValidate(sides, name="sides")(uf.int_validate(), uf.Positive())

        radius = length / (2 * uf.sine(180 / sides))
        angle_to_right = (180-(180*(sides-2))/sides) / 2

        (
            tls_num
            . rt(angle_to_right)
            . circle(radius,360,sides)
            . lt(angle_to_right)
        )

#* [[Shapes#polygon]] with fill color
    def polygon_fill(length, sides, tls_num):

        side_tls_num(length, tls_num)
        uf.ComboValidate(sides, name="sides")(uf.int_validate(), uf.Positive())

        tls_num.begin_fill()
        Shapes.polygon(
            length = length,
            sides = sides,
            tls_num = tls_num,
        )
        tls_num.end_fill()

#* ===== SHAPES DICT =====
#* Creates and returns a dictionary with all [[Shapes]] available functions
    def list_shapes():
        return uf.classes_to_dict(Shapes)