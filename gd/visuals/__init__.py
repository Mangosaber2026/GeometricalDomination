# ⚓ Anchor for this module: [[visuals-anchor|visuals.__init__.py]] 

#* 📝 Imports the class, function and dictionary available in [[#eng-alphabets-anchor|alphabets.py]] 
from .eng_alphabets import (
    EngAlphabets,
    # 🔗 Link to source code: [[#EngAlphabets-anchor|class EngAlphabets]] 
    eng_alphabets_dict,
    # 🔗 Link to source code: [[#eng-alphabets-dict-anchor|eng_alphabets_dict()]] 
)

#* 📝 Imports the class, functions and dictionary available in [[#premade-designs-anchor|premade_designs]] 
from .premade_designs import (
    Designs,
    # 🔗 Link to source code: [[#Designs-anchor|class Designs]] 
    get_Patterns_dict,
    # 🔗 Link to source code: [[#get-Patterns-dict-anchor|get_Patterns_dict()]] 
    turtles,
    # 🔗 Link to source code: [[#turtles-anchor|decorator turtles(amount)]] 
)

#* 📝 Imports the class available in [[#shapes-anchor|shapes.py]] 
from .premade_shapes.shapes import (
    Shapes,
    # 🔗 Link to source code: [[#Shapes-anchor|class Shapes]] 
)

#* 📝 Imports the dictionaries available in [[#shapes-dictionaries-anchor|shapes_dictionaries.py]] 
from .premade_shapes.shapes_dictionaries import (
    shapes_length_dict,
    # 🔗 Link to source code: [[#shapes-length-dict-anchor|shapes_length_dict()]] 
    shapes_length_sides_dict,
    # 🔗 Link to source code: [[#shapes-length-sides-dict-anchor|shapes_length_sides_dict()]] 
    shapes_radius_dict,
    # 🔗 Link to source code: [[#shapes-radius-dict-anchor|shapes_radius_dict()]] 
)

#* 📝 Specifies all functions, dictionaries and classes available through wildcard import
__all__ = [
    "EngAlphabets",
    "eng_alphabets_dict",

    "Designs",
    "get_Patterns_dict",
    "turtles",

    "Shapes",

    "shapes_length_dict",
    "shapes_length_sides_dict",
    "shapes_radius_dict"
]