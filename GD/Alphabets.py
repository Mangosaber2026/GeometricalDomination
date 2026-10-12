from .TurtleHeart import ChainTurtle
from math import sqrt
from .Shapes import Shapes
from collections.abc import Callable
import UF as uf
from numbers import Real
from functools import wraps


sine = uf.sine
cosine = uf.cosine
Positive = uf.Positive

type alphabet_function = Callable[[Real, ChainTurtle], None]

type alphabet_dict = dict[str, alphabet_function]

type full_alphabet_dict = dict[str, alphabet_function | Callable[[], full_alphabet_dict]]

class AlphabetsMeta(type):
    """
    METACLASS: specifically designed for the Alphabets class, not to be used conventionally!
    """
    def __getattr__(cls, func: str) -> alphabet_function:
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

def alphabets_validate(height: Real, tls: ChainTurtle) -> tuple[Real, ChainTurtle]:
    """
    This function takes the parameters from all alphabet drawing functions and validates them.
    :param height: height of each letter/punctuation/symbol
    :param tls: an instance of ChainTurtle
    :return: validated height and tls
    """
    uf.ComboValidate(height, name="height")(uf.real_validate(), uf.Positive())
    uf.TypeValidate(ChainTurtle)(tls, name="tls")
    return height, tls

def alphabets_deco(func: alphabet_function) -> alphabet_function:
    """
    DECORATOR!!!

    This decorator takes each alphabet function and uses alphabets_validate to validate the functions
    parameters.
    :param func: alphabet function
    :return: validated alphabet function
    """
    @wraps(func)
    def wrapper(height: Real, tls: ChainTurtle):
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

            a = (height*0.6) / sine(70)
            b = (height*0.4) / sine(70)
            c = 2 * sqrt(a**2 - (height*0.6)**2)

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
                . fd_inv(height/10)
                . lt(90)
            )

        def B(height, tls):

            (
                tls.fd(height)
                . rt(90)
                . fd(height/5)
                . circle(-(height/4), 180)
                . lt(180)
                . circle(-(height/4), 180)
                . fd(height/5)
                . rt(180)
                . fd_inv(height/2+5)
                . lt(90)
             )

        def C(height, tls):

            (
                tls
                . rt(90)
                . fd_inv(height/2)
                . lt(90)
                . fd_inv(height)
                . lt(90)
                . circle(height/2, 180)
                . fd_inv(height/10)
                . lt(90)
            )

        def D(height, tls):

            (
                tls
                . fd(height)
                . rt(90)
                . circle(-(height/2), 180)
                . rt(180)
                . fd_inv(height/2+10)
                . lt(90)
            )

        def E(height, tls):

            (
                tls
                . rt(90)
                . fd_inv(height/2)
                . lt(90)
                . fd_inv(height)
            )
            for _ in range(3):
                tls.lt(90).fd(height/2)

            (
                tls
                . bk(height/2)
                . rt(90)
                . fd(height/2)
                . lt(90)
                . fd(height/2)
                . fd_inv(height/10)
                . lt(90)
            )

        def F(height, tls):

            for _ in range(2):
                (
                    tls
                    . fd(height/2)
                    . rt(90)
                    . fd(height/2)
                    . bk(height/2)
                    . lt(90)
                )
            (
                tls
                . lt(90)
                . bk_inv(height*0.6)
                . rt(90)
                . bk_inv(height)
            )

        def G(height, tls):

            (
                tls
                . rt(90)
                . fd_inv(height/2)
                . lt(90)
                . fd_inv(height)
                . lt(90)
                . circle(height/2, 180).lt(90)
                . fd(height/2)
                . lt(90)
                . fd(height*0.3)
                . rt(180)
                . fd_inv(height*0.4)
                . lt(90)
                . bk_inv(height/2)
            )

        def H(height, tls):

            (
                tls
                . fd(height)
                . bk(height/2)
                . rt(90)
                . fd(height/2)
                . lt(90)
                . fd(height/2)
                . bk(height)
                . rt(90)
                . fd_inv(height/10)
                . lt(90)
            )

        def I(height, tls):

            (
                tls
                . rt(90)
                . fd(height/2)
                . bk(height/4)
                . lt(90)
                . fd(height)
                . rt(90)
                . bk(height/4)
                . fd(height/2)
                . fd_inv(height/10)
                . lt(90)
                . bk_inv(height)
            )

        def J(height, tls):

            (
                tls
                . fd_inv(height)
                . rt(90)
                . fd(height*0.6)
                . rt(90)
                . fd(height*0.7)
                . circle(-(height*0.3), 180)
                . rt(90)
                . fd_inv(height*0.7)
                . lt(90)
                . bk_inv(height*0.3)
            )

        def K(height: Real, tls: ChainTurtle) -> None:

            diagonal = sqrt((height/2) ** 2 * 2)

            (
                tls
                . fd(height)
                . bk(height/2)
                . rt(45)
                . fd(diagonal)
                . bk(diagonal)
                . rt(90)
                . fd(diagonal)
                . lt(45)
                . fd_inv(height/10)
                . lt(90)
            )

        def L(height, tls):

            (
                tls
                . fd(height)
                . bk(height)
                . rt(90)
                . fd(height*0.45)
                . fd_inv(height/10)
                . lt(90)
            )

        def M(height, tls):

            diagonal = (height / cosine(30)) / 2

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
                . fd_inv(height/10)
                . lt(90)
            )

        def N(height, tls) -> None:

            diagonal = height / cosine(30)

            (   tls
                . fd(height)
                . rt(150)
                . fd(diagonal)
                . lt(150)
                . fd(height)
                . bk(height)
                . rt(90)
                . fd_inv(height/10)
                . lt(90)
                )

        def O(height, tls):

            (
                tls
                . fd_inv(height*0.4)
                . rt(180)
                . circle(height*0.4, 180)
                . fd(height/5)
                . circle(height*0.4, 180)
                . fd(height/5)
                . lt(90)
                . fd_inv(height*0.9)
                . lt(90)
                . bk_inv(height*0.4)
            )

        def P(height, tls):

            (
                tls
                . fd(height)
                . rt(90)
                . circle(-(height*0.27), 180)
                . rt(180)
                . fd_inv(height*0.37)
                . lt(90)
                . bk_inv(height*0.46)
            )

        def Q(height, tls):

            side_a = sqrt((height * 0.35) ** 2 + (height / 2) ** 2)
            turn_right = uf.asine((height / 2) / side_a)

            (
                tls
                . rt(90)
                . fd_inv(height/2)
                . circle(height/2, 360)
                . lt(90)
                . fd_inv(height*0.35)
                . rt(180 - turn_right)
                . fd(side_a)
                . lt(90 - turn_right)
                . fd_inv(height / 10)
                . lt(90)
            )

        def R(height, tls):

            (
                tls
                . fd(height)
                . rt(90)
                . circle(-(height*0.27), 180)
                . lt(120)
                . fd((height*0.46) / sine(60))
                . lt(60)
                . fd_inv(height/10)
                . lt(90)
            )

        def S(height, tls):

            geo_fix = sine(20) - sine(272)
            radius = height * 0.27

            (
                tls
                . rt(90)
                . fd_inv(height*0.54)
                . lt(90)
                . fd_inv(height*0.54 + geo_fix*radius)
                . lt(20)
                . circle(radius, 0.7*360)
                . circle(-radius, 0.7*360)
                . pu()
                . circle(-radius, 0.3*360)
                . rt(2)
                . fd(height*0.37)
                . lt(90)
                . bk(height*0.54)
                . pd()
            )

        def T(height, tls):

            (
                tls
                . rt(90)
                . fd_inv(height*0.45)
                . lt(90)
                . fd(height)
                . lt(90)
                . fd(height*0.45)
                . bk(height*0.9)
                . bk_inv(height/10)
                . rt(90)
                . bk_inv(height)
            )

        def U(height, tls):

            (
                tls
                . fd_inv(height)
                . rt(180)
                . fd(height*0.7)
                . circle(height*0.3, 180)
                . fd(height*0.7)
                . rt(90)
                . fd_inv(height/10)
                . lt(90)
                . bk_inv(height)
            )

        def V(height, tls):

            diagonal = height / sine(65)

            (
                tls
                . fd_inv(height)
                . rt(155)
                . fd(diagonal)
                . lt(130)
                . fd(diagonal)
                . rt(65)
                . fd_inv(height/10)
                . lt(90)
                . bk_inv(height)
            )

        def W(height, tls):

            side_a = height / sine(75)
            side_c = (height/2) / sine(75)

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
                . fd_inv(height/10)
                . lt(90)
                . bk_inv(height)
            )

        def X(height, tls):

            a_half = (height/2) / sine(55)
            side_b = sqrt((a_half **2) - (height/2)**2)

            (
                tls
                . rt(35)
                . fd(a_half *2)
                . lt(125)
                . fd_inv(side_b * 2)
                . lt(125)
                . fd(a_half *2)
                . lt(55)
                . fd_inv(height/10)
                . lt(90)
            )

        def Y(height, tls):

            side = (height*0.4) / sine(55)
            width = sqrt(side**2 - (height*0.4)**2)

            (
                tls
                . rt(90)
                . fd_inv(width)
                . lt(90)
                . fd(height*0.6)
                . rt(35)
                . fd(side)

                .bk(side)
                .lt(70)
                .fd(side)
                .rt(35)
                .bk_inv(height)
                .rt(90)
                .fd_inv(2 * width + height / 10)
                .lt(90)
            )

        def Z(height, tls):

            side_a = height / sine(50)
            side_b = sqrt(side_a**2 - height**2)

            (
                tls
                . fd_inv(height)
                . rt(90)
                . fd(side_b)
                . rt(130)
                . fd(side_a)
                . lt(130)
                . fd(side_b)
                . fd_inv(height/10)
                . lt(90)
            )

    class Punctuation:
        """A collection of functions to draw English punctuation marks."""
        def space(height, tls):

            tls.rt(90).fd_inv(height/4).lt(90)

        def dot(height, tls):

            (
                tls
                . rt(90)
                . fd_inv(height/20)
                . dot(height/10)
                . fd_inv(height*0.15)
                . lt(90)
            )

        def exclamation(height, tls):

            tls.fd_inv(height/5)
            Shapes.rectangle_fill(height*0.8, height/10, -1, tls)

            (
                tls
                . lt(180)
                . fd_inv(height/10)
                . circle_fill(height/20, 540)
                . bk_inv(height/20)
                . rt(90)
                . fd_inv(height/10)
                . lt(90)
            )

        def question(height, tls):

            height_tenth = height / 10
            height_quarter = height / 4
            height_fifth = height / 5
            (
                tls
                . rt(90)
                . fd_inv(height_tenth)
                . lt(90)
                . fd_inv(height)
                . lt(36)
                . begin_fill()

                . fd(height_tenth)
                . rt(90)
                . circle(-height_fifth, 216)
                .circle(height_fifth, 216)
                .rt(90)
                .fd(height_tenth)
                .rt(90)
                .circle(-height_fifth, 216)
                .circle(height_fifth, 216)

                .end_fill()
                .lt(54)
                .fd_inv(height)
                .lt(90)
                .fd_inv(height_tenth)
                .dot(height_tenth)
                .fd_inv(height_quarter)
                .lt(90)
            )

        def apostrophe(height, tls):

            tls.fd_inv(height*0.7)

            Shapes.rectangle_fill(height*0.3, height/20, -1, tls)

            tls.rt(90).fd_inv(height*0.15).lt(90).bk_inv(height*0.7)

        def colon(height, tls):

            height_p7 = height*0.07
            height_p28 = height*0.28
            (
                tls
                . rt(90)
                . fd_inv(height_p7)
                . circle_fill(height_p7, 360)
                . lt(90)
                . fd_inv(height_p28)

                .rt(90)
                .circle_fill(height_p7, 360)
                .fd_inv(height * 0.17)
                .lt(90)
                .bk_inv(height_p28)
            )

        def comma(height, tls):

            height_p5 = height*0.05
            height_p1 = height*0.01
            height_p15 = height*0.15
            (
                tls
                . begin_fill()
                . rt(180)
                . fd(height_p5)
                . circle(-height_p5, 90)
                . lt(90)
                . fd(height_p5)
                . lt(90)

                . circle(height_p1, 90)
                . fd(height_p5)
                . lt(90)
                . fd(height_p5)
                . end_fill()
                . rt(180)
                . fd_inv(height_p15)
                . lt(90)
            )

    class Shapes:
        """A collection of functions to draw shapes (and mathematical symbols)."""
        def plus(height, tls):

            (
                tls
                . rt(90)
                . fd_inv(height / 4)
                . lt(90)
                . fd_inv(height / 2)
                . rt(90)
            )
            Shapes.lines(height / 4, 4, tls)
            (
                tls
                . fd_inv(height * 0.35)
                . lt(90)
                .bk_inv(height / 2)
            )

        def equals(height, tls):

            (
                tls
                . fd_inv(height * 0.3)
                . rt(90)
                . fd(height / 2)
                . lt(90)
                . fd_inv(height * 0.4)
                . lt(90)
                . fd(height / 2)
                . bk_inv(height * 0.6)
                . rt(90)
                . bk_inv(height * 0.7)
            )

        def times(height, tls):

            side = sine(45) * height / 4
            (
                tls
                . fd_inv(height / 2)
                . rt(90)
                . fd_inv(height / 2)
                . rt(45)
            )
            Shapes.lines(height / 4, 4, tls)
            (
                tls
                . lt(45)
                . fd_inv(side + height / 10)
                . lt(90)
                . bk_inv(height / 2)
            )

        def minus(height, tls):

            (
                tls
                . fd_inv(height / 2)
                . rt(90)
                . fd(height / 2)
                . fd_inv(height / 10)
                . lt(90)
                . bk_inv(height / 2)
            )

        def underline(height, tls):

            tls.rt(90).fd(height / 2).fd_inv(height / 10).lt(90)

        def heart(height, tls):

            (
                tls
                . rt(90)
                . fd_inv(height * 0.6)
                . lt(135)
                . begin_fill()
                . fd(height * 0.65)

                .circle(-height * 0.325, 180)
                .lt(90)
                .circle(-height * 0.325, 180)

                .fd(height * 0.65)
                .end_fill()
                .lt(135)
                .fd_inv(height * 0.65)
                .lt(90)
            )

        def star(height, tls):

            direction = tls.heading()
            (
                tls
                . rt(90)
                . fd_inv(height)
                . lt(90)
                . fd((-1e-07)*height)
                . lt(17)
            )
            for _ in range(5):
                tls.fd(height / sine(62)).lt(144)

            (
                tls
                . seth(direction - 90)
                . fd(height * 0.4)
                . lt(90)
            )

    @classmethod
    def list_alphabets(cls):

        dictionary = uf.classes_to_dict(cls.Letters, cls.Punctuation, cls.Shapes)
        name: str
        item: alphabet_function | Callable[[], full_alphabet_dict]

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