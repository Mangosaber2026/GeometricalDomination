from .alphabets import (
    ALPHABETS,
    Alphabets,
    letters_functions,
)

from .designs import (
    PATTERNS,
    Designs,
    get_Patterns_dict,
    turtles,
)

from .shapes import (
    Shapes,
)

from .shapes_dictionaries import (
    SHAPES_LENGTH,
    SHAPES_LENGTH_SIDES,
    SHAPES_RADIUS,
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
    "SHAPES_LENGTH_SIDES",
    "SHAPES_RADIUS",
]