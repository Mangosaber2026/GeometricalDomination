# ⚓ Anchor for this module: [[premade-designs-anchor|premade_designs.__init__.py]] 

#* 📝 Imports classes and dictionaries from [[#designs-anchor|designs.py]] 
from .designs import (
    PATTERNS,
    # 🔗 Link to source code: [[#PATTERNS-anchor|dictionary PATTERNS]] 
    Designs,
    # 🔗 Link to source code: [[#Designs-anchor|class Designs]] 
    get_Patterns_dict,
    # 🔗 Link to source code: [[#get-Patterns-dict-anchor|get_Patterns_dict()]] 
)
from .designs_decorator import turtles

#* 📝 Specifies all available dictionaries, classes and decorators through wildcard import
__all__ = [
    "PATTERNS",
    "Designs",
    "get_Patterns_dict",
    "turtles",
]