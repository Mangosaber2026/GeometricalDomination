# ⚓ Anchor for this module: [[shapes-anchor|shapes.py]] 

lazy import numbers as num
lazy import typing as tp

lazy import turtle_extension as tx
lazy import uf

#* 📝 Type for any real number
type RealType = float | int | num.Real

def side_tls_num(side: RealType, tls_num: tx.ChainTurtle) -> None:
    """
    This function validates the parameters side and tls_num of all Shapes functions.

    :param side: RealType number

    :param tls_num: ChainTurtle instance
    
    :return: None
    """
    side_name: tp.Final = "side"
    tls_num_name: tp.Final = "tls_num"

    uf.Positive()(value=side, name=side_name)
    uf.TypeValidate(expected=tx.ChainTurtle)(value=tls_num, name=tls_num_name)


# ⚓ Shapes anchor: [[Shapes-anchor|class Shapes]] 
#* 📝 Contains predefined shapes which are used all throughout the software
class Shapes:

    # ⚓ SOD anchor: [[Shapes-SOD-anchor|SOD()]] 
    #* 📝 ====== STAR OF DAVID ======
    @staticmethod
    def SOD(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)

        for _ in range(6):
            (
                tls_num
                . penup()
                . forward(side)
                . pendown()
                . right(60)
            )
            for _ in range(3):
                tls_num.forward(side).right(120)
            (
                tls_num
                . left(60)
                . penup()
                . backward(side)
                . pendown()
                . left(60)
            )


    # ⚓ SOD_fill anchor: [[Shapes-SOD-fill-anchor|SOD_fill()]] 
    #* 📝 [[#Shapes-SOD-anchor|SOD()]] with fill color
    @staticmethod
    def SOD_fill(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)

        for _ in range(6):
            (
                tls_num
                . penup()
                . forward(side)
                . pendown()
                . right(60)
                . begin_fill()
            )
            for _ in range(3):
                tls_num.forward(side).right(120)
            (
                tls_num
                . end_fill()
                . left(60)
                . penup()
                . backward(side)
                . pendown()
                . left(60)
            )


    # ⚓ hexagon anchor: [[Shapes-hexagon-anchor|hexagon()]] 
    #* 📝 ====== HEXAGON ======
    @staticmethod
    def hexagon(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)
        (
            tls_num
            . penup()
            . forward(side)
            . pendown()
            . left(90)
            . circle(side,360,6)
        )


    # ⚓ hexagon_fill anchor: [[Shapes-hexagon-fill-anchor|hexagon_fill()]] 
    #* 📝 [[#Shapes-hexagon-anchor|hexagon()]]  with fill color
    @staticmethod
    def hexagon_fill(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)

        tls_num.begin_fill()
        Shapes.hexagon(
            side = side,
            tls_num = tls_num,
        )
        tls_num.end_fill()


    # ⚓ triangle anchor: [[Shapes-triangle-anchor|triangle()]] 
    #* 📝 ====== TRIANGLE ======
    @staticmethod
    def triangle(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)

        for _ in range(3):
            tls_num.forward(side).left(120)


    # ⚓ triangle_fill anchor: [[Shapes-triangle-fill-anchor|triangle_fill()]] 
    #* 📝 [[#Shapes-triangle-anchor|triangle()]]  with fill color
    @staticmethod
    def triangle_fill(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)

        tls_num.begin_fill()
        Shapes.triangle(
            side = side,
            tls_num = tls_num,
        )
        tls_num.end_fill()


    # ⚓ triangle_half anchor: [[Shapes-triangle-half-anchor|triangle_half()]] 
    #* 📝 Triangle starting in the middle of a side
    @staticmethod
    def triangle_half(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)
        side_50 = uf.pct50(side)

        tls_num.forward(side_50).left(120)

        for _ in range(2):
            tls_num.forward(side).left(120)

        tls_num.forward(side_50)


    # ⚓ square anchor: [[Shapes-square-anchor|square()]] 
    #* 📝 ====== SQUARE ======
    @staticmethod
    def square(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)

        for _ in range(4):
            tls_num.forward(side).left(90)


    # ⚓ square_fill anchor: [[Shapes-square-fill-anchor|square_fill()]] 
    #* 📝 [[#Shapes-square-anchor|square()]]  with fill color
    @staticmethod
    def square_fill(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)

        tls_num.begin_fill()
        Shapes.square(
            side = side,
            tls_num = tls_num,
        )
        tls_num.end_fill()


    # ⚓ square_half anchor: [[Shapes-square-half-anchor|square_half()]] 
    #* 📝 Square starting in the middle of a side
    @staticmethod
    def square_half(side, tls_num: tx.ChainTurtle):

        side_tls_num(side, tls_num)
        side_50 = uf.pct50(side)

        tls_num.forward(side_50).left(90)

        for _ in range(3):
            tls_num.forward(side).left(90)

        tls_num.forward(side_50)


    # ⚓ rectangle anchor: [[Shapes-rectangle-anchor|rectangle()]] 
    #* 📝 ====== RECTANGLE ======
    @staticmethod
    def rectangle(length, width, direction, tls_num: tx.ChainTurtle):

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
                . forward(length)
                . left(turn)
                . forward(width)
                . left(turn)
            )


    # ⚓ rectangle_fill anchor: [[Shapes-rectangle-fill-anchor|rectangle_fill()]] 
    #* 📝 [[#Shapes-rectangle-anchor|rectangle()]]  with fill color
    @staticmethod
    def rectangle_fill(length, width, direction, tls_num: tx.ChainTurtle):

        uf.TypeValidate(tx.ChainTurtle)(tls_num, name="tls_num")

        tls_num.begin_fill()
        Shapes.rectangle(
            length = length,
            width = width,
            direction = direction,
            tls_num = tls_num)
        tls_num.end_fill()


    # ⚓ hexaflower_tri anchor: [[Shapes-hexaflower-tri-anchor|hexaflower_tri()]] 
    #* 📝 ====== HEXAFLOWER TRIANGLE VERSION ======
    @staticmethod
    def hexaflower_tri(length, tls_num: tx.ChainTurtle):

        side_tls_num(length, tls_num)

        diagonal = (length*uf.sine(120))/uf.sine(30)

        for _ in range(6):
            (
                tls_num
                . forward(diagonal)
                . left(150)
                . forward(length)
                . right(120)
                . backward(length)

                . forward(length)
                . lt(60)
                . forward(length)
                . right(30)
                . backward(diagonal)
            )


    # ⚓ hexaflower_tri_fill anchor: [[Shapes-hexaflower-tri-fill-anchor|hexaflower_tri_fill()]] 
    #* 📝 [[#Shapes-hexaflower-tri-anchor|hexaflower_tri()]]  with fill color
    @staticmethod
    def hexaflower_tri_fill(length, tls_num: tx.ChainTurtle):

        side_tls_num(length, tls_num)

        tls_num.begin_fill()
        Shapes.hexaflower_tri(
            length = length,
            tls_num = tls_num,
        )
        tls_num.end_fill()


    # ⚓ hexa_flower anchor: [[Shapes-hexa-flower-anchor|hexa_flower()]] 
    #* 📝 ====== HEXAFLOWER CIRCLE VERSION ======
    @staticmethod
    def hexa_flower(radius, tls_num: tx.ChainTurtle):

        side_tls_num(radius, tls_num)

        for _ in range(6):
            (
                tls_num
                . circle(-radius,60)
                . right(120)
                . circle(-radius,60)
                . right(60)
            )


    # ⚓ hexa_flower_fill anchor: [[Shapes-hexa-flower-fill-anchor|hexa_flower_fill()]] 
    #* 📝 [[#Shapes-hexa-flower-anchor|hexa_flower()]] with fill color
    @staticmethod
    def hexa_flower_fill(radius, tls_num: tx.ChainTurtle):

        side_tls_num(radius, tls_num)

        tls_num.begin_fill()
        Shapes.hexa_flower(
            radius = radius,
            tls_num = tls_num,
        )
        tls_num.end_fill()


    # ⚓ lotus_flower anchor: [[Shapes-lotus-flower-anchor|lotus_flower()]] 
    #* 📝 ====== LOTUS FLOWER ======
    @staticmethod
    def lotus_flower(radius, tls_num: tx.ChainTurtle):

        side_tls_num(radius, tls_num)

        for n in range(2):
            Shapes.hexa_flower(
                radius = radius,
                tls_num = tls_num,
            )
            tls_num.left((-1)**n*30)


    # ⚓ lotus_flower_fill anchor: [[Shapes-lotus-flower-fill-anchor|lotus_flower_fill()]] 
    #* 📝 [[#Shapes-lotus-flower-anchor|lotus_flower()]] with fill color
    @staticmethod
    def lotus_flower_fill(radius, tls_num: tx.ChainTurtle):

        side_tls_num(radius, tls_num)

        tls_num.begin_fill()
        Shapes.lotus_flower(
            radius = radius,
            tls_num = tls_num,
        )
        tls_num.end_fill()


    # ⚓ lines anchor: [[Shapes-lines-anchor|lines()]] 
    #* 📝 ====== LINES ======
    #* 📝 Draws evenly spaced lines in a circular pattern
    @staticmethod
    def lines(distance, lines_num, tls_num: tx.ChainTurtle):

        uf.real_validate()(distance, name="distance")
        uf.ComboValidate(lines_num, name="lines_num")(uf.int_validate(), uf.Positive())
        uf.TypeValidate(tx.ChainTurtle)(tls_num, name="tls_num")

        angle = int(360/lines_num)

        for _ in range(lines_num):
            tls_num.forward(distance).backward(distance).left(angle)


    # ⚓ circle anchor: [[Shapes-circle-anchor|circle()]] 
    #* 📝 ====== CIRCLE ======
    @staticmethod
    def circle(radius, tls_num: tx.ChainTurtle):

        side_tls_num(radius, tls_num)

        tls_num.circle(radius)


    # ⚓ circle_filler anchor: [[Shapes-circle-filler-anchor|circle_filler()]] 
    #* 📝 [[#Shapes-circle-anchor|circle()]] with fill color
    @staticmethod
    def circle_filler(radius, tls_num: tx.ChainTurtle):

        side_tls_num(radius, tls_num)

        tls_num.begin_fill().circle(radius).end_fill()


    # ⚓ polygon anchor: [[Shapes-polygon-anchor|polygon()]] 
    #* 📝 ====== POLYGON ======
    #* 📝 Draws a regular polygon with an arbitrary number of sides
    @staticmethod
    def polygon(length, sides, tls_num: tx.ChainTurtle):

        side_tls_num(length, tls_num)
        uf.ComboValidate(sides, name="sides")(uf.int_validate(), uf.Positive())

        radius = length / (2 * uf.sine(180 / sides))
        angle_to_right = (180-(180*(sides-2))/sides) / 2

        (
            tls_num
            . right(angle_to_right)
            . circle(radius,360,sides)
            . left(angle_to_right)
        )


    # ⚓ polygon_fill anchor: [[Shapes-polygon-fill-anchor|polygon_fill()]] 
    #* 📝 [[#Shapes-polygon-anchor|polygon()]] with fill color
    @staticmethod
    def polygon_fill(length, sides, tls_num: tx.ChainTurtle):

        side_tls_num(length, tls_num)
        uf.ComboValidate(sides, name="sides")(uf.int_validate(), uf.Positive())

        tls_num.begin_fill()
        Shapes.polygon(
            length = length,
            sides = sides,
            tls_num = tls_num,
        )
        tls_num.end_fill()


    # ⚓ list_shapes anchor: [[Shapes-list-shapes-anchor|list_shapes()]] 
    #* 📝 ===== SHAPES DICT =====
    #* 📝 Creates and returns a dictionary with all [[#Shapes-anchor|Shapes]] available functions
    @staticmethod
    def list_shapes():
        return uf.classes_to_dict(Shapes)