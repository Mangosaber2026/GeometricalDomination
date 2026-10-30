# ⚓ Anchor for this module: [[premade-shapes-anchor|premade_shapes.__init__.py]] 

#* 📝 Imports all available classes in [[#shapes-anchor|shapes.py]] 
from .shapes import Shapes
from .shapes_dictionaries import (
    SHAPES_LENGTH,
    # 🔗 Link to source code: [[#SHAPES-LENGTH-anchor|dictionary SHAPES_LENGTH]] 
    SHAPES_LENGTH_SIDES,
    # 🔗 Link to source code: [[#SHAPES-LENGTH-SIDES-anchor|dictionary SHAPES_LENGTH_SIDES]] 
    SHAPES_RADIUS,
    # 🔗 Link to source code: [[#SHAPES-RADIUS-anchor|dictionary SHAPES_RADIUS]] 
)

__all__ = [
    "Shapes",

    "SHAPES_LENGTH",
    "SHAPES_LENGTH_SIDES",
    "SHAPES_RADIUS"
]