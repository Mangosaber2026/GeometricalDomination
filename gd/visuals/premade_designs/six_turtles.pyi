"""
This module contains the class `TurtleSix` which contains premade drawing functions
which takes a list of 6 ChainTurtle instances.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import turtle_extension as tx

#* 📝 The type used for a list of ChainTurtle instances
type TurtleListType = list[tx.ChainTurtle]

class TurtleSix:

    # ======== TURTLE 6 =========

    @staticmethod
    def circles6(tls: TurtleListType) -> None:
        """
        Draws 6 circles (with 6 turtles) 'simultaneously' with each being 60° to the left of the last one.
        
        :param tls: list of 6 chainable turtles

        :return: None
        """