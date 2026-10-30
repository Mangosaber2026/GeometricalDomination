"""
This module contains the class Command, which contains functions for the user_drawing_ft() function.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import collections.abc as cabc  # noqa: I001
import numbers as num

import turtle_extension as tx
import uf


#* 📝 Type for any real number
type RealType = float | int | num.Real

#* 📝 Type for turtle lists
type TurtleList = list[tx.ChainTurtle]

 #* 📝 Marks the type used to indicate which function returns a Command dictionary [[Command]]
type CommandDictType = dict[
    str,
    cabc.Callable[
        [],
        tx.ChainTurtle | TurtleList | int | RealType | None
    ]
]


@uf.cls_deco_superposition(staticmethod)
class Command:
    """
    This class contains a collection of functions for the user_drawing_ft().

    The functions that use turtles in this class are from the UV dictionary!
    """
    @staticmethod
    def fd_ft() -> tx.ChainTurtle:
        """
        This function makes the turtle go forward.

        :return: the last tx.ChainTurtle in the UV dictionary.
        """


    @staticmethod
    def bk_ft() -> tx.ChainTurtle:
        """
        This function makes the turtle go backward.

        :return: the last tx.ChainTurtle in the UV dictionary.
        """


    @staticmethod
    def rt_ft() -> tx.ChainTurtle:
        """
        This function makes the turtle turn right.

        :return: the last tx.ChainTurtle in the UV dictionary.
        """


    @staticmethod
    def lt_ft() -> tx.ChainTurtle:
        """
        This function makes the turtle turn left.

        :return: the last tx.ChainTurtle in the UV dictionary.
        """


    @staticmethod
    def create_tls() -> TurtleList:
        """
        This function lets the user create a chosen number of colored turtles.

        :return: a list of new created ChainTurtles.
        """


    @staticmethod
    def change_tls() -> int:
        """
        This function lets the user switch to a different turtle from the UV dictionary.

        :return: the index of the new turtle in the UV dictionary.
        """


    @staticmethod
    def clear_ft() -> None:
        """
        This function clears all turtle drawings of the turtles in the UV dictionary.

        :return: None
        """


    @staticmethod
    def clear_tls() -> TurtleList:
        """
        This function clears all turtles and their drawings in the UV dictionary.

        :return: a list of new created ChainTurtles.
        """


    @staticmethod
    def home_ft() -> tx.ChainTurtle:
        """
        This function sets the last turtle's (in the UV dictionary) to the home position and heading.
        
        :return: the last tx.ChainTurtle in the UV dictionary.
        """


    @staticmethod
    def setpos_ft() -> tx.ChainTurtle:
        """
        This function sets the last turtle's (in the UV dictionary) position to (x|y) without trace.
        
        :return: the last tx.ChainTurtle in the UV dictionary.
        """


    @staticmethod
    def move_to_ft() -> tx.ChainTurtle:
        """
        This function sets the turtle's position to (x|y) with trace.
        
        :return: the last tx.ChainTurtle in the UV dictionary.
        """


    @staticmethod
    def set_timer() -> RealType:
        """
        This functions sets a time delay for user_drawing_ft().
        
        :return: chosen time delay.
        """


    @staticmethod
    def del_timer() -> None:
        """
        This function deletes/deactivates the time delay for user_drawing_ft().
        
        :return: None
        """


    @staticmethod
    def writer() -> None:
        """
        This function draws the letters and some common punctuation of the English Alphabet.
        
        :return: None
        """


    @staticmethod
    def change_shape() -> tx.ChainTurtle:
        """
        This function lets the user change the shape of the turtle to either default ones, or custom ones.
        
        :return: tx.ChainTurtle()
        """


    @staticmethod
    def list_commands() -> CommandDictType:
        """
        This function creates a dictionary with all the functions inside the class Command and returns it.
            
        :return: dictionary of function names mapped with the actual function.
        """


def exec_ft() -> None:
    """
    Special side function ONLY for debugging purposes
    
    :return: None
    """


def get_Command_dict() -> CommandDictType:
    """
    This function creates a dictionary with all the functions inside the class Command and returns it.
    
    :return: dictionary of function names mapped with the actual function.
    """


COMMANDS: CommandDictType