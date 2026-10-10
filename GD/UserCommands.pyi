import UF as uf
from collections.abc import Callable
from .TurtleSkeleton import ChainTurtle
from numbers import Real


type command_dict = dict[str, Callable[[], ChainTurtle | list[ChainTurtle] | int | Real | None]]

@uf.cls_deco_superposition(staticmethod)
class Command:
    """
    This class contains a collection of functions for the user_drawing_ft().

    The functions that use turtles in this class are from the UV dictionary!
    """
    def fd_ft() -> ChainTurtle:
        """
        This function makes the turtle go forward.
        :return: the last ChainTurtle in the UV dictionary.
        """
        ...
    def bk_ft() -> ChainTurtle:
        """
        This function makes the turtle go backward.
        :return: the last ChainTurtle in the UV dictionary.
        """
        ...
    def rt_ft() -> ChainTurtle:
        """
        This function makes the turtle turn right.
        :return: the last ChainTurtle in the UV dictionary.
        """
        ...
    def lt_ft() -> ChainTurtle:
        """
        This function makes the turtle turn left.
        :return: the last ChainTurtle in the UV dictionary.
        """
        ...
    def create_tls() -> list[ChainTurtle]:
        """
        This function lets the user create a chosen number of colored turtles.
        :return: a list of new created ChainTurtles.
        """
        ...
    def change_tls() -> int:
        """
        This function lets the user switch to a different turtle from the UV dictionary.
        :return: the index of the new turtle in the UV dictionary.
        """
        ...
    def clear_ft() -> None:
        """
        This function clears all turtle drawings of the turtles in the UV dictionary.
        :return: None
        """
        ...
    def clear_tls() -> list[ChainTurtle]:
        """
        This function clears all turtles and their drawings in the UV dictionary.
        :return: a list of new created ChainTurtles.
        """
        ...
    def home_ft() -> ChainTurtle:
        """
        This function sets the last turtle's (in the UV dictionary) to the home position and heading.
        :return: the last ChainTurtle in the UV dictionary.
        """
        ...
    def setpos_ft() -> ChainTurtle:
        """
        This function sets the last turtle's (in the UV dictionary) position to (x|y) without trace.
        :return: the last ChainTurtle in the UV dictionary.
        """
        ...
    def move_to_ft() -> ChainTurtle:
        """
        This function sets the turtle's position to (x|y) with trace.
        :return: the last ChainTurtle in the UV dictionary.
        """
        ...
    def set_timer() -> Real:
        """
        This functions sets a time delay for user_drawing_ft().
        :return: chosen time delay.
        """
        ...
    def del_timer() -> None:
        """
        This function deletes/deactivates the time delay for user_drawing_ft().
        :return: None
        """
        ...
    def writer() -> None:
        """
        This function draws the letters and some common punctuation of the English Alphabet.
        :return: None
        """
        ...
    def change_shape() -> ChainTurtle:
        """
        This function lets the user change the shape of the turtle to either default ones, or custom ones.
        :return: ChainTurtle()
        """
        ...

def exec_ft() -> None:
    """
    Special side function ONLY for debugging purposes
    :return: None
    """
    ...

def get_Command_dict() -> command_dict:
    """
    This function creates a dictionary with all the functions inside the class Command and returns it.
    :return: dictionary of function names mapped with the actual function.
    """
    ...


COMMANDS: command_dict