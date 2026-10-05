"""
This module contains a collection of classes and functions for drawing/rendering or calculating
mathematical functions.
"""

from ..GD.GlobalFunctions import SU, mainloop, get_screen, tls_color
from numbers import Real
import UF as uf
import numpy as np
from typing import Final, Literal
from ..GD.Shapes import Shapes


type list_xy = tuple[list[Real], list[Real]]

class Drawing:
    """Parent class for drawing/rendering mathematical functions."""
    def __init__(self, domain: tuple[Real, Real, int]) -> None:
        """
        Takes the start and end values of desired domain
        :param domain: tuple of start and end values (real numbers)
        """
        uf.SequenceValidate(Real, Real, int)(domain, name="domain")
        self.domain = domain
        self.start, self.end, self.steps = self.domain

    def x_val(self) -> list[Real]:
        return np.linspace(self.start, self.end, self.steps+1).tolist()

    @staticmethod
    def render(coordinates: list_xy) -> None:
        """
        Renders the function produced by the provided generator function.

        Initiates the turtle screen before drawing to make sure screen configurations are applied appropriately.
        :param coordinates: tuple containing 2 lists, 1st with x values, 2nd with y values
        :return: None
        """
        name: Final[Literal["coordinates"]] = "coordinates"
        uf.TypeValidate(tuple)(coordinates, name)
        uf.SequenceValidate(list, list,
                            callable_items=(uf.SequenceValidate(Real, ...),)
                            )(coordinates, name)
        get_screen()
        xval, yval = coordinates
        turtle = tls_color(tl_num=2)

        Shapes.lines(700, 4, turtle[1])
        for x, y in zip(xval, yval):
            turtle[0].setpos(x, y)

        SU()
        mainloop()

    def draw(self) -> None:
        """
        Generate and render the drawing for this class.
        :return: None
        """
        self.render(self.generate())

class LinearFct(Drawing):
    def __init__(self, domain: tuple[Real, Real, int], k: Real, d: Real) -> None:
        super().__init__(domain)
        uf.TypeValidate(Real)(k, name="k")
        uf.TypeValidate(Real)(d, name="d")
        self.k, self.d = k, d

    def generate(self) -> list_xy:
        x_val = self.x_val()
        y_val = [self.k * x + self.d for x in x_val]
        return x_val, y_val


class SineWave(Drawing):
    """Class for drawing a sine wave."""
    def generate(self) -> list_xy:
        """
        Generate the coordinates of the sine wave.

        >>> coordinates = SineWave((0, 30, 1)).generate()
        ([0.0, 30.0], [0.0, 49.99999999999999])

        :return: list of coordinates of the sine wave (tuple of x and y values).
        """
        x_val = self.x_val()
        y_val = [100 * uf.sine(x) for x in x_val]
        return x_val, y_val

class CosineWave(Drawing):
    """Class for drawing a cosine wave."""
    def generate(self) -> list_xy:
        """
        Generate the coordinates of the cosine wave.
        :return: list of coordinates of the cosine wave (tuple of x and y values)
        """
        x_val = self.x_val()
        y_val = [100 * uf.cosine(x) for x in x_val]
        return x_val, y_val

class AbsoluteX(Drawing):
    """Class for drawing an absolute x value."""
    def generate(self) -> list_xy:
        """
        Generate the coordinates of the absolute x value.
        :return: list of coordinates of the absolute x value (tuple of x and y values).
        """
        x_val = self.x_val()
        y_val = [100 * abs(x) for x in x_val]
        return x_val, y_val

class QuadraticFct(Drawing):
    """Class for drawing a quadratic function."""
    def __init__(
            self,
            domain: tuple[Real, Real, int],
            a: Real, b: Real, c: Real,
    ) -> None:
        super().__init__(domain)
        uf.SequenceValidate(Real, ...)((a, b, c), name="variables")
        self.a, self.b, self.c = a, b, c

    def generate(self) -> list_xy:
        x_val = self.x_val()
        y_val = [(self.a*x**2) + (self.b*x) + self.c for x in x_val]
        return x_val, y_val