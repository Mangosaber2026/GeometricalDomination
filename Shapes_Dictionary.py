from .UniversalFunctions.Shapes import Shapes

# DICTIONARY: SHAPES REQUIRING LENGTH
SHAPES_LENGTH = {
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
}

# DICTIONARY: SHAPES REQUIRING LENGTH + SIDES
SHAPES_LENGTH_SIDES = {
    "poly": Shapes.polygon,
    "poly fill": Shapes.polygon_fill,
}

# DICTIONARY: SHAPES REQUIRING RADIUS
SHAPES_RADIUS = {
    "circle": Shapes.circle_ft,
    "circle fill": Shapes.circle_filler,
    "hexa flower": Shapes.hexa_flower,
    "lotus": Shapes.lotus_flower,
}