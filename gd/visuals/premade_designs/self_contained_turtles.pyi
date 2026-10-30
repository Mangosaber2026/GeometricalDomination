"""
This module contains the class `TurtleSelfMade` which contains premade drawing functions
which creates a list of turtles internally
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import turtle_extension as tx

#* 📝 The type used for a list of ChainTurtle
type TlsType = list[tx.ChainTurtle]


class TurtleSelfMade:

    # ========= Creates turtles internally =========

    @staticmethod
    def duo_triforce() -> TlsType:
        """
        Draws a duo triforce (Zelda reference), triangles have corresponding colors.
        
        :return: list of 6 chainable turtles
        """