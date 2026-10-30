# ⚓ Anchor for this module: [[eng-alphabets-anchor|eng_alphabets.__init__.py]] 


#* 📝 Imports dictionaries, classes and functions from [[#english-alphabets-anchor|english_alphabets.py]] 
from .english_alphabets import (  # noqa: I001
    ENG_ALPHABETS,
    # 🔗 Link to source code: [[#ENG_ALPHABETS-anchor|dictionary ALPHABETS]] 
    EngAlphabets,
    # 🔗 Link to source code: [[#EngAlphabets-anchor|class EngAlphabets]] 
    letters_functions,
    # 🔗 Link to source code: [[#letters-functions-anchor|letters_functions()]] 
)


#* 📝 Specifies all available dictionaries, classes and functions through wildcard import
__all__ = [
    "ENG_ALPHABETS",
    "EngAlphabets",
    "letters_functions"
]