# ⚓ Anchor for this module: [[premade-shapes-anchor|premade_shapes.__init__.py]] 

#* 📝 Imports all available classes in [[#shapes-anchor|shapes.py]] 
lazy from .shapes import Shapes

#* 📝 Imports all available dictionaries in [[#shapes-dictionaries-anchor|shapes_dictionaries.py]]
lazy from .shapes_dictionaries import (
    shapes_length_dict,
    # 🔗 Link to source code: [[#shapes-length-dict-anchor|shapes_length_dict()]] 
    shapes_length_sides_dict,
    # 🔗 Link to source code: [[#shapes-length-sides-dict-anchor|shapes_length_sides_dict()]] 
    shapes_radius_dict,
    # 🔗 Link to source code: [[#shapes-radius-dict-anchor|shapes_radius_dict()]] 
)

__all__ = [
    "Shapes",

    "shapes_length_dict",
    "shapes_length_sides_dict",
    "shapes_radius_dict"
]