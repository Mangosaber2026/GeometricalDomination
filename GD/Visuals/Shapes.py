from typing import Literal,  Final
from GD.TurtleHeart import ChainTurtle
from numbers import Real
import UF as uf


sine: Final = uf.sine
Positive: Final = uf.Positive

def side_tls_num(side, tls_num):
    side_name: Final[Literal["side"]] = "side"
    tls_num_name: Final[Literal["tls_num"]] = "tls_num"

    uf.ComboValidate(side, name=side_name)(uf.real_validate(), uf.Positive())
    uf.TypeValidate(ChainTurtle)(tls_num, name=tls_num_name)

@uf.cls_deco_superposition(staticmethod)
class Shapes:
# ====== STAR OF DAVID ======
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

# ====== STAR OF DAVID FILL ======
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

# ====== HEXAGON ======
    def hexagon_ft(side, tls_num):
        side_tls_num(side, tls_num)
        (
            tls_num
            . pu()
            . fd(side)
            . pd()
            . lt(90)
            . circle(side,360,6)
        )

# ====== TRIANGLE ======
    def triangle_ft(side, tls_num):
        side_tls_num(side, tls_num)

        for _ in range(3):
            tls_num.fd(side).lt(120)

    def triangle_fill(side, tls_num):
        side_tls_num(side, tls_num)

        tls_num.begin_fill()
        Shapes.triangle_ft(side,tls_num)
        tls_num.end_fill()

    def triangle_half(side: Real, tls_num: ChainTurtle):
        side_tls_num(side, tls_num)

        tls_num.fd(side/2).lt(120)
        for _ in range(2):
            tls_num.fd(side).lt(120)
        tls_num.fd(side/2)

# ====== SQUARE ======
    def square(side, tls_num):
        side_tls_num(side, tls_num)

        for _ in range(4):
            tls_num.fd(side).lt(90)

    def square_fill(side, tls_num):
        side_tls_num(side, tls_num)

        tls_num.begin_fill()
        Shapes.square(side,tls_num)
        tls_num.end_fill()

    def square_half(side, tls_num):
        side_tls_num(side, tls_num)

        tls_num.fd(side/2).lt(90)
        for _ in range(3):
            tls_num.fd(side).lt(90)
        tls_num.fd(side/2)

# ====== RECTANGLE ======
    def rectangle(length, width, direction, tls_num):

        for item, item_name in zip((length, width), ("length", "width")):
            uf.ComboValidate(item, name=item_name)(uf.real_validate(), uf.Positive())
        uf.TypeValidate(ChainTurtle)(tls_num, name="tls_num")

        if direction not in (-1, 1):
            uf.ErrorDedent(ValueError)(f"""
                Function: Shapes.rectangle()
                Parameter direction must be either -1 or 1
                Expected: -1 or 1
                Received: {direction}
                """)

        turn = direction * 90
        for _ in range(2):
            tls_num.fd(length).lt(turn).fd(width).lt(turn)

    def rectangle_fill(length, width, direction, tls_num):

        uf.TypeValidate(ChainTurtle)(tls_num, name="tls_num")

        tls_num.begin_fill()
        Shapes.rectangle(length,width,direction,tls_num)
        tls_num.end_fill()

# ====== HEXAFLOWER ======
    def hexaflower_tri(length, tls_num):
        side_tls_num(length, tls_num)

        diagonal = (length*sine(120))/sine(30)
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

# ====== LOTUS FLOWER ======
    def lotus_flower(radius, tls_num):
        side_tls_num(radius, tls_num)

        for n in range(2):
            Shapes.hexa_flower(radius,tls_num)
            tls_num.lt((-1)**n*30)

# ====== LINES ======
    def lines(distance, lines_num, tls_num):

        uf.real_validate()(distance, name="distance")
        uf.ComboValidate(lines_num, name="lines_num")(uf.int_validate(), uf.Positive())
        uf.TypeValidate(ChainTurtle)(tls_num, name="tls_num")

        angle = int(360/lines_num)

        for _ in range(lines_num):
            tls_num.fd(distance).bk(distance).lt(angle)

# ====== CIRCLE ======
    def circle_ft(radius, tls_num):
        side_tls_num(radius, tls_num)

        tls_num.circle(radius)

    def circle_filler(radius, tls_num):
        side_tls_num(radius, tls_num)

        tls_num.begin_fill().circle(radius).end_fill()

# ====== POLYGON ======
    def polygon(length, sides, tls_num):
        side_tls_num(length, tls_num)
        uf.ComboValidate(sides, name="sides")(uf.int_validate(), uf.Positive())

        radius = length / (2 * sine(180 / sides))
        angle_to_right = (180-(180*(sides-2))/sides) / 2

        (
            tls_num
            . rt(angle_to_right)
            . circle(radius,360,sides)
            . lt(angle_to_right)
        )

    def polygon_fill(length, sides, tls_num):
        side_tls_num(length, tls_num)
        uf.ComboValidate(sides, name="sides")(uf.int_validate(), uf.Positive())

        tls_num.begin_fill()
        Shapes.polygon(length,sides,tls_num)
        tls_num.end_fill()

# ===== SHAPES DICT =====
    def _list_shapes():
        return uf.classes_to_dict(Shapes)