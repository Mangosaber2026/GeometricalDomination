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
from .GD import *
from .ShapesMultiverse import *

__all__ = [
    "Alphabets",
    "ALPHABETS",
    "UserShape",
    "CUSTOM_SHAPES",
    "PATTERNS",
    "SU",
    "get_screen",
    "mainloop",
    "tls_color",
    "reset_tls",
    "UV",
    "t_now",
    "t_shape",
    "SHAPES_LENGTH",
    "SHAPES_RADIUS",
    "SHAPES_LENGTH_SIDES",
    "main",
    "user_drawing_ft",
    "ChainTurtle",
    "Command",
    "COMMANDS",
    "Shapes",

    "Drawing",
    "LinearFct",
    "SineWave",
    "CosineWave",
    "AbsoluteX",
    "QuadraticFct",
]