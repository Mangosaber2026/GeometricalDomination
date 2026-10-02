from ..UniversalFunctions.HelperFunctions import sine, cosine, range_f
from ..GlobalFunctions import SU, mainloop, get_screen, tls_color
from numbers import Real
from ..UniversalFunctions.Validators.ValidationClasses import TupleValidate


type list_xy = tuple[list[Real], list[Real]]

class Drawing:
    """Parent class for drawing/rendering mathematical functions."""
    def __init__(self, domain: tuple[Real, Real, Real]) -> None:
        """
        Takes the start and end values of desired domain
        :param domain: tuple of start and end values (real numbers)
        """
        TupleValidate(Real, Real, Real)(domain, name="domain")
        self.domain = domain
        self.start, self.end, self.steps = domain

    @staticmethod
    def _render(generator_func) -> None:
        """
        Renders the function produced by the provided generator function.

        Initiates the turtle screen before drawing to make sure screen configurations are applied appropriately.
        :param generator_func: given generator function
        :return: None
        """
        get_screen()
        xval, yval = generator_func()
        turtle = tls_color(tl_num=1)

        for x, y in zip(xval, yval):
            turtle[0].setpos(x, y)

        SU()
        mainloop()

    def draw(self) -> None:
        """
        Generate and render the drawing for this class.
        :return: None
        """
        self._render(self.generate)

class LinearFct(Drawing):
    def generate(self) -> list_xy:
        x_val = [x/10 for x in range_f(self.start, self.end, self.steps)]
        y_val = [3*x + 4 for x in x_val]

        return x_val, y_val


class SineWave(Drawing):
    """Class for drawing a sine wave."""
    def generate(self) -> list_xy:
        """
        Generate the coordinates of the sine wave.
        :return: list of coordinates of the sine wave (tuple of x and y values).
        """
        x_val = [x/10 for x in range_f(self.start, self.end, self.steps)]
        y_val = [100 * sine(x) for x in x_val]

        return x_val, y_val

class CosineWave(Drawing):
    """Class for drawing a cosine wave."""
    def generate(self) -> list_xy:
        """
        Generate the coordinates of the cosine wave.
        :return: list of coordinates of the cosine wave (tuple of x and y values)
        """
        x_val = [x/10 for x in range_f(self.start, self.end, self.steps)]
        y_val = [100 * cosine(x) for x in x_val]

        return x_val, y_val

class AbsoluteX(Drawing):
    """Class for drawing an absolute x value."""
    def generate(self) -> list_xy:
        """
        Generate the coordinates of the absolute x value.
        :return: list of coordinates of the absolute x value (tuple of x and y values).
        """
        x_val = [x/10 for x in range_f(self.start, self.end, self.steps)]
        y_val = [100 * abs(x) for x in x_val]
        return x_val, y_val