"""
This module contains a very useful function: tls_color, which lets the user create any number of turtles with
colors and get a list with them.
"""

from .TurtleSkeleton import tl, ChainTurtle
from .GlobalVariables import t_shape, UV
from turtle import TurtleGraphicsError
from time import sleep as rest
import UF as uf


_screen = None

def get_screen():
    """Initiates the turtle screen when the function is called"""
    global _screen

    if _screen is None:
        _screen = tl.Screen()
        _screen.getcanvas().winfo_toplevel().state("zoomed")
        _screen.tracer(0)

    return _screen

def SU() -> None:
    """This function updates the turtle screen"""
    get_screen().update()

def mainloop() -> None:
    """This function keeps the turtle screen open"""
    get_screen().mainloop()

type turtle_list = list[ChainTurtle]

def tls_color(**options) -> int | tuple[turtle_list, int] | turtle_list | None:
    """This function creates a turtle list with their colors or adds newly creates turtles to the UV["tls"] list
    to be used for the user_drawing_ft()

    USERS NOTICE: it is HIGHLY recommended to NOT enter a turtles count of MORE than a few hundred (max. 200) unless required!!!
    :param options: tl_num -> number of turtles to create, entry -> input string, index -> number of turtles to be created for user_drawing_ft()
    & it returns the index of the last turtle
    :return: tls_num: turtle list with colored turtles, entry: list with colored turtles + number of turtles ,otherwise: index of last turtle
    """
    if "tl_num" in options:
        tl_num_name = "tl_num"
        tl_num = options[tl_num_name]
        uf.int_validate()(tl_num, tl_num_name)
        uf.Positive()(tl_num, tl_num_name)
        turtles_num_count = tl_num
    elif "entry" in options:
        entry_name = "entry"
        entry = options[entry_name]
        uf.str_validate()(entry, entry_name)
        turtles_num_count = uf.get_num(int, entry, MIN=1)
    elif "index" in options:
        index_name = "index"
        index = options[index_name]
        uf.int_validate()(index, index_name)
        uf.Positive()(index, index_name)
        turtles_num_count = index
    else:
        print("NONE of the entered options exist!")
        return None
    tls: turtle_list = []

    for color_num in range(turtles_num_count):
        while True:
            color_iteration: str = input(f"Enter turtle color {color_num + 1}: ")
            try:
                turtle: ChainTurtle = ChainTurtle().color(color_iteration).shape(t_shape())
                if "index" in options:
                    UV["tls"].append(turtle)
                else:
                    tls.append(turtle)
                break
            except TurtleGraphicsError:
                print("Enter a VALID color!"); rest(2)
    if "index" in options:
        return len(UV["tls"]) - 1
    elif "entry" in options:
        return tls, turtles_num_count
    elif "tl_num" in options:
        return tls
    return None


def reset_tls(tls_list: turtle_list) -> None:
    """This function deletes the drawings of given turtle list + turtles"""
    for turtle in tls_list:
        uf.TypeValidate(ChainTurtle)(turtle, "turtle")

    for t in tls_list:
        t.clear(); t.ht()
    tls_list.clear()