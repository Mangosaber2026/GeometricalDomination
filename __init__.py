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

from .Alphabets import Alphabets, ALPHABETS
from .CustomTurtleShapes import UserShape, CUSTOM_SHAPES
from .Designs import PATTERNS
from .GlobalFunctions import SU, tls_color, reset_tls
from .GlobalVariables import UV, t_now, t_shape
from .Shapes_Dictionary import SHAPES_LENGTH, SHAPES_RADIUS, SHAPES_LENGTH_SIDES
from .TurtleRunner import main, user_drawing_ft
from .TurtleSkeleton import ChainTurtle
from .UserCommands import Command, COMMANDS