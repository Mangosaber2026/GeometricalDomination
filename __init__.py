"""
Welcome to GeometricalDomination!!!

Developer: Miah M. Sabiq

This is a Domain-Specific API (DSAPI) with an embedded DSL made for Python 3.14.6 or later versions.

This software combines conventional Turtle drawings with an ever-increasingly complex architecture built around it,
you are permitted to use all reusable functions as you wish, but with ONE CONDITION:

The developer must be given credit for the use of their functions somewhere in the program where any external user can
easily see it.

Otherwise, hopefully you enjoy this masterpiece!
"""
from .GD.Alphabets import Alphabets, ALPHABETS
from .GD.CustomTurtleShapes import UserShape, CUSTOM_SHAPES
from .GD.Designs import PATTERNS
from .GD.GlobalFunctions import SU, get_screen, mainloop, tls_color, reset_tls
from .GD.GlobalVariables import UV, t_now, t_shape
from .GD.Shapes_Dictionary import SHAPES_LENGTH, SHAPES_RADIUS, SHAPES_LENGTH_SIDES
from .GD.TurtleRunner import main, user_drawing_ft
from .GD.TurtleSkeleton import ChainTurtle
from .GD.UserCommands import Command, COMMANDS
from .GD.Shapes import Shapes