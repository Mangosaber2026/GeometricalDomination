"""
This module contains the class `TurtleToChoose` which contains premade drawing functions
which require the user to choose the number of turtles.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import turtle_extension as tx

#* 📝 The type used for a list of ChainTurtle
type TlsType = list[tx.ChainTurtle]

class TurtleToChoose:

    # ========= TURTLE UNDEFINED =========

    @staticmethod
    def flower_infinite() -> TlsType:
        """
        Draws a customized flower: petals + circles number.

        :return: list of a chosen number of turtles
        """