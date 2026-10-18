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

from .Visuals import (
    Alphabets,
    ALPHABETS,
    letters_functions,
    Designs,
    turtles,
    get_Patterns_dict,
    PATTERNS,
    Shapes,
    SHAPES_LENGTH,
    SHAPES_RADIUS,
    SHAPES_LENGTH_SIDES,
)
from .ProgramExecutors import (
    main,
    user_drawing_ft,
)
from .UserFeatures import (
    Command,
    COMMANDS,
)

__all__ = [
    "Alphabets",
    "ALPHABETS",
    "letters_functions",
    "Designs",
    "turtles",
    "get_Patterns_dict",
    "PATTERNS",
    "Shapes",
    "SHAPES_LENGTH",
    "SHAPES_RADIUS",
    "SHAPES_LENGTH_SIDES",
    "main",
    "user_drawing_ft",
    "Command",
    "COMMANDS",
    "Shapes",
]