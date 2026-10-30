"""
This module contains the decorators and validators required to validate the 
inputs given for the variables in the EngAlphabets functions
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.


import collections.abc as cabc
import numbers as num

import turtle_extension as tx

def alphabets_validate(height: num.Real, tls: tx.ChainTurtle) -> tuple[num.Real, tx.ChainTurtle]:
    """
    This function takes the parameters from all alphabet drawing functions and validates them.

    :param height: height of each letter/punctuation/symbol

    :param tls: an instance of ChainTurtle

    :return: validated height and tls
    """

def alphabets_deco(func: cabc.Callable) -> cabc.Callable:
    """
    DECORATOR!!!

    This decorator takes each alphabet function and uses alphabets_validate to validate the functions
    parameters.

    :param func: alphabet function

    :return: validated alphabet function
    """