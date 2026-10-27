# ⚓ Anchor for this module: [[visuals-anchor|visuals.__init__.py]] 

#* 📝 Imports the class, functions and dictionary available in [[designs.py]]
from .designs import (  # noqa: I001
    PATTERNS,
    # 🔗 Link to source code: [[#]]
    Designs,
    # 🔗 Link to source code: [[#]]
    get_Patterns_dict,
    # 🔗 Link to source code: [[#]]
    turtles,
    # 🔗 Link to source code: [[#]]
)

#* 📝 Imports the class, function and dictionary available in [[#eng-alphabets-anchor|alphabets.py]] 
from .eng_alphabets import (
    ALPHABETS,
    # 🔗 Link to source code: [[#ALPHABETS-anchor|dictionary ALPHABETS]] 
    Alphabets,
    # 🔗 Link to source code: [[#Alphabets-anchor|class Alphabets]] 
    letters_functions,
    # 🔗 Link to source code: [[#letters-functions-anchor|letters_functions()]] 
)

#* 📝 Imports the class available in [[shapes.py]]
from .shapes import (
    Shapes,
    # 🔗 Link to source code: [[#]]
)

#* 📝 Imports the dictionaries available in [[shapes_dictionaries.py]]
from .shapes_dictionaries import (
    SHAPES_LENGTH,
    # 🔗 Link to source code: [[#]]
    SHAPES_LENGTH_SIDES,
    # 🔗 Link to source code: [[#]]
    SHAPES_RADIUS,
    # 🔗 Link to source code: [[#]]
)


 #* 📝 Specifies all functions, dictionaries and classes available through wildcard import
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