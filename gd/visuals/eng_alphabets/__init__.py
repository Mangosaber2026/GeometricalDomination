# ⚓ Anchor for this module: [[eng-alphabets-anchor|eng_alphabets.__init__.py]] 


#* 📝 Imports dictionaries, classes and functions from [[#english-alphabets-anchor|english_alphabets.py]] 
from .english_alphabets import (  # noqa: I001
    ALPHABETS,
    # 🔗 Link to source code: [[#ALPHABETS-anchor|dictionary ALPHABETS]] 
    Alphabets,
    # 🔗 Link to source code: [[#Alphabets-anchor|class Alphabets]] 
    letters_functions,
    # 🔗 Link to source code: [[#letters-functions-anchor|letters_functions()]] 
)


#* 📝 Specifies all available dictionaries, classes and functions through wildcard import
__all__ = [
    "ALPHABETS",
    "Alphabets",
    "letters_functions"
]