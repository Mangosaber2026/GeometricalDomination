"""
This module contains the Alphabets class which provides a collection of functions for drawing English letters,
punctuation, and shapes (heart, star).
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.


import collections.abc as cabc  # noqa: I001
import numbers as num

import turtle_extension as tx

from . import english_letters, english_punctuations, english_shapes


 #* 📝 Type variable for [[Alphabets]] functions
type AlphabetFunctionType = cabc.Callable[[num.Real, tx.ChainTurtle], None]

 #* 📝 Type variable for classes which return [[Alphabets]] functions
type AlphabetDictType = dict[str, AlphabetFunctionType]

 #* 📝 Type variable for functions which return the entire [[Alphabets]] dictionary
type FullAlphabetDictType = dict[
    str,
    AlphabetFunctionType | cabc.Callable[[], FullAlphabetDictType]
]


class Alphabets(
    english_letters.Letters,
    english_punctuations.Punctuation,
    english_shapes.EngShapes,
):
    """
    The definitive collection of English letters, punctuation marks, and shapes.
    """

    @classmethod
    def list_alphabets(cls) -> FullAlphabetDictType:
        """
        Creates a dictionary with the functions in Alphabets and returns it.

        :return: dictionary containing function names -> function
        """

def letters_functions() -> AlphabetDictType:
    """
    Takes all Letters in Alphabets.Letters and returns a dictionary.
    
    :return: letter dictionary
    """

letters_dict: AlphabetDictType

ALPHABETS: AlphabetDictType