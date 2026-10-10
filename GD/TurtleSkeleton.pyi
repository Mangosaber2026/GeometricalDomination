from numbers import Real
from collections.abc import Callable


class ChainTurtle:
    """This class adds chaining functionality to turtle.Turtle"""
    def fd(self, distance: Real) -> ChainTurtle:
        """
        Makes the turtle go forward with trace
        :param distance: distance in pixels
        """
        ...
    def fd_inv(self, distance: Real) -> ChainTurtle:
        """
        Makes the turtle go forward with no trace
        :param distance: distance in pixels
        """
        ...
    def bk(self, distance: Real) -> ChainTurtle:
        """
        Makes the turtle go backwards with trace
        :param distance: distance in pixels
        """
        ...
    def bk_inv(self, distance: Real) -> ChainTurtle:
        """
        Makes the turtle go backward with no trace
        :param distance: distance in pixels
        """
        ...
    def rt(self, angle: Real) -> ChainTurtle:
        """
        Makes the turtle turn right
        :param angle: angle in degrees
        """
        ...
    def lt(self, angle: Real) -> ChainTurtle:
        """
        Makes the turtle turn left
        :param angle: angle in degrees
        """
        ...
    def setpos(self, x_val: Real, y_val: Real) -> ChainTurtle:
        """
        Makes the turtle go to a specific position with a trace
        :param x_val: x position in pixels
        :param y_val: y position in pixels
        """
        ...
    def pu(self) -> ChainTurtle:
        """Puts the pen down to leave a trace"""
        ...
    def pd(self) -> ChainTurtle:
        """Puts the pen up to not leave a trace"""
        ...
    def seth(self, direction: Real) -> ChainTurtle:
        """
        Sets the direction of the turtle starting East, going counterclockwise
        :param direction: direction in degrees
        """
    def home(self) -> ChainTurtle:
        """Sets the position of the turtle to home (0, 0) with trace, heading = 0"""
        ...
    def home_inv(self) -> ChainTurtle:
        """Sets the position of the turtle to home (0, 0) without trace, heading = 0"""
        ...
    def begin_fill(self) -> ChainTurtle:
        """Makes the turtle begin fill for a closed shape"""
        ...
    def end_fill(self) -> ChainTurtle:
        """Ends the turtle fill for a closed shape, therefore fills the shapes"""
        ...
    def circle(self,
               radius: Real,
               extent: Real | None = None,
               steps: int = None) -> ChainTurtle:
        """
        Makes the turtle draw a circle
        :param radius: radius in pixels
        :param extent: extent in degrees
        :param steps: number of sides
        """
        ...
    def circle_fill(self,
                    radius: Real,
                    angle: Real | None = None,
                    sides: int = None) -> ChainTurtle:
        """
        Makes the turtle draw a circle and fills it
        :param radius: radius in degrees
        :param angle: angle in degrees
        :param sides: number of sides
        """
        ...
    def dot(self, radius: Real) -> ChainTurtle:
        """
        Makes the turtle draw a colored dot
        :param radius: radius in pixels
        """
        ...
    def color(self, turtle_color: str) -> ChainTurtle:
        """
        Lets the user change the color of the turtle trace and turtle color itself
        :param turtle_color: valid turtle color
        """
        ...
    def teleport(self, x: Real, y: Real, *, fill_gap: bool = False) -> ChainTurtle:
        """
        Makes the turtle to go a specific coordinate with no trace
        :param x: x position in pixels
        :param y: y position in pixels
        """
        ...
    def shape(self, shape_name: str) -> ChainTurtle:
        """
        Changes the shape of the turtle shape
        :param shape_name: name of the shape
        """
        ...
    def undo(self) -> ChainTurtle:
        """Undoes the last turtle command"""
        ...
    @classmethod
    def list_methods(cls) -> dict[str, Callable]:
        """
        Creates a dictionary with all ChainTurtle methods and returns it
        :return: dictionary
        """
        ...