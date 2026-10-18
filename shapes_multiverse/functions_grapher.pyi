"""
This module contains a collection of classes and functions for drawing/rendering or calculating
mathematical functions.
"""

from numbers import Real


type ListXYType = tuple[list[Real], list[Real]]

type DomainType = tuple[Real, Real, int]


class Drawing:
   """
   Parent class for drawing/rendering mathematical functions.
   """

   def __init__(self, domain: DomainType) -> None:
      """
      Takes the start, end and steps value of desired domain.
      :param domain: tuple of start, end and steps value of desired domain
      """

   def x_val(self) -> list[Real]:
      """
      Returns the x values of desired domain.
      :return: list of x values
      """

   @staticmethod
   def render(coordinates: ListXYType) -> None:
      """
      Renders the function produced by the provided generator function.

      Initiates the turtle screen before drawing to make sure screen configurations are applied appropriately.
      :param coordinates: tuple containing 2 lists, 1st with x values, 2nd with y values
      :return: None
      """

   def draw(self) -> None:
      """
      Generate and render the drawing for this class.
      :return: None
      """

class LinearFct(Drawing):
   """
   This class contains methods for drawing/rendering linear functions.
   """

   def __init__(self,
                domain: DomainType,
                k: Real,
                d: Real
                ) -> None:
      """
      Takes the start and end values of desired domain.
      :param domain: tuple of desired domain
      :param k: scaling factor
      :param d: y-intercept
      """

   def generate(self) -> ListXYType:
      """
      Generates the coordinates of the points of the linear function created with the desired domain.
      :return: list of coordinates
      """

class SineWave(Drawing):
   """
   This class contains methods for drawing/rendering sine wave functions.
   """

   def generate(self) -> ListXYType:
      """
      Generates the coordinates of the points of the sine wave function created with the desired domain.
      :return: list of coordinates
      """

class CosineWave(Drawing):
   """
   This class contains methods for drawing/rendering cosine wave functions.
   """

   def generate(self) -> ListXYType:
      """
      Generates the coordinates of the points of the cosine wave function created with the desired domain.
      :return: list of coordinates
      """

class AbsoluteX(Drawing):
   """
   This class contains methods for drawing/rendering absolute x values.
   """

   def generate(self) -> ListXYType:
      """
      Generates the coordinates of the points of the absolute x values created with the desired domain.
      :return: list of coordinates
      """

class QuadraticFct(Drawing):
   """
   This class contains methods for drawing/rendering quadratic functions.
   """

   def __init__(
         self,
         domain: DomainType,
         a: Real,
         b: Real,
         c: Real,
   ) -> None:
      """
      Takes the start and end values of desired domain and the parameters a,b,and c.
      :param domain: tuple of start and end values of desired domain
      :param a: parameter a of a quadratic function
      :param b: parameter b of a quadratic function
      :param c: parameter c of a quadratic function
      :return: None
      """

   def generate(self) -> ListXYType:
      """
      Generates the coordinates of the points of the quadratic function created with the desired domain.
      :return: list of coordinates
      """
