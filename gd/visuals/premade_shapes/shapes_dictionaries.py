# ⚓ Anchor for this module: [[shapes-dictionaries-anchor|shapes_dictionaries.py]] 

from .shapes import Shapes

# ⚓ SHAPES_LENGTH anchor: [[SHAPES-LENGTH-anchor|dictionary SHAPES_LENGTH]] 
#* 📝 DICTIONARY: SHAPES REQUIRING LENGTH, [[#Shapes-anchor|class Shapes]] 
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

# ⚓ SHAPES_LENGTH_SIDES anchor: [[SHAPES-LENGTH-SIDES-anchor|dictionary SHAPES_LENGTH_SIDES]] 
#* 📝 DICTIONARY: SHAPES REQUIRING LENGTH + SIDES, [[#Shapes-anchor|class Shapes]] 
SHAPES_LENGTH_SIDES = {
    "poly": Shapes.polygon,
    "poly fill": Shapes.polygon_fill,
}

# ⚓ SHAPES_RADIUS anchor: [[SHAPES-RADIUS-anchor|dictionary SHAPES_RADIUS]] 
#* 📝 DICTIONARY: SHAPES REQUIRING RADIUS, [[#Shapes-anchor|class Shapes]] 
SHAPES_RADIUS = {
    "circle": Shapes.circle,
    "circle fill": Shapes.circle_filler,
    "hexa flower": Shapes.hexa_flower,
    "lotus": Shapes.lotus_flower,
}