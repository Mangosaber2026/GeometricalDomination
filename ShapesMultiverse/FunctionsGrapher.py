from ..UniversalFunctions.HelperFunctions import sine, cosine
from ..GlobalFunctions import SU, mainloop, get_screen, tls_color
from ..UniversalFunctions.DecoratorArchive import cls_deco_superposition
from ..UniversalFunctions.TypingVariables import Real
from typing import TypeAlias


list_xy: TypeAlias = tuple[list[Real], list[Real]]

class Drawing:
    """Parent class for drawing/rendering mathematical functions."""
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

    @classmethod
    def draw(cls) -> None:
        """
        Generate and render the drawing for this class.
        :return: None
        """
        cls._render(cls.generate)

@cls_deco_superposition(staticmethod)
class LinearFct(Drawing):
    def generate() -> list_xy:
        x_val = [x/10 for x in range(0, 4001)]
        y_val = [3*x + 4 for x in x_val]

        return x_val, y_val


@cls_deco_superposition(staticmethod)
class SineWave(Drawing):
    """Class for drawing a sine wave."""
    def generate() -> list_xy:
        """
        Generate the coordinates of the sine wave.
        :return: list of coordinates of the sine wave (tuple of x and y values).
        """
        x_val = [x/10 for x in range(0, 4001)]
        y_val = [100 * sine(x) for x in x_val]

        return x_val, y_val

@cls_deco_superposition(staticmethod)
class CosineWave(Drawing):
    """Class for drawing a cosine wave."""
    def generate() -> list_xy:
        """
        Generate the coordinates of the cosine wave.
        :return: list of coordinates of the cosine wave (tuple of x and y values
        """
        x_val = [x/10 for x in range(0, 4001)]
        y_val = [100 * cosine(x) for x in x_val]

        return x_val, y_val