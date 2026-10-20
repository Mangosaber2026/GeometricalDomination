#* Imports the class, function and dictionary available in [[alphabets.py]]
from .alphabets import (
    ALPHABETS,
    Alphabets,
    letters_functions,
)

#* Imports the class, functions and dictionary available in [[designs.py]]
from .designs import (
    PATTERNS,
    Designs,
    get_Patterns_dict,
    turtles,
)

#* Imports the class available in [[shapes.py]]
from .shapes import (
    Shapes,
)

#* Imports the dictionaries available in [[shapes_dictionaries.py]]
from .shapes_dictionaries import (
    SHAPES_LENGTH,
    SHAPES_LENGTH_SIDES,
    SHAPES_RADIUS,
)


#* Specifies all functions, dictionaries and classes available through wildcard import
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
    "SHAPES_LENGTH_SIDES",
    "SHAPES_RADIUS",
]