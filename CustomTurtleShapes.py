from typing import TypeAlias
from collections.abc import Callable, Sequence
from .UniversalFunctions.TypingVariables import Real
from .UniversalFunctions.GetVariable import get_num
from .UniversalFunctions.HelperFunctions import helper, sine
from .UniversalFunctions.DecoratorArchive import class_decorator
from .UniversalFunctions.ClassToDict import classes_to_dict
from .TurtleSkeleton import tl

return_shape: TypeAlias = Sequence[tuple[Real,Real]] | None
user_shape_dict: TypeAlias = dict[str, Callable[[None], return_shape]]

@class_decorator(staticmethod)
class UserShape:
    def custom_circle() -> return_shape:
        """Creates a custom circle turtle shape"""
        radius: Real = get_num(float, "Enter the radius: ")
        tl.begin_poly()
        tl.circle(radius)
        tl.end_poly()
        return tl.get_poly()

    def custom_square() -> return_shape:
        """Creates a custom square turtle shape"""
        length: Real = helper.length_float()
        tl.begin_poly()
        for _ in range(4): tl.fd(length); tl.lt(90)
        tl.end_poly()
        return tl.get_poly()

    def custom_triangle() -> return_shape:
        """Creates a custom equilateral triangle turtle shape"""
        length: Real = helper.length_float()
        tl.begin_poly()
        for _ in range(3): tl.fd(length); tl.lt(120)
        tl.end_poly()
        return tl.get_poly()

    def custom_poly() -> return_shape:
        """Creates a custom regular polygon turtle shape"""
        length: Real = helper.length_float(); sides: int = helper.sides_num()

        radius = length / (2 * sine(180 / sides)); angle_to_right = (180 - (180 * (sides - 2)) / sides) / 2
        tl.begin_poly()
        tl.rt(angle_to_right); tl.circle(radius, 360, sides); tl.lt(angle_to_right)
        tl.end_poly()
        return tl.get_poly()

    def custom_SOD() -> return_shape:
        """Creates a custom star of David turtle shape"""
        side: Real = helper.length_float()
        tl.begin_poly()
        for _ in range(6):
            tl.pu(); tl.fd(side); tl.pd(); tl.rt(60)
            for _ in range(3): tl.fd(side); tl.rt(120)
            tl.lt(60); tl.pu(); tl.bk(side); tl.pd(); tl.lt(60)
        tl.end_poly()
        return tl.get_poly()

    @classmethod
    def _list_shapes(cls) -> user_shape_dict:
        """
        Creates a dictionary with the functions in Alphabets and returns it
        :return: dictionary containing function names -> function
        """
        return classes_to_dict(cls)

def get_UserShape_dict() -> user_shape_dict:
    """
    Takes all custom turtle functions in UserShape and returns a dictionary
    :return: dictionary
    """
    return {
        f"cm {name.removeprefix('custom_')}": func
        for name, func in classes_to_dict(UserShape).items()
        if not name.startswith("_")
    }

CUSTOM_SHAPES: user_shape_dict = get_UserShape_dict()