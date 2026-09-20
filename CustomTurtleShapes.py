from typing import Sequence
from collections.abc import Callable
from .UniversalFunctions.TypingVariables import Real
from .UniversalFunctions.GetVariable import get_num
from .UniversalFunctions.HelperFunctions import helper, sine
from .UniversalFunctions.DecoratorArchive import class_decorator
from .UniversalFunctions.ClassToDict import class_to_dict
from .TurtleSkeleton import tl

return_shape = Sequence[tuple[float|int,float|int]] | None

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
    def list_shapes(cls) -> dict[str, Callable[[None], return_shape]]:
        """
        Creates a dictionary with the functions in Alphabets and returns it
        :return: dictionary containing function names -> function
        """
        return class_to_dict(cls)

CUSTOM_SHAPES: dict[str, Callable[[], return_shape]] = {
    "cm circle": UserShape.custom_circle,
    "cm square": UserShape.custom_square,
    "cm triangle": UserShape.custom_triangle,
    "cm poly": UserShape.custom_poly,
    "cm sod": UserShape.custom_SOD,
}