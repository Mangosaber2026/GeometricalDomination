"""
This module contains the class Usershape which contains functions to make a customized turtle shape.
"""

from numbers import Real
from collections.abc import Callable, Sequence


type return_shape = Sequence[tuple[Real,Real]] | None
type user_shape_dict = dict[str, Callable[[], return_shape]]

class UserShape:
    """
    This class contains different custom turtle shape maker functions
    """
    @staticmethod
    def custom_circle() -> return_shape:
        """
        Creates a custom circle turtle shape.
        :return: the custom shape
        """
        ...

    @staticmethod
    def custom_square() -> return_shape:
        """
        Creates a custom square turtle shape.
        :return: the custom shape
        """
        ...

    @staticmethod
    def custom_triangle() -> return_shape:
        """
        Creates a custom equilateral triangle turtle shape.
        :return: the custom shape
        """
        ...

    @staticmethod
    def custom_poly() -> return_shape:
        """
        Creates a custom regular polygon turtle shape.
        :return: the custom shape
        """
        ...

    @staticmethod
    def custom_SOD() -> return_shape:
        """
        Creates a custom star of David turtle shape.
        :return: the custom shape
        """
        ...

    @classmethod
    def _list_shapes(cls) -> user_shape_dict:
        """
        Creates a dictionary with the functions in UserShape and returns it
        :return: dictionary containing function names -> function
        """
        ...

def get_UserShape_dict() -> user_shape_dict:
    """
    Takes all custom turtle functions in UserShape and returns a dictionary with them
    :return: dictionary mapping function names to functions
    """
    ...

CUSTOM_SHAPES: user_shape_dict