# ⚓ Anchor for this module: [[eng-alphabets-anchor|eng_alphabets.__init__.py]] 


#* 📝 Imports dictionaries, classes and functions from [[#english-alphabets-anchor|english_alphabets.py]] 
lazy from .english_alphabets import (
    EngAlphabets,
    # 🔗 Link to source code: [[#EngAlphabets-anchor|class EngAlphabets]] 
    eng_alphabets_dict,
    # 🔗 Link to source code: [[#eng-alphabets-dict-anchor|eng_alphabets_dict()]] 
)

#* 📝 Specifies all available dictionaries, classes and functions through wildcard import
__all__ = [
    "EngAlphabets",
    "eng_alphabets_dict",
]