"""
This module contains the Alphabets class which provides a collection of functions for drawing English letters,
punctuation, and shapes (heart, star).
"""

from collections.abc import Callable
from numbers import Real


import TurtleExtension as tx


type AlphabetFunctionType = Callable[[Real, tx.ChainTurtle], None]

type AlphabetDictType = dict[str, AlphabetFunctionType]

type FullAlphabetDictType = dict[str, AlphabetFunctionType | Callable[[], FullAlphabetDictType]]


class Alphabets:
    """
    A collection of classes containing functions to draw the English alphabets, punctuation and shapes.
    """
    @staticmethod
    def A(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter A with a ChainTurtle.
        :param height: height of letter A
        :param tls: given ChainTurtle
        :return: None
        """

    @staticmethod
    def B(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter B with a ChainTurtle.
        :param height: height of letter B
        :param tls: given ChainTurtle
        :return: None
        """

    @staticmethod
    def C(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter C with a ChainTurtle.
        :param height: height of letter C
        :param tls: given ChainTurtle
        :return: None
        """

    @staticmethod
    def D(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter D with a ChainTurtle.
        :param height: height of letter D
        :param tls: given ChainTurtle
        :return: None
        """

    @staticmethod
    def E(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter E with a ChainTurtle.
        :param height: height of letter E
        :param tls: given ChainTurtle
        :return: None
        """

    @staticmethod
    def F(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter F with a ChainTurtle.
        :param height: height of letter F
        :param tls: given ChainTurtle
        :return: None
        """
    
    @staticmethod
    def G(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter G with a ChainTurtle.
        :param height: height of letter G
        :param tls: given ChainTurtle
        :return: None
        """

    @staticmethod
    def H(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter H with a ChainTurtle.
        :param height: height of letter H
        :param tls: given ChainTurtle
        :return: None
        """

    @staticmethod
    def I(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter I with a ChainTurtle.
        :param height: height of letter I
        :param tls: given ChainTurtle
        """
    
    @staticmethod
    def J(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter J with a ChainTurtle.
        :param height: height of letter J
        :param tls: given ChainTurtle
        :return: None
        """
    
    @staticmethod
    def K(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter K with a ChainTurtle.
        :param height: height of letter K
        :param tls: given ChainTurtle
        :return: None
        """
    
    @staticmethod
    def L(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter L with a ChainTurtle.
        :param height: height of letter L
        :param tls: given ChainTurtle
        :return: None
        """

    @staticmethod
    def M(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter M with a ChainTurtle.
        :param height: height of letter M
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def N(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter N with a ChainTurtle.
        :param height: height of letter N
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def O(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter O with a ChainTurtle.
        :param height: height of letter O
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def P(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter P with a ChainTurtle.
        :param height: height of letter P
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def Q(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter Q with a ChainTurtle.
        :param height: height of letter Q
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def R(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter R with a ChainTurtle.
        :param height: height of letter R
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def S(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter S with a ChainTurtle.
        :param height: height of letter S
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def T(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter T with a ChainTurtle.
        :param height: height of letter T
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def U(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter U with a ChainTurtle.
        :param height: height of letter U
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def V(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter V with a ChainTurtle.
        :param height: height of letter V
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def W(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter W with a ChainTurtle.
        :param height: height of letter W
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def X(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter X with a ChainTurtle.
        :param height: height of letter X
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def Y(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter Y with a ChainTurtle.
        :param height: height of letter Y
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def Z(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws the letter Z with a ChainTurtle.
        :param height: height of letter Z
        :param tls: a ChainTurtle
        :return: None
        """

# =========================
# ====== PUNCTUATION ======
# =========================

    @staticmethod
    def space(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Traces an invisible space with a ChainTurtle.
        :param height: to calculate the amount of space
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def dot(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a dot with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def exclamation(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws an exclamation mark with given height and turtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def question(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a question mark with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def apostrophe(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws an apostrophe with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def colon(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a colon with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def comma(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a comma with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

# ====================
# ====== SHAPES ======
# ====================

    @staticmethod
    def plus(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a plus with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def equals(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws an equal sign with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def times(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a multiplication sign with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def minus(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a minus sign with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def underline(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws an underline with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @staticmethod
    def heart(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a heart with given height and ChainTurtle
        :param height: height of the letters
        :param tls: a ChainTurtle
        """

    @staticmethod
    def star(height: Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a star with given height and ChainTurtle.
        :param height: height of the letters
        :param tls: a ChainTurtle
        :return: None
        """

    @classmethod
    def list_alphabets(cls) -> FullAlphabetDictType:
        """
        Creates a dictionary with the functions in Alphabets and returns it.
        :return: dictionary containing function names -> function
        """

def letters_functions() -> AlphabetDictType:
    """
    Takes all Letters in Alphabets.Letters and returns a dictionary.
    :return: letter dictionary
    """

letters_dict: AlphabetDictType

ALPHABETS: AlphabetDictType