"""
This module contains the class ChainTurtle() which is the foundational object around which this entire software has been made.
"""

import turtle as tl
from collections.abc import Callable
import UF as uf


class ChainTurtle(tl.Turtle):
    """This class adds chaining functionality to turtle.Turtle"""
    def fd(self, distance):
        """
        Makes the turtle go forward
        :param distance: distance in pixels
        """
        super().fd(distance); return self
    def fd_inv(self,distance):
        """
        Makes the turtle go forward with no trace
        :param distance: distance in pixels
        """
        self.pu().fd(distance).pd(); return self
    def bk(self, distance):
        """
        Makes the turtle go backwards
        :param distance: distance in pixels
        """
        super().bk(distance); return self
    def bk_inv(self,distance):
        """
        Makes the turtle go backward with no trace
        :param distance: distance in pixels
        """
        self.pu().bk(distance).pd(); return self
    def rt(self, angle):
        """
        Makes the turtle turn right
        :param angle: angle in degrees
        """
        super().rt(angle); return self
    def lt(self, angle):
        """
        Makes the turtle turn left
        :param angle: angle in degrees
        """
        super().lt(angle); return self
    def setpos(self, x_val, y_val):
        """
        Makes the turtle go to a specific position with a trace
        :param x_val: x position in pixels
        :param y_val: y position in pixels
        """
        super().setpos(x_val, y_val); return self
    def pu(self):
        """Puts the pen down to leave a trace"""
        super().pu(); return self
    def pd(self):
        """Puts the pen up to not leave a trace"""
        super().pd(); return self
    def seth(self, direction):
        """
        Sets the direction of the turtle starting East, going counterclockwise
        :param direction: direction in degrees
        """
        super().seth(direction); return self
    def home(self):
        """Sets the position of the turtle to home (0, 0) with trace, heading = 0"""
        super().home(); return self
    def home_inv(self):
        """Sets the position of the turtle to home (0, 0) without trace, heading = 0"""
        self.pu().home().pd(); return self
    def begin_fill(self):
        """Makes the turtle begin fill for a closed shape"""
        super().begin_fill(); return self
    def end_fill(self):
        """Ends the turtle fill for a closed shape, therefore fills the shapes"""
        super().end_fill(); return self
    def circle(self, radius, extent=None, steps=None):
        """
        Makes the turtle draw a circle
        :param radius: radius in pixels
        :param extent: extent in degrees
        :param steps: number of sides
        """
        super().circle(radius, extent, steps); return self
    def circle_fill(self,radius,angle=None,sides=None):
        """
        Makes the turtle draw a circle and fills it
        :param radius: radius in degrees
        :param angle: angle in degrees
        :param sides: number of sides
        """
        self.begin_fill().circle(radius,angle,sides).end_fill(); return self
    def dot(self, radius):
        """
        Makes the turtle draw a colored dot
        :param radius: radius in pixels
        """
        self.begin_fill().circle(radius).end_fill(); return self
    def color(self, turtle_color):
        """
        Lets the user change the color of the turtle trace and turtle color itself
        :param turtle_color: valid turtle color
        """
        super().color(turtle_color); return self
    def teleport(self, x, y):
        """
        Makes the turtle to go a specific coordinate with no trace
        :param x: x position in pixels
        :param y: y position in pixels
        """
        super().teleport(x,y); return self
    def shape(self, shape_name):
        """
        Changes the shape of the turtle shape
        :param shape_name: name of the shape
        """
        super().shape(shape_name); return self
    def undo(self):
        """Undoes the last turtle command"""
        super().undo(); return self

    @classmethod
    def list_methods(cls) -> dict[str, Callable]:
        """
        Creates a dictionary with all ChainTurtle methods and returns it
        :return: dictionary
        """
        return uf.classes_to_dict(cls)