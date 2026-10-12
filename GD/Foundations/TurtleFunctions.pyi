"""
This module contains the class TurtleFct which lets the user change the turtle shape to a customized one.
"""

from ..TurtleHeart import ChainTurtle


class TurtleFct:
    """
    This class contains a function that lets users change the shape of the turtles that will be created in the future with tls_color.
    """
    @classmethod
    def change_shape(cls, tls_num: ChainTurtle|None = None) -> ChainTurtle | str:
        """
        This function lets the user choose different turtles shapes, including a custom option.
        :param tls_num: ChainTurtle() or None
        :return: ChainTurtle() if tls_num is a ChainTurtle(), otherwise None
        """
        ...

    @staticmethod
    def user_tls_shape_ft(tls_num: ChainTurtle | None = None) -> ChainTurtle | str:
        """
        This function lets the user create custom turtle shapes.
        :param tls_num: ChainTurtle() or None
        :return: ChainTurtle() if tls_num is a ChainTurtle(), otherwise None
        """
        ...