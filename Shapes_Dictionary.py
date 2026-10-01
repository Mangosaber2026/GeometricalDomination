"""
This module contains dictionaries which contain all shape functions from the Shapes.py module.
"""

from .Shapes import Shapes
from collections.abc import Callable
from numbers import Real
from .TurtleSkeleton import ChainTurtle

type shapes_dict_type = dict[str, Callable[[Real, ChainTurtle], None]]

# DICTIONARY: SHAPES REQUIRING LENGTH
SHAPES_LENGTH: shapes_dict_type = {
    "tri": Shapes.triangle_ft,
    "tri fill": Shapes.triangle_fill,
    "tri half": Shapes.triangle_half,
    "square": Shapes.square,
    "square fill": Shapes.square_fill,
    "square half": Shapes.square_half,
    "hexagon": Shapes.hexagon_ft,
    "sod": Shapes.SOD,
    "sod fill": Shapes.SOD_fill,
    "flower tri": Shapes.hexaflower_tri,
    "triangle": Shapes.triangle_ft,
}

# DICTIONARY: SHAPES REQUIRING LENGTH + SIDES
SHAPES_LENGTH_SIDES: dict[str, Callable[[Real, int, ChainTurtle], None]] = {
    "poly": Shapes.polygon,
    "poly fill": Shapes.polygon_fill,
}

# DICTIONARY: SHAPES REQUIRING RADIUS
SHAPES_RADIUS: shapes_dict_type = {
    "circle": Shapes.circle_ft,
    "circle fill": Shapes.circle_filler,
    "hexa flower": Shapes.hexa_flower,
    "lotus": Shapes.lotus_flower,
}