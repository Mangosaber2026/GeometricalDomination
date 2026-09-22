from .GlobalFunctions import SU, tls_color
from .GlobalVariables import UV
from .Shapes_Dictionary import Shapes
from .TurtleSkeleton import ChainTurtle
from math import pi, sqrt, degrees, asin
from .UniversalFunctions.GetVariable import get_num
from .UniversalFunctions.HelperFunctions import helper, sine, range_f
from .UniversalFunctions.StringCheck import get_str
from .UniversalFunctions.ClassToDict import classes_to_dict
from collections.abc import Callable
from typing import TypeAlias

designs_dict: TypeAlias = dict[str, Callable[[list[ChainTurtle]|None], list[ChainTurtle]]]

def turtles(amount: int):
    """
    DECORATOR:
    Takes a given number of turtles, gets their colors from the user and executes the function
    :param amount: number of turtles > 0
    """
    if not isinstance(amount, int):
        raise TypeError("Number of turtles must be an integer > 0")
    elif amount <= 0:
        raise ValueError("Number of turtles must be greater than 0!!!")
    def decorator(func):
        def wrapper():
            tls: list[ChainTurtle] = tls_color(tl_num=amount)
            func(tls)
            SU(); return tls
        return wrapper
    return decorator

def designs_decorator(cls):
    for class_name, design_class in vars(cls).items():
        if isinstance(design_class, type) and class_name.startswith("Turtle"):
            amount = design_class.TURTLE_COUNT

            for func_name, func in vars(design_class).items():
                if callable(func):
                    setattr(design_class, func_name, staticmethod(turtles(amount)(func)))

    return cls

class DesignsMeta(type):
    def __getattr__(cls, func):
        for class_name, category in vars(cls).items():
            if (
                isinstance(category, type)
                and class_name.startswith("Turtle")
            ):
                function = getattr(category, func, None)

                if callable(function):
                    return function

        raise AttributeError(f"{cls.__name__} has no attribute {func!r}")

@designs_decorator
class Designs(metaclass=DesignsMeta):
    class TurtleOne:
        TURTLE_COUNT = 1

        def hexaflower(tls: list[ChainTurtle]) -> None:
            """
            Draws flowers with 12 triangle petals in a horizontal + vertical pattern
            :param tls: list of 1 chainable turtle
            """
            length: float | int = helper.length_float()
            flower_num: int = helper.object_num()
            row_count: int = helper.row_pair()

            diagonal = (length * sine(120)) / sine(30)
            height = sqrt(diagonal ** 2 - (diagonal / 2) ** 2)
            length_total = diagonal * flower_num * 2
            for _ in range(row_count):
                for row in range(2):
                    for _ in range(flower_num - row):
                        Shapes.hexaflower_tri(length, tls[0])
                        tls[0].bk_inv(diagonal * 2)

                    tls[0].fd_inv(length_total - diagonal).lt(90).fd_inv(height * 2).rt(90)

        def star_of_david(tls: list[ChainTurtle]) -> None:
            """
            Draws a star of David
            :param tls: list of 1 chainable turtle
            """
            Shapes.SOD(helper.length_float(), tls[0])

        def diamond_pattern(tls: list[ChainTurtle]) -> None:
            """
            Draws a diamond pattern
            :param tls: list of 1 chainable turtle
            """
            length: float|int = helper.length_float()
            diamond_num: int = helper.object_num()
            row_count: int = helper.row_num()

            outer_side = (length*sine(120))*2; height = sqrt(length**2 - (outer_side/2)**2)
            for _ in range(row_count):
                for _ in range(diamond_num):
                    Shapes.SOD(length,tls[0]); tls[0].pu().bk((length+height)*2).pd()

                tls[0].pu().fd((length+height)*diamond_num*2).lt(90).fd(outer_side).rt(90)

        def hidden_sds(tls: list[ChainTurtle]) -> None:
            """
            Draws stars of David in the same orientation (1 turtle)
            :param tls: list of 1 chainable turtle
            """
            length: float|int = helper.length_float(); star_count: int = helper.object_num()
            for _ in range(star_count):
                Shapes.SOD(length,tls[0]); length = (length * sine(30))/sine(120)

        def gd_reference(tls: list[ChainTurtle]) -> None:
            """
            Draws a square icon that resembles a GD icon
            :param tls: list of 1 chainable turtle
            """
            length: float|int = helper.length_float()

            diagonal = (length*sine(120))/sine(30); tls[0].lt(30)
            for _ in range(6):
                tls[0].begin_fill().fd(diagonal).lt(150).fd(length).rt(120).bk(length).end_fill()
                tls[0].fd(length).lt(120).fd(length).rt(60).bk(diagonal)

        def tri_wheel(tls: list[ChainTurtle]) -> None:
            """
            Draws a wheel made with triangles on the sides
            :param tls: list of 1 chainable turtle
            """
            length: float|int = helper.length_float()

            diagonal = (length*sine(120))/sine(30); tls[0].width(3)
            for _ in range(12):
                tls[0].begin_fill().fd(diagonal).lt(150).fd(length).rt(120).bk(length).end_fill()
                tls[0].fd(length).lt(60).fd(length).rt(60).bk(diagonal)

        def lotus_pattern(tls: list[ChainTurtle]) -> None:
            """
            Draws a lotus pattern (12 petals)
            :param tls: list of 1 chainable turtle
            """
            radius: float | int = helper.radius_float()
            lotuses: int = helper.object_num()
            rows: int = helper.row_num()

            for _ in range(rows):
                for _ in range(lotuses):
                    Shapes.lotus_flower(radius, tls[0]); tls[0].bk_inv(radius * 2)

                tls[0].fd_inv(lotuses * radius * 2).lt(90).fd_inv(radius * 2).rt(90)

    class TurtleTwo:
        TURTLE_COUNT = 2

        def duo_spiral(tls: list[ChainTurtle]) -> None:
            """
            Draws 2 overlapping spirals, one to the right and one to the left
            :param tls: list of 2 chainable turtles
            """
            for i in range(500):
                tls[0].fd(i).rt(91); tls[1].fd(i).lt(91); SU()

        def squares8(tls: list[ChainTurtle]) -> None:
            """
            Draws 4 squares on each corner, with 4 squares tilted by 45° in between them + square pattern in between
            :param tls: list of 2 chainable turtles
            """
            length: float | int = helper.length_float()
            interval: float | int = helper.intervals_f()
            diameter, diameter_half = helper.diameter_sq(length)

            tls[0].teleport(diameter_half, diameter_half)
            tls[1].teleport(0, length / 2).lt(45)
            for i, t in enumerate(tls):
                for _ in range(4):
                    Shapes.square_fill(length, t)
                    t.rt(90).fd_inv(diameter / (i + 1))

            tls[0].teleport(0, 0).seth(180)
            tls[1].teleport(0, 0).lt(90)

            for c in range_f(0, length + 1, interval):
                tls[0].setpos(c / 2, c / 2)
                tls[1].setpos((sqrt(2) * c) / 2, 0)
                Shapes.square(c, tls[0])
                Shapes.square(c, tls[1])

            tls[0].setpos(0, 0).rt(135)
            tls[1].home()
            for t in tls:
                Shapes.lines(length * 1.5, 4, t)

        def tri_hexaflower(tls: list[ChainTurtle]) -> None:
            """
            Draws flowers with 12 triangle petals with lines in the middle in a horizontal + vertical pattern
            :param tls: list of 2 chainable turtles
            """
            length: float | int = helper.length_float()
            flower_num: int = helper.object_num()
            row_count: int = helper.row_pair()

            diagonal = (length * sine(120)) / sine(30)
            height = sqrt(diagonal ** 2 - (diagonal / 2) ** 2)
            length_total = diagonal * flower_num * 2

            for _ in range(row_count):
                for row in range(2):
                    for _ in range(flower_num - row):
                        tls[1].lt(30)
                        Shapes.lines(length * 2, 6, tls[1])
                        tls[1].rt(30)
                        Shapes.hexaflower_tri(length, tls[0])
                        for t in tls: t.bk_inv(diagonal * 2)
                    for t in tls:
                        t.fd_inv(length_total - diagonal).lt(90).fd_inv(height * 2).rt(90)

        def sd_pattern(tls: list[ChainTurtle]) -> None:
            """
            Draws stars of David in a horizontal + vertical pattern
            :param tls: list of 2 chainable turtles
            """
            length: float | int = helper.length_float()
            star_num: int = helper.object_num()
            row_count: int = helper.row_pair()

            outer_side = (length * sine(120)) / sine(30)
            height = sqrt(length ** 2 - (outer_side / 2) ** 2)
            side_2 = (length * sine(30)) / sine(120)
            for _ in range(row_count):
                for row in range(1, 3):
                    for a in range(star_num):
                        Shapes.SOD_fill(length, tls[0])
                        tls[1].lt(30)
                        Shapes.SOD_fill(side_2, tls[1])
                        tls[1].rt(30)
                        for b in range(2):
                            tls[b].pu().bk((length + height) * 2).pd()
                    for t in range(2):
                        tls[t].pu().fd((length + height) * (star_num * 2 + (-1) ** row)).lt(90).fd(outer_side * 1.5).rt(90)

        def sd_spiral(tls: list[ChainTurtle]) -> None:
            """
            Draws stars of David in a spiral pattern inside a main star with 2 turtles
            :param tls: list of 2 chainable turtles
            """
            length: float | int = helper.length_float()
            pairs_count: int = get_num(int, "How many pairs of stars?", MIN=1)
            tls[1].lt(30)
            for _ in range(pairs_count):
                for t in tls:
                    Shapes.SOD(length, t)
                    length = (length * sine(30)) / sine(120)
                    t.lt(60)

        def sd_triflower(tls: list[ChainTurtle]) -> None:
            """
            Draws three 6 petalled flowers in triangular shape in a star of David in an external structure
            :param tls: list of 2 chainable turtles
            """
            radius: float | int = helper.radius_float()

            height = sqrt(radius ** 2 - (radius / 2) ** 2)
            side_c = sqrt(radius ** 2 + (radius * 2) ** 2 + radius * (radius * 2))
            angle_b = degrees(asin(((radius * 2) * sine(120)) / side_c))
            angle_a = 180 - (angle_b + 120)
            tls[0].rt(30)

            for _ in range(3):
                Shapes.hexa_flower(radius, tls[0])
                tls[0].lt(60).circle(radius, 60)

            tls[1].teleport(0, -height)
            Shapes.triangle_half(radius * 5, tls[1])
            tls[1].teleport(0, height * 2).lt(180)
            Shapes.triangle_half(radius * 4, tls[1])
            tls[0].teleport(-radius * 2, height * 2).seth(180).lt(180 - (60 + angle_b))

            for _ in range(3):
                tls[0].fd(side_c).lt(180 - (angle_a * 2 + 60)).fd(side_c).lt(180 - (angle_b * 2 + 60))

        def hexaflower_sd(tls: list[ChainTurtle]) -> None:
            """
            Draws six 6 petalled flowers in a hexagon pattern, with lines in between the petals, all inside a star of David
            :param tls: list of 2 chainable turtles
            """
            radius: float | int = helper.radius_float()
            tls[0].lt(30)

            for _ in range(6):
                Shapes.hexa_flower(radius, tls[0])
                tls[0].circle(radius, 60)
                Shapes.lines(radius, 6, tls[1])
                tls[1].lt(60).fd(radius)

            tls[1].pu().lt(90).circle(radius, 60).pd().rt(150)
            Shapes.SOD(radius * 2, tls[1])

    class TurtleThree:
        TURTLE_COUNT = 3

        def squares10(tls: list[ChainTurtle]) -> None:
            """
            Draws 4 squares on each corner, with 4 squares tilted by 45° in between them + Star of David (fill) in the middle
            :param tls: list of 3 chainable turtles
            """
            length: float | int = helper.length_float()
            diameter, d_half = helper.diameter_sq(length)

            tls[0].teleport(d_half, d_half)
            tls[1].fd_inv(d_half + (length - d_half)).rt(45)
            for a in range(2):
                for _ in range(4):
                    Shapes.square_fill(length, tls[a])
                    tls[a].rt(90).fd_inv(diameter)

            tls[2].fd(d_half + (length - d_half)).lt(135)
            Shapes.square_fill(diameter, tls[2])
            tls[2].teleport(d_half, d_half).lt(45)
            Shapes.square_fill(diameter, tls[2])

        def sd_flower(tls: list[ChainTurtle]) -> None:
            """
            Draws a 6 petalled flower inside a star of David inside a hexagon
            :param tls: list of 3 chainable turtles
            """
            radius: float | int = helper.radius_float()
            hexa_side = (radius * sine(120)) / sine(30)
            tls[0].lt(30)
            Shapes.hexa_flower(radius, tls[0])
            Shapes.SOD(radius, tls[1])
            tls[2].lt(30)
            Shapes.hexagon_ft(hexa_side, tls[2])

    class TurtleFour:
        TURTLE_COUNT = 4

        def flower_4petals(tls: list[ChainTurtle]) -> None:
            """
            Draws a flower with 4 petals
            :param tls: list of 4 chainable turtles
            """
            for i, t in enumerate(tls):
                t.lt(i * 90)
            for a in range(0, 500, 10):
                for b in range(4):
                    tls[b].circle(a)

        def square4(tls: list[ChainTurtle]) -> None:
            """
            Draws 4 squares where the axes slice the squares in half
            :param tls: list of 4 chainable turtles
            """
            length: float | int = helper.length_float()
            interval: float | int = helper.intervals_f()
            for i, t in enumerate(tls):
                t.lt(i * 90)
            for a in range_f(0, length + 1, interval):
                for t in tls:
                    Shapes.square_half(a, t)

        def quadrant_square(tls: list[ChainTurtle]) -> None:
            """
            Draws squares in each quadrant
            :param tls: list of 4 chainable turtles
            """
            length: float | int = get_num(float, "Enter max side length(ℚ>0): ", MIN=1)
            interval: float | int = helper.intervals_f()

            for i, t in enumerate(tls):
                t.lt(i * 90)
            for a in range_f(0, length + 1, interval):
                for t in tls:
                    Shapes.square(a, t)

        def multi_square_grid(tls: list[ChainTurtle]) -> None:
            """
            Draws a 45° tilted grid with 4 turtles => 4 colors
            :param tls: list of 4 chainable turtles
            """
            length: float | int = helper.length_float()
            x_val = (length * sqrt(2)) / 2
            tls[1].lt(180)

            for i in range(1, 5, 3):
                tls[0].teleport(x_val * i, 0).lt(135)
                Shapes.square(length * i, tls[0])
                tls[0].home_inv()
            for a in range(1, 3):
                tls[1].teleport(x_val * a, x_val * a)
                Shapes.square(((length * 2) * a) / sqrt(2), tls[1])

            Shapes.lines(x_val * 4, 4, tls[2])
            tls[3].pu().fd(x_val * 4).rt(135).pd()
            for _ in range(3):
                tls[3].fd_inv(length).rt(90).fd(length * 4).bk(length * 4).lt(90)

            tls[3].pu().fd(length).rt(90).pd()
            for _ in range(3):
                tls[3].fd_inv(length).rt(90).fd(length * 4).bk(length * 4).lt(90)

    class TurtleSix:
        TURTLE_COUNT = 6

        def circles6(tls: list[ChainTurtle]) -> None:
            """
            Draws 6 circles (with 6 turtles) 'simultaneously' with each being 60° to the left of the last one
            :param tls: list of 6 chainable turtles
            """
            radius: float|int = helper.radius_float()

            step = 2 * pi * radius / 360
            for i,t in enumerate(tls):
                t.lt(i * 60)
            for a in range(0, 360):
                for b in range(6):
                    tls[b].fd(step).rt(1)
                SU()

    @staticmethod
    def duo_triforce() -> list[ChainTurtle]:
        """Draws a duo triforce, triangles have corresponding colors"""
        length: float | int = helper.length_float()

        color_list = ["red", "blue", "green", "magenta", "cyan", "yellow", "black"]
        height = sqrt(length ** 2 - (length / 2) ** 2)
        tls = [ChainTurtle().color(t) for t in color_list]

        tls[0].teleport(length / 2, height).lt(120)
        tls[1].lt(120)
        tls[3].teleport(-length / 4, height / 2).lt(60)
        tls[4].lt(60)
        tls[5].lt(60).teleport(length / 4, height / 2)
        for n in range(3):
            Shapes.triangle_fill(length, tls[n])
            Shapes.triangle_fill(length / 2, tls[n + 3])
        for _ in range(3):
            Shapes.triangle_ft(length, tls[6])
            tls[6].lt(60).fd(length).lt(60)

        tls[6].setpos(length / 4, height / 2).lt(120)
        Shapes.triangle_ft(length / 2, tls[6])
        SU()
        return tls

    @staticmethod
    def flower_infinite() -> list[ChainTurtle]:
        """Draws a customized flower: petals + circles number"""
        tls: list[ChainTurtle]
        petals_count: int
        tls, petals_count = tls_color(entry="Enter petal count: ")
        circles_num: int = get_num(int, "Enter circles count: ", MIN=1)
        interval: float | int = helper.intervals_f()

        angle = int(360 / petals_count)
        for i in range(petals_count):
            tls[i].lt(i * angle)
        for a in range_f(0, circles_num + 1, interval):
            for b in range(petals_count):
                tls[b].circle(a)
        for t in tls:
            t.lt(90).fd(circles_num * 2)
        SU()
        return tls

    def change_shape() -> None:
        """Changes the shape of the turtle according to user input"""
        shape_choice: str = get_str('''
            Which shape?
            arrow, blank, circle, classic, square, triangle, turtle
            Enter choice: 
            ''', ("arrow","blank","circle","classic","square","triangle","turtle"))
        UV["tls_shape"]: str = shape_choice

    @classmethod
    def _list_designs(cls) -> designs_dict:
        """
        Creates a dictionary with all the designs and returns it
        :return: dictionary
        """
        dictionary: designs_dict = {}
        name: str
        item: Callable[[list[ChainTurtle]|None], list[ChainTurtle]]
        for name, item in vars(cls).items():
            if name.startswith("Turtle") and isinstance(item, type):
                dictionary.update(classes_to_dict(item))
            elif callable(item):
                dictionary[name] = item

        return dictionary

def get_Patterns_dict() -> designs_dict:
    return {
        name.replace("_", " "): func
        for name, func in Designs._list_designs().items()
        if not name.startswith("_")
    }

# DICTIONARY: ALL COMMANDS OF MAIN MENU
PATTERNS = get_Patterns_dict()