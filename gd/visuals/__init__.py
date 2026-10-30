# ⚓ Anchor for this module: [[visuals-anchor|visuals.__init__.py]] 

#* 📝 Imports the class, function and dictionary available in [[#eng-alphabets-anchor|alphabets.py]] 
from .eng_alphabets import (
    ENG_ALPHABETS,
    # 🔗 Link to source code: [[#ENG_ALPHABETS-anchor|dictionary ALPHABETS]] 
    EngAlphabets,
    # 🔗 Link to source code: [[#EngAlphabets-anchor|class EngAlphabets]] 
    letters_functions,
    # 🔗 Link to source code: [[#letters-functions-anchor|letters_functions()]] 
)

#* 📝 Imports the class, functions and dictionary available in [[#premade-designs-anchor|premade_designs]] 
from .premade_designs import (
    PATTERNS,
    # 🔗 Link to source code: [[#PATTERNS-anchor|dictionary PATTERNS]] 
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
    SHAPES_LENGTH,
    # 🔗 Link to source code: [[#SHAPES-LENGTH-anchor|dictionary SHAPES_LENGTH]] 
    SHAPES_LENGTH_SIDES,
    # 🔗 Link to source code: [[#SHAPES-LENGTH-SIDES-anchor|dictionary SHAPES_LENGTH_SIDES]] 
    SHAPES_RADIUS,
    # 🔗 Link to source code: [[#SHAPES-RADIUS-anchor|dictionary SHAPES_RADIUS]] 
)

#* 📝 Specifies all functions, dictionaries and classes available through wildcard import
__all__ = [
    "EngAlphabets",
    "ENG_ALPHABETS",
    "letters_functions",

    "Designs",
    "PATTERNS",
    "get_Patterns_dict",
    "turtles",

    "Shapes",

    "SHAPES_LENGTH",
    "SHAPES_LENGTH_SIDES",
    "SHAPES_RADIUS",
]