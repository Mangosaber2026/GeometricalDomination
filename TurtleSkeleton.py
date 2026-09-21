import turtle as tl
from collections.abc import Callable
from .UniversalFunctions.ClassToDict import class_to_dict


class ChainTurtle(tl.Turtle):
    """This class adds chaining functionality to turtle.Turtle"""
    def fd(self, distance): super().fd(distance); return self
    def fd_inv(self,distance): self.pu().fd(distance).pd(); return self
    def bk(self, distance): super().bk(distance); return self
    def bk_inv(self,distance): self.pu().bk(distance).pd(); return self
    def rt(self, angle): super().rt(angle); return self
    def lt(self, angle): super().lt(angle); return self
    def setpos(self, x_val, y_val): super().setpos(x_val, y_val); return self
    def pu(self): super().pu(); return self
    def pd(self): super().pd(); return self
    def seth(self, direction): super().seth(direction); return self
    def home(self): super().home(); return self
    def home_inv(self): self.pu().home().pd(); return self
    def begin_fill(self): super().begin_fill(); return self
    def end_fill(self): super().end_fill(); return self
    def circle(self, radius, extent=None, steps=None): super().circle(radius, extent, steps); return self
    def circle_fill(self,radius,angle=None,sides=None): self.begin_fill().circle(radius,angle,sides).end_fill(); return self
    def dot(self, radius): self.begin_fill().circle(radius).end_fill(); return self
    def color(self,turtle_color): super().color(turtle_color); return self
    def teleport(self,x,y): super().teleport(x,y); return self
    def shape(self, shape_name): super().shape(shape_name); return self
    def undo(self): super().undo(); return self

    @classmethod
    def list_methods(cls) -> dict[str, Callable]:
        """
        Creates a dictionary with all ChainTurtle methods and returns it
        :return: dictionary
        """
        return class_to_dict(cls)