from .TurtleSkeleton import ChainTurtle
from math import sqrt, cos, asin, radians, degrees
from .Shapes_Dictionary import Shapes
from collections.abc import Callable
from typing import TypeAlias
from functools import wraps
from .UniversalFunctions.HelperFunctions import sine, Real
from .UniversalFunctions.DecoratorArchive import class_decorator
from .UniversalFunctions.ClassToDict import classes_to_dict
from .UniversalFunctions.FctInputValidators import validate

alphabet_function: TypeAlias = Callable[[Real, ChainTurtle], None]

class AlphabetsMeta(type):
    def __getattr__(cls, func: str) -> alphabet_function:
        for category in (
            cls.Letters,
            cls.Punctuation,
            cls.Shapes,
        ):
            function = getattr(category, func, None)

            if callable(function):
                return function

        raise AttributeError(f"{cls.__name__} has no attribute {func!r}")

def alphabet_guard(func: alphabet_function) -> alphabet_function:
    """
    Takes the given alphabet function, checks it's inputs, and returns it
    :param func: alphabet function
    :return: decorated function
    """
    @wraps(func)
    def wrapper(height: Real, tls: ChainTurtle) -> None:
        validate(height, Real, "height")
        validate(tls, ChainTurtle, "tls")

        return func(height, tls)
    return wrapper

def alphabet_method(func: alphabet_function) -> Callable:
    """
    Takes each alphabet function and apply staticmethod and alphabet_guard to it
    :param func: alphabet function
    :return: decorated function
    """
    return staticmethod(alphabet_guard(func))

class Alphabets(metaclass=AlphabetsMeta):
    @class_decorator(alphabet_method)
    class Letters:
        def A(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter A with a ChainTurtle
            :param height: height of letter A
            :param tls: a ChainTurtle
            """
            a = (height*0.6) / sine(70); b = (height*0.4) / sine(70); c = 2 * sqrt(a**2 - (height*0.6)**2)
            tls.rt(20).fd(b).rt(70).fd(c).bk(c).lt(70).fd(a).rt(140).fd(a + b).lt(70).fd_inv(height/10).lt(90)

        def B(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter B with a ChainTurtle
            :param height: height of letter B
            :param tls: a ChainTurtle
            """
            tls.fd(height).rt(90).fd(height/5).circle(-(height/4), 180).lt(180).circle(-(height/4), 180).fd(height/5).rt(180).fd_inv(height/2+5).lt(90)

        def C(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter C with a ChainTurtle
            :param height: height of letter C
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height/2).lt(90).fd_inv(height).lt(90).circle(height/2, 180).fd_inv(height/10).lt(90)

        def D(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter D with a ChainTurtle
            :param height: height of letter D
            :param tls: a ChainTurtle
            """
            tls.fd(height).rt(90).circle(-(height/2), 180).rt(180).fd_inv(height/2+10).lt(90)

        def E(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter E with a ChainTurtle
            :param height: height of letter E
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height/2).lt(90).fd_inv(height)
            for _ in range(3): tls.lt(90).fd(height/2)
            tls.bk(height/2).rt(90).fd(height/2).lt(90).fd(height/2).fd_inv(height/10).lt(90)

        def F(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter F with a ChainTurtle
            :param height: height of letter F
            :param tls: a ChainTurtle
            """
            for _ in range(2): tls.fd(height/2).rt(90).fd(height/2).bk(height/2).lt(90)
            tls.lt(90).bk_inv(height*0.6).rt(90).bk_inv(height)

        def G(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter G with a ChainTurtle
            :param height: height of letter G
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height/2).lt(90).fd_inv(height).lt(90).circle(height/2, 180).lt(90).fd(height/2).lt(90).fd(height*0.3).rt(180).fd_inv(height*0.4).lt(90).bk_inv(height/2)

        def H(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter H with a ChainTurtle
            :param height: height of letter H
            :param tls: a ChainTurtle
            """
            tls.fd(height).bk(height/2).rt(90).fd(height/2).lt(90).fd(height/2).bk(height).rt(90).fd_inv(height/10).lt(90)

        def I(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter I with a ChainTurtle
            :param height: height of letter I
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd(height/2).bk(height/4).lt(90).fd(height).rt(90).bk(height/4).fd(height/2).fd_inv(height/10).lt(90).bk_inv(height)

        def J(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter J with a ChainTurtle
            :param height: height of letter J
            :param tls: a ChainTurtle
            """
            tls.fd_inv(height).rt(90).fd(height*0.6).rt(90).fd(height*0.7).circle(-(height*0.3), 180).rt(90).fd_inv(height*0.7).lt(90).bk_inv(height*0.3)

        def K(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter K with a ChainTurtle
            :param height: height of letter K
            :param tls: a ChainTurtle
            """
            diagonal = sqrt((height/2) ** 2 * 2)
            tls.fd(height).bk(height/2).rt(45).fd(diagonal).bk(diagonal).rt(90).fd(diagonal).lt(45).fd_inv(height/10).lt(90)

        def L(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter L with a ChainTurtle
            :param height: height of letter L
            :param tls: a ChainTurtle
            """
            tls.fd(height).bk(height).rt(90).fd(height*0.45).fd_inv(height/10).lt(90)

        def M(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter M with a ChainTurtle
            :param height: height of letter M
            :param tls: a ChainTurtle
            """
            diagonal = (height / cos(radians(30))) / 2
            tls.fd(height).rt(150).fd(diagonal).lt(120).fd(diagonal).rt(150).fd(height).lt(90).fd_inv(height/10).lt(90)

        def N(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter N with a ChainTurtle
            :param height: height of letter N
            :param tls: a ChainTurtle
            """
            diagonal = height / cos(radians(30))
            tls.fd(height).rt(150).fd(diagonal).lt(150).fd(height).bk(height).rt(90).fd_inv(height/10).lt(90)

        def O(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter O with a ChainTurtle
            :param height: height of letter O
            :param tls: a ChainTurtle
            """
            tls.fd_inv(height*0.4).rt(180).circle(height*0.4, 180).fd(height/5).circle(height*0.4, 180).fd(height/5).lt(90).fd_inv(height*0.9).lt(90).bk_inv(height*0.4)

        def P(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter P with a ChainTurtle
            :param height: height of letter P
            :param tls: a ChainTurtle
            """
            tls.fd(height).rt(90).circle(-(height*0.27), 180).rt(180).fd_inv(height*0.37).lt(90).bk_inv(height*0.46)

        def Q(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter Q with a ChainTurtle
            :param height: height of letter Q
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height/2).circle(height/2, 360).lt(90).fd_inv(height*0.35)
            side_a = sqrt((height*0.35)**2 + (height/2)**2); turn_right = degrees(asin((height/2) / side_a))
            tls.rt(180 - turn_right).fd(side_a).lt(90 - turn_right).fd_inv(height/10).lt(90)

        def R(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter R with a ChainTurtle
            :param height: height of letter R
            :param tls: a ChainTurtle
            """
            tls.fd(height).rt(90).circle(-(height*0.27), 180).lt(120).fd((height*0.46) / sine(60)).lt(60).fd_inv(height/10).lt(90)

        def S(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter S with a ChainTurtle
            :param height: height of letter S
            :param tls: a ChainTurtle
            """
            geo_fix = sine(20) - sine(272); radius = height * 0.27
            tls.rt(90).fd_inv(height*0.54).lt(90).fd_inv(height*0.54 + geo_fix*radius).lt(20).circle(radius, 0.7*360).circle(-radius, 0.7*360).pu().circle(-radius, 0.3*360).rt(2).fd(37).lt(90).bk(height*0.54).pd()

        def T(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter T with a ChainTurtle
            :param height: height of letter T
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height*0.45).lt(90).fd(height).lt(90).fd(height*0.45).bk(height*0.9).bk_inv(height/10).rt(90).bk_inv(height)

        def U(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter U with a ChainTurtle
            :param height: height of letter U
            :param tls: a ChainTurtle
            """
            tls.fd_inv(height).rt(180).fd(height*0.7).circle(height*0.3, 180).fd(height*0.7).rt(90).fd_inv(height/10).lt(90).bk_inv(height)

        def V(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter V with a ChainTurtle
            :param height: height of letter V
            :param tls: a ChainTurtle
            """
            diagonal = height / sine(65)
            tls.fd_inv(height).rt(155).fd(diagonal).lt(130).fd(diagonal).rt(65).fd_inv(height/10).lt(90).bk_inv(height)

        def W(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter W with a ChainTurtle
            :param height: height of letter W
            :param tls: a ChainTurtle
            """
            side_a = height / sine(75); side_c = (height/2) / sine(75)
            tls.fd_inv(height).rt(165).fd(side_a).lt(150)
            tls.fd(side_c).rt(150).fd(side_c).lt(150).fd(side_a)
            tls.rt(75).fd_inv(height/10).lt(90).bk_inv(height)

        def X(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter X with a ChainTurtle
            :param height: height of letter X
            :param tls: a ChainTurtle
            """
            a_half = (height/2) / sine(55); side_b = sqrt((a_half **2) - (height/2)**2)
            tls.rt(35).fd(a_half *2).lt(125).fd_inv(side_b * 2).lt(125).fd(a_half *2).lt(55).fd_inv(height/10).lt(90)

        def Y(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter Y with a ChainTurtle
            :param height: height of letter Y
            :param tls: a ChainTurtle
            """
            side = (height*0.4) / sine(55); width = sqrt(side**2 - (height*0.4)**2); tls.rt(90).fd_inv(width).lt(90).fd((height*0.6)).rt(35).fd(side)
            tls.bk(side).lt(70).fd(side).rt(35).bk_inv(height).rt(90).fd_inv(2 * width + height/10).lt(90)

        def Z(height: Real, tls: ChainTurtle) -> None:
            """
            Draws the letter Z with a ChainTurtle
            :param height: height of letter Z
            :param tls: a ChainTurtle
            """
            side_a = height / sine(50); side_b = sqrt(side_a**2 - height**2)
            tls.fd_inv(height).rt(90).fd(side_b).rt(130).fd(side_a).lt(130).fd(side_b).fd_inv(height/10).lt(90)

    @class_decorator(alphabet_method)
    class Punctuation:
        def space(height: Real, tls: ChainTurtle) -> None:
            """
            Traces an invisible space with a ChainTurtle
            :param height: to calculate the amount of space
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height/4).lt(90)

        def dot(height: Real, tls: ChainTurtle) -> None:
            """
            Draws a dot with given height and ChainTurtle
            :param height: height of the letters
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height/20).dot(height/10).fd_inv(height*0.15).lt(90)

        def exclamation(height: Real, tls: ChainTurtle) -> None:
            """
            Draws an exclamation mark with given height and turtle
            :param height: height of the letters
            :param tls: a ChainTurtle
            """
            tls.fd_inv(height/5); Shapes.rectangle_fill(height*0.8, height/10, -1, tls)
            tls.lt(180).fd_inv(height/10).circle_fill(height/20, 540).bk_inv(height/20).rt(90).fd_inv(height/10).lt(90)

        def question(height: Real, tls: ChainTurtle) -> None:
            """
            Draws a question mark with given height and ChainTurtle
            :param height: height of the letters
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height/10).lt(90).fd_inv(height).lt(36).begin_fill().fd(height/10).rt(90).circle(-height/5, 216)
            tls.circle(height/5, 216).rt(90).fd(height/10).rt(90).circle(-height/5, 216).circle(height/5, 216)
            tls.end_fill().lt(54).fd_inv(height).lt(90).fd_inv(height/10).dot(height/10).fd_inv(height/4).lt(90)

        def apostrophe(height: Real, tls: ChainTurtle) -> None:
            """
            Draws an apostrophe with given height and ChainTurtle
            :param height: height of the letters
            :param tls: a ChainTurtle
            """
            tls.fd_inv(height*0.7); Shapes.rectangle_fill(height*0.3, height/20, -1, tls)
            tls.rt(90).fd_inv(height*0.15).lt(90).bk_inv(height*0.7)

        def colon(height: Real, tls: ChainTurtle) -> None:
            """
            Draws a colon with given height and ChainTurtle
            :param height: height of the letters
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height*0.07).circle_fill(height*0.07, 360).lt(90).fd_inv(height*0.28)
            tls.rt(90).circle_fill(height*0.07, 360).fd_inv(height*0.17).lt(90).bk_inv(height*0.28)

        def comma(height: Real, tls: ChainTurtle) -> None:
            """
            Draws a comma with given height and ChainTurtle
            :param height: height of the letters
            :param tls: a ChainTurtle
            """
            tls.begin_fill().rt(180).fd(height*0.05).circle(-height*0.05, 90).lt(90).fd(height*0.05).lt(90)
            tls.circle(height*0.1, 90).fd(height*0.05).lt(90).fd(height*0.05).end_fill().rt(180).fd_inv(height*0.15).lt(90)

    @class_decorator(alphabet_method)
    class Shapes:
        def plus(height: Real, tls: ChainTurtle) -> None:
            """
            Draws a plus with given height and ChainTurtle
            :param height: height of the letters
            :param tls: a ChainTurtle
            """
            tls.rt(90).fd_inv(height / 4).lt(90).fd_inv(height / 2).rt(90)
            Shapes.lines(height / 4, 4, tls)
            tls.fd_inv(height * 0.35).lt(90).bk_inv(height / 2)


        def equals(height: Real, tls: ChainTurtle) -> None:
            """
                Draws an equal sign with given height and ChainTurtle
                :param height: height of the letters
                :param tls: a ChainTurtle
                """
            tls.fd_inv(height * 0.3).rt(90).fd(height / 2).lt(90).fd_inv(height * 0.4).lt(90).fd(height / 2).bk_inv(height * 0.6).rt(90).bk_inv(height * 0.7)


        def times(height: Real, tls: ChainTurtle) -> None:
            """
                Draws a multiplication sign with given height and ChainTurtle
                :param height: height of the letters
                :param tls: a ChainTurtle
                """
            side = sine(45) * height / 4
            tls.fd_inv(height / 2).rt(90).fd_inv(height / 2).rt(45)
            Shapes.lines(height / 4, 4, tls)
            tls.lt(45).fd_inv(side + height / 10).lt(90).bk_inv(height / 2)


        def minus(height: Real, tls: ChainTurtle) -> None:
            """
                Draws a minus sign with given height and ChainTurtle
                :param height: height of the letters
                :param tls: a ChainTurtle
                """
            tls.fd_inv(height / 2).rt(90).fd(height / 2).fd_inv(height / 10).lt(90).bk_inv(height / 2)


        def underline(height: Real, tls: ChainTurtle) -> None:
            """
                Draws an underline with given height and ChainTurtle
                :param height: height of the letters
                :param tls: a ChainTurtle
                """
            tls.rt(90).fd(height / 2).fd_inv(height / 10).lt(90)


        def heart(height: Real, tls: ChainTurtle) -> None:
            """
                Draws a heart with given height and ChainTurtle
                :param height: height of the letters
                :param tls: a ChainTurtle
                """
            tls.rt(90).fd_inv(height * 0.6).lt(135).begin_fill().fd(height * 0.65)
            tls.circle(-height * 0.325, 180).lt(90).circle(-height * 0.325, 180)
            tls.fd(height * 0.65).end_fill().lt(135).fd_inv(height * 0.65).lt(90)


        def star(height: Real, tls: ChainTurtle) -> None:
            """
                Draws a star with given height and ChainTurtle
                :param height: height of the letters
                :param tls: a ChainTurtle
                """
            direction = tls.heading()
            tls.rt(90).fd_inv(height).lt(90).fd(-1e-07).lt(17)
            for _ in range(5): tls.fd(height / sine(62)).lt(144)
            tls.seth(direction - 90).fd(height * 0.4).lt(90)

    @classmethod
    def list_alphabets(cls) -> dict[str, alphabet_function]:
        """
        Creates a dictionary with the functions in Alphabets and returns it
        :return: dictionary containing function names -> function
        """
        dictionary = classes_to_dict(cls.Letters, cls.Punctuation, cls.Shapes)
        name: str
        item: alphabet_function
        for name, item in vars(cls).items():
            if not isinstance(item, type) and isinstance(item, Callable):
                dictionary[name] = item

        return dictionary

def letters_functions() -> dict[str, alphabet_function]:
    """
    Takes all Letters in Alphabets.Letters and returns a dictionary
    :return: dictionary
    """
    return {
        name: func
        for name, func in classes_to_dict(Alphabets.Letters).items()
    }

letters_dict: dict[str, alphabet_function] = letters_functions()
# ALPHABET DICTIONARY
ALPHABETS: dict[str, alphabet_function] = {
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