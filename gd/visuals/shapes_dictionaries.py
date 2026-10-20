from .shapes import Shapes


#* DICTIONARY: SHAPES REQUIRING LENGTH, [[Shapes]]
SHAPES_LENGTH = {
    "tri": Shapes.triangle,
    "tri fill": Shapes.triangle_fill,
    "tri half": Shapes.triangle_half,
    "square": Shapes.square,
    "square fill": Shapes.square_fill,
    "square half": Shapes.square_half,
    "hexagon": Shapes.hexagon,
    "sod": Shapes.SOD,
    "sod fill": Shapes.SOD_fill,
    "flower tri": Shapes.hexaflower_tri,
    "triangle": Shapes.triangle,
}

#* DICTIONARY: SHAPES REQUIRING LENGTH + SIDES, [[Shapes]]
SHAPES_LENGTH_SIDES = {
    "poly": Shapes.polygon,
    "poly fill": Shapes.polygon_fill,
}

#* DICTIONARY: SHAPES REQUIRING RADIUS, [[Shapes]]
SHAPES_RADIUS = {
    "circle": Shapes.circle,
    "circle fill": Shapes.circle_filler,
    "hexa flower": Shapes.hexa_flower,
    "lotus": Shapes.lotus_flower,
}