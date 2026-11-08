# ⚓ Anchor for this module: [[premade-designs-anchor|premade_designs.__init__.py]] 

#* 📝 Imports classes and dictionaries from [[#designs-anchor|designs.py]] 
lazy from .designs import (
    Designs,
    # 🔗 Link to source code: [[#Designs-anchor|class Designs]] 
    get_Patterns_dict,
    # 🔗 Link to source code: [[#get-Patterns-dict-anchor|get_Patterns_dict()]] 
)
lazy from .designs_decorator import turtles

#* 📝 Specifies all available dictionaries, classes and decorators through wildcard import
__all__ = [
    "Designs",
    "get_Patterns_dict",
    "turtles",
]