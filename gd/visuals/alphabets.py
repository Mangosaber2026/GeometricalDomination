from collections.abc import Callable
from functools import wraps
from math import sqrt
from numbers import Real

import turtle_extension as tx
import uf

from .shapes import Shapes


class AlphabetsMeta(type):
    """
    METACLASS: specifically designed for the Alphabets class, not to be used conventionally!
    """
    def __getattr__(cls, func: str):
        for category in (
            cls.Letters,
            cls.Punctuation,
            cls.Shapes,
        ):
            function = getattr(category, func, None)

            if callable(function):
                return function

        raise uf.attribute_error()(f"""
            Function: AlphabetsMeta.__getattr__
            {cls.__name__} has no attribute {func!r}
            """)

def alphabets_validate(height: Real, tls: tx.ChainTurtle) -> tuple[Real, tx.ChainTurtle]:
    """
    This function takes the parameters from all alphabet drawing functions and validates them.
    :param height: height of each letter/punctuation/symbol
    :param tls: an instance of ChainTurtle
    :return: validated height and tls
    """
    uf.ComboValidate(height, name="height")(uf.real_validate(), uf.Positive())
    uf.TypeValidate(tx.ChainTurtle)(tls, name="tls")
    return height, tls

def alphabets_deco(func):
    """
    DECORATOR!!!

    This decorator takes each alphabet function and uses alphabets_validate to validate the functions
    parameters.
    :param func: alphabet function
    :return: validated alphabet function
    """
    @wraps(func)
    def wrapper(height: Real, tls: tx.ChainTurtle):
        alphabets_validate(height, tls)
        return func(height, tls)
    return wrapper

def alphabets_main_deco(cls) -> type:
    """
    Takes the Alphabets class and transforms it's subclasses Letters, Punctuation and Shapes with
    the decorators staticmethod and qtm_validation_decorator
    :param cls: Alphabets class
    :return: decorated Alphabets class
    """
    for category in (
        cls.Letters,
        cls.Punctuation,
        cls.Shapes,
    ):
        uf.cls_deco_superposition(staticmethod, alphabets_deco)(category)
    return cls

@alphabets_main_deco
class Alphabets(metaclass=AlphabetsMeta):

    class Letters:
        """
        A collection of functions to draw the English alphabets.
        """
        def A(height, tls):

            height_60 = uf.pct60(height)
            height_40 = uf.pct40(height)
            height_10 = uf.pct10(height)

            a = height_60 / uf.sine(70)
            b = height_40 / uf.sine(70)
            c = 2 * sqrt(a ** 2 - height_60 ** 2)

            (
                tls
                . rt(20)
                . fd(b)
                . rt(70)
                . fd(c)
                . bk(c)
                . lt(70)
                . fd(a)
                . rt(140)
                . fd(a + b)
                . lt(70)
                . fd_inv(height_10)
                . lt(90)
            )

        def B(height, tls):

            height_20 = uf.pct20(height)
            height_25 = uf.pct25(height)
            height_50 = uf.pct50(height)
            (
                tls.fd(height)
                . rt(90)
                . fd(height_20)
                . circle(-height_25, 180)
                . lt(180)
                . circle(-height_25, 180)
                . fd(height_20)
                . rt(180)
                . fd_inv(height_50+5)
                . lt(90)
             )

        def C(height, tls):

            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)
            (
                tls
                . rt(90)
                . fd_inv(height_50)
                . lt(90)
                . fd_inv(height)
                . lt(90)
                . circle(height_50, 180)
                . fd_inv(height_10)
                . lt(90)
            )

        def D(height, tls):

            height_50 = uf.pct50(height)
            (
                tls
                . fd(height)
                . rt(90)
                . circle(-height_50, 180)
                . rt(180)
                . fd_inv(height_50+10)
                . lt(90)
            )

        def E(height, tls):

            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)
            (
                tls
                . rt(90)
                . fd_inv(height_50)
                . lt(90)
                . fd_inv(height)
            )
            for _ in range(3):
                tls.lt(90).fd(height_50)

            (
                tls
                . bk(height_50)
                . rt(90)
                . fd(height_50)
                . lt(90)
                . fd(height_50)
                . fd_inv(height_10)
                . lt(90)
            )

        def F(height, tls):

            height_50 = uf.pct50(height)
            height_60 = uf.pct60(height)
            for _ in range(2):
                (
                    tls
                    . fd(height_50)
                    . rt(90)
                    . fd(height_50)
                    . bk(height_50)
                    . lt(90)
                )
            (
                tls
                . lt(90)
                . bk_inv(height_60)
                . rt(90)
                . bk_inv(height)
            )

        def G(height, tls):

            height_50 = uf.pct50(height)
            height_30 = uf.pct30(height)
            height_40 = uf.pct40(height)
            (
                tls
                . rt(90)
                . fd_inv(height_50)
                . lt(90)
                . fd_inv(height)
                . lt(90)
                . circle(height_50, 180).lt(90)
                . fd(height_50)
                . lt(90)
                . fd(height_30)
                . rt(180)
                . fd_inv(height_40)
                . lt(90)
                . bk_inv(height_50)
            )

        def H(height, tls):

            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)
            (
                tls
                . fd(height)
                . bk(height_50)
                . rt(90)
                . fd(height_50)
                . lt(90)
                . fd(height_50)
                . bk(height)
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
            )

        def I(height, tls):

            height_50 = uf.pct50(height)
            height_25 = uf.pct25(height)
            height_10 = uf.pct10(height)
            (
                tls
                . rt(90)
                . fd(height_50)
                . bk(height_25)
                . lt(90)
                . fd(height)
                . rt(90)
                . bk(height_25)
                . fd(height_50)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height)
            )

        def J(height, tls):

            height_60 = uf.pct60(height)
            height_70 = uf.pct70(height)
            height_30 = uf.pct30(height)
            (
                tls
                . fd_inv(height)
                . rt(90)
                . fd(height_60)
                . rt(90)
                . fd(height_70)
                . circle(-height_30, 180)
                . rt(90)
                . fd_inv(height_70)
                . lt(90)
                . bk_inv(height_30)
            )

        def K(height, tls):

            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)
            diagonal = sqrt(height_50 ** 2 * 2)

            (
                tls
                . fd(height)
                . bk(height_50)
                . rt(45)
                . fd(diagonal)
                . bk(diagonal)
                . rt(90)
                . fd(diagonal)
                . lt(45)
                . fd_inv(height_10)
                . lt(90)
            )

        def L(height, tls):

            height_45 = uf.Percent(45)(height)
            height_10 = uf.pct10(height)
            (
                tls
                . fd(height)
                . bk(height)
                . rt(90)
                . fd(height_45)
                . fd_inv(height_10)
                . lt(90)
            )

        def M(height, tls):

            diagonal = (height / uf.cosine(30)) / 2
            height_10 = uf.pct10(height)

            (
                tls
                . fd(height)
                . rt(150)
                . fd(diagonal)
                . lt(120)
                . fd(diagonal)
                . rt(150)
                . fd(height)
                . lt(90)
                . fd_inv(height_10)
                . lt(90)
            )

        def N(height, tls):

            diagonal = height / uf.cosine(30)
            height_10 = uf.pct10(height)

            (
                tls
                . fd(height)
                . rt(150)
                . fd(diagonal)
                . lt(150)
                . fd(height)
                . bk(height)
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
            )

        def O(height, tls):

            height_40 = uf.pct40(height)
            height_20 = uf.pct20(height)
            height_90 = uf.pct90(height)
            (
                tls
                . fd_inv(height_40)
                . rt(180)
                . circle(height_40, 180)
                . fd(height_20)
                . circle(height_40, 180)
                . fd(height_20)
                . lt(90)
                . fd_inv(height_90)
                . lt(90)
                . bk_inv(height_40)
            )

        def P(height, tls):

            height_27 = uf.Percent(27)(height)
            height_37 = uf.Percent(37)(height)
            height_46 = uf.Percent(46)(height)
            (
                tls
                . fd(height)
                . rt(90)
                . circle(-height_27, 180)
                . rt(180)
                . fd_inv(height_37)
                . lt(90)
                . bk_inv(height_46)
            )

        def Q(height, tls):

            height_50 = uf.pct50(height)
            height_35 = uf.Percent(35)(height)
            height_10 = uf.pct10(height)

            side_a = sqrt(height_35 ** 2 + height_50 ** 2)
            turn_right = uf.asine(height_50 / side_a)

            (
                tls
                . rt(90)
                . fd_inv(height_50)
                . circle(height_50, 360)
                . lt(90)
                . fd_inv(height_35)
                . rt(180 - turn_right)
                . fd(side_a)
                . lt(90 - turn_right)
                . fd_inv(height_10)
                . lt(90)
            )

        def R(height, tls):

            height_27 = uf.Percent(27)(height)
            height_46 = uf.Percent(46)(height)
            height_10 = uf.pct10(height)
            (
                tls
                . fd(height)
                . rt(90)
                . circle(-height_27, 180)
                . lt(120)
                . fd(height_46 / uf.sine(60))
                . lt(60)
                . fd_inv(height_10)
                . lt(90)
            )

        def S(height, tls):

            height_27 = uf.Percent(27)(height)
            height_54 = uf.Percent(54)(height)
            height_37 = uf.Percent(37)(height)
            arc_70 = uf.pct70(360)
            arc_30 = uf.pct30(360)

            geo_fix = uf.sine(20) - uf.sine(272)
            radius = height_27

            (
                tls
                . rt(90)
                . fd_inv(height_54)
                . lt(90)
                . fd_inv(height_54 + geo_fix * radius)
                . lt(20)
                . circle(radius, arc_70)
                . circle(-radius, arc_70)
                . pu()
                . circle(-radius, arc_30)
                . rt(2)
                . fd(height_37)
                . lt(90)
                . bk(height_54)
                . pd()
            )

        def T(height, tls):

            height_45 = uf.Percent(45)(height)
            height_90 = uf.pct90(height)
            height_10 = uf.pct10(height)
            (
                tls
                . rt(90)
                . fd_inv(height_45)
                . lt(90)
                . fd(height)
                . lt(90)
                . fd(height_45)
                . bk(height_90)
                . bk_inv(height_10)
                . rt(90)
                . bk_inv(height)
            )

        def U(height, tls):

            height_70 = uf.pct70(height)
            height_30 = uf.pct30(height)
            height_10 = uf.pct10(height)
            (
                tls
                . fd_inv(height)
                . rt(180)
                . fd(height_70)
                . circle(height_30, 180)
                . fd(height_70)
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height)
            )

        def V(height, tls):

            height_10 = uf.pct10(height)
            diagonal = height / uf.sine(65)
            (
                tls
                . fd_inv(height)
                . rt(155)
                . fd(diagonal)
                . lt(130)
                . fd(diagonal)
                . rt(65)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height)
            )

        def W(height, tls):

            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)

            side_a = height / uf.sine(75)
            side_c = height_50 / uf.sine(75)

            (
                tls
                . fd_inv(height)
                . rt(165)
                . fd(side_a)
                . lt(150)

                . fd(side_c)
                . rt(150)
                . fd(side_c)
                . lt(150)
                . fd(side_a)

                . rt(75)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height)
            )

        def X(height, tls):

            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)

            a_half = height_50 / uf.sine(55)
            a_full = a_half * 2
            side_b = sqrt(a_half ** 2 - height_50 ** 2)
            (
                tls
                . rt(35)
                . fd(a_full)
                . lt(125)
                . fd_inv(side_b * 2)
                . lt(125)
                . fd(a_full)
                . lt(55)
                . fd_inv(height_10)
                . lt(90)
            )

        def Y(height, tls):

            height_40 = uf.pct40(height)
            height_60 = uf.pct60(height)
            height_10 = uf.pct10(height)

            side = height_40 / uf.sine(55)
            width = sqrt(side ** 2 - height_40 ** 2)

            (
                tls
                . rt(90)
                . fd_inv(width)
                . lt(90)
                . fd(height_60)
                . rt(35)
                . fd(side)

                .bk(side)
                .lt(70)
                .fd(side)
                .rt(35)
                .bk_inv(height)
                .rt(90)
                .fd_inv(2 * width + height_10)
                .lt(90)
            )

        def Z(height, tls):

            height_10 = uf.pct10(height)

            side_a = height / uf.sine(50)
            side_b = sqrt(side_a ** 2 - height ** 2)

            (
                tls
                . fd_inv(height)
                . rt(90)
                . fd(side_b)
                . rt(130)
                . fd(side_a)
                . lt(130)
                . fd(side_b)
                . fd_inv(height_10)
                . lt(90)
            )

    class Punctuation:
        """A collection of functions to draw English punctuation marks."""
        def space(height, tls):

            height_25 = uf.pct25(height)
            tls.rt(90).fd_inv(height_25).lt(90)

        def dot(height, tls):

            height_5 = uf.Percent(5)(height)
            height_10 = uf.pct10(height)
            height_15 = uf.Percent(15)(height)
            (
                tls
                . rt(90)
                . fd_inv(height_5)
                . dot(height_10)
                . fd_inv(height_15)
                . lt(90)
            )

        def exclamation(height, tls):

            height_20 = uf.pct20(height)
            height_80 = uf.pct80(height)
            height_10 = uf.pct10(height)
            height_5 = uf.Percent(5)(height)

            tls.fd_inv(height_20)
            Shapes.rectangle_fill(height_80, height_10, -1, tls)

            (
                tls
                . lt(180)
                . fd_inv(height_10)
                . circle_fill(height_5, 540)
                . bk_inv(height_5)
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
            )

        def question(height, tls):

            height_10 = uf.pct10(height)
            height_25 = uf.pct25(height)
            height_fifth = uf.pct20(height)
            (
                tls
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
                . fd_inv(height)
                . lt(36)
                . begin_fill()

                . fd(height_10)
                . rt(90)
                . circle(-height_fifth, 216)
                .circle(height_fifth, 216)
                .rt(90)
                .fd(height_10)
                .rt(90)
                .circle(-height_fifth, 216)
                .circle(height_fifth, 216)

                .end_fill()
                .lt(54)
                .fd_inv(height)
                .lt(90)
                .fd_inv(height_10)
                .dot(height_10)
                .fd_inv(height_25)
                .lt(90)
            )

        def apostrophe(height, tls):

            height_70 = uf.pct70(height)
            height_30 = uf.pct30(height)
            height_5 = uf.Percent(5)(height)
            height_15 = uf.Percent(15)(height)

            tls.fd_inv(height_70)

            Shapes.rectangle_fill(height_30, height_5, -1, tls)

            tls.rt(90).fd_inv(height_15).lt(90).bk_inv(height_70)

        def colon(height, tls):

            height_7 = uf.Percent(7)(height)
            height_28 = uf.Percent(28)(height)
            height_17 = uf.Percent(17)(height)
            (
                tls
                . rt(90)
                . fd_inv(height_7)
                . circle_fill(height_7, 360)
                . lt(90)
                . fd_inv(height_28)

                .rt(90)
                .circle_fill(height_7, 360)
                .fd_inv(height_17)
                .lt(90)
                .bk_inv(height_28)
            )

        def comma(height, tls):

            height_5 = uf.Percent(5)(height)
            height_1 = uf.Percent(1)(height)
            height_15 = uf.Percent(15)(height)
            (
                tls
                . begin_fill()
                . rt(180)
                . fd(height_5)
                . circle(-height_5, 90)
                . lt(90)
                . fd(height_5)
                . lt(90)

                . circle(height_1, 90)
                . fd(height_5)
                . lt(90)
                . fd(height_5)
                . end_fill()
                . rt(180)
                . fd_inv(height_15)
                . lt(90)
            )

    class Shapes:
        """A collection of functions to draw shapes (and mathematical symbols)."""
        def plus(height, tls):

            height_25 = uf.pct25(height)
            height_50 = uf.pct50(height)
            height_35 = uf.Percent(35)(height)
            (
                tls
                . rt(90)
                . fd_inv(height_25)
                . lt(90)
                . fd_inv(height_50)
                . rt(90)
            )
            Shapes.lines(height_25, 4, tls)
            (
                tls
                . fd_inv(height_35)
                . lt(90)
                .bk_inv(height_50)
            )

        def equals(height, tls):

            height_30 = uf.pct30(height)
            height_50 = uf.pct50(height)
            height_40 = uf.pct40(height)
            height_60 = uf.pct60(height)
            height_70 = uf.pct70(height)
            (
                tls
                . fd_inv(height_30)
                . rt(90)
                . fd(height_50)
                . lt(90)
                . fd_inv(height_40)
                . lt(90)
                . fd(height_50)
                . bk_inv(height_60)
                . rt(90)
                . bk_inv(height_70)
            )

        def times(height, tls):

            height_25 = uf.pct25(height)
            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)

            side = uf.sine(45) * height_25
            (
                tls
                . fd_inv(height_50)
                . rt(90)
                . fd_inv(height_50)
                . rt(45)
            )
            Shapes.lines(height_25, 4, tls)
            (
                tls
                . lt(45)
                . fd_inv(side + height_10)
                . lt(90)
                . bk_inv(height_50)
            )

        def minus(height, tls):

            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)
            (
                tls
                . fd_inv(height_50)
                . rt(90)
                . fd(height_50)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height_50)
            )

        def underline(height, tls):

            height_50 = uf.pct50(height)
            height_10 = uf.pct10(height)

            tls.rt(90).fd(height_50).fd_inv(height_10).lt(90)

        def heart(height, tls):

            height_60 = uf.pct60(height)
            height_65 = uf.Percent(65)(height)
            height_32_5 = uf.Percent(32.5)(height)
            (
                tls
                . rt(90)
                . fd_inv(height_60)
                . lt(135)
                . begin_fill()
                . fd(height_65)

                .circle(-height_32_5, 180)
                .lt(90)
                .circle(-height_32_5, 180)

                .fd(height_65)
                .end_fill()
                .lt(135)
                .fd_inv(height_65)
                .lt(90)
            )

        def star(height, tls):

            direction = tls.heading()
            side = height / uf.sine(62)
            geo_fix = uf.Percent(-1e-05)(height)
            height_40 = uf.pct40(height)
            (
                tls
                . rt(90)
                . fd_inv(height)
                . lt(90)
                . fd(geo_fix)
                . lt(17)
            )
            for _ in range(5):
                tls.fd(side).lt(144)

            (
                tls
                . seth(direction - 90)
                . fd(height_40)
                . lt(90)
            )

    @classmethod
    def list_alphabets(cls):

        dictionary = uf.classes_to_dict(cls.Letters, cls.Punctuation, cls.Shapes)

        for name, item in vars(cls).items():
            if not isinstance(item, type) and isinstance(item, Callable):
                dictionary[name] = item

        return dictionary

def letters_functions():

    return {
        name: func
        for name, func in uf.classes_to_dict(Alphabets.Letters).items()
    }

letters_dict = letters_functions()
# ALPHABET DICTIONARY
ALPHABETS = {
    **letters_dict,
    " ": Alphabets.space,
    ".": Alphabets.dot,
    "!": Alphabets.exclamation,
    "?": Alphabets.question,
    "'": Alphabets.apostrophe,
    ":": Alphabets.colon,
    ",": Alphabets.comma,
    "+": Alphabets.plus,
    "=": Alphabets.equals,
    "*": Alphabets.times,
    "-": Alphabets.minus,
    "_": Alphabets.underline,
    "<": Alphabets.heart,
    "#": Alphabets.star,
}