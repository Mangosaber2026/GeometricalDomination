from typing import Any, Annotated
from collections.abc import Generator
from math import sqrt, sin, radians
from .GetVariable import get_num
from .DecoratorArchive import cls_deco_superposition
from .TypingVariables import Real
from .ClassToDict import classes_to_dict
from .Validators.FctInputValidators import validation_deco


@cls_deco_superposition(staticmethod)
class HelperFunctions:

    def intervals_f() -> Real:
        """Asks the user for rational intervals"""
        interval_num: float = get_num(float, "Enter intervals(ℚ>0): ", MIN=0)
        return interval_num

    def length_float() -> Real:
        """Asks the user for rational lengths"""
        length: float = get_num(float, "Enter side length(ℚ>0): ", MIN=0)
        return length

    def radius_float() -> Real:
        """Asks the user for rational radius"""
        radius: float = get_num(float, "Enter radius(ℚ>0): ", MIN=0)
        return radius

    def object_num() -> int:
        """Asks the user for the number of objects"""
        object_count: int = get_num(int, "Enter object count(ℕ≥1): ", MIN=1)
        return object_count

    def sides_num() -> int:
        """Asks the user for the number of sides"""
        sides: int = get_num(int, "Enter sides count(ℕ≥3): ", MIN=3)
        return sides

    def row_num() -> int:
        """Asks the user for the number of rows"""
        row_count: int = get_num(int, "Enter row count(ℕ≥1): ", MIN=1)
        return row_count

    def row_pair() -> int:
        """Asks the user for the number of pairs of rows"""
        row_count: int = get_num(int, "Enter row pairs count(ℕ≥1): ", MIN=1)
        return row_count

    @validation_deco
    def diameter_sq(length: Real) -> tuple[Real,Real]:
        """
        Calculates the diameter of a square with given length
        :return: diameter, diameter/2
        """
        if length <= 0:
            raise ValueError("Length must be greater than 0")

        diameter: float = length*sqrt(2); d_half: Real = diameter / 2
        return diameter, d_half

    def x_ft() -> Real:
        """Asks the user for the x value (on the coordinate system)"""
        x_val: float = get_num(float, "Enter x value: ")
        return x_val

    def y_ft() -> Real:
        """Asks the user for the y value (on the coordinate system)"""
        y_val: float = get_num(float, "Enter y value: ")
        return y_val

    def list_helperfunctions() -> dict:
        """
        Creates a dictionary with all helper functions
        :return: dictionary
        """
        return classes_to_dict(HelperFunctions)

helper = HelperFunctions

@validation_deco
def sine(angle: Real) -> Real:
    """
    Calculates the sine of a given angle
    :param angle: value required in degrees
    """
    return sin(radians(angle))

def range_f(start: Real,stop: Annotated[Real, "stop >= start"],step: Annotated[Real, "step > 0"]) -> Generator[Real,Any,None]:
    """
    Lets the user choose Real inputs for start, stop and step
    :param start: start value; Real number
    :param stop: stop value; Real number >= start
    :param step: step value; Real number > 0
    """
    if not all(isinstance(x, Real) for x in [start, stop, step]):
        raise TypeError("All inputs must be real numbers!")

    if stop < start:
        raise ValueError("Stop value must be greater than start value!")
    if step <= 0:
        raise ValueError("Step value must be greater than 0!")

    while start < stop:
        yield start
        start += step