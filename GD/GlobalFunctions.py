from .TurtleHeart import tl, ChainTurtle
from .GlobalVariables import t_shape, UV
from turtle import TurtleGraphicsError
from time import sleep as rest
import UF as uf
from typing import Final, Literal


_screen = None

def get_screen():
    global _screen

    if _screen is None:
        _screen = tl.Screen()
        _screen.getcanvas().winfo_toplevel().state("zoomed")
        _screen.tracer(0)

    return _screen

def SU():
    get_screen().update()

def mainloop():
    get_screen().mainloop()

type turtle_list = list[ChainTurtle]

def tls_color(**options):

    tl_num_name: Final[Literal["tl_num"]] = "tl_num"
    entry_name: Final[Literal["entry"]] = "entry"
    index_name: Final[Literal["index"]] = "index"

    if tl_num_name in options:
        tl_num = options[tl_num_name]
        uf.int_validate()(tl_num, tl_num_name)
        uf.Positive()(tl_num, tl_num_name)
        turtles_num_count = tl_num

    elif entry_name in options:
        entry = options[entry_name]
        uf.str_validate()(entry, entry_name)
        turtles_num_count = uf.get_num(int, entry, MIN=1)

    elif index_name in options:
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
                if index_name in options:
                    UV["tls"].append(turtle)
                else:
                    tls.append(turtle)
                break

            except TurtleGraphicsError:
                print("Enter a VALID color!"); rest(2)

    if index_name in options:
        return len(UV["tls"]) - 1

    elif entry_name in options:
        return tls, turtles_num_count

    elif tl_num_name in options:
        return tls
    return None


def reset_tls(tls_list):

    tls_list_name: Final[Literal["tls_list"]] = "tls_list"
    uf.TypeValidate(list)(tls_list, name=tls_list_name)
    uf.SequenceValidate(ChainTurtle, ...)(tls_list, name=tls_list_name)

    for t in tls_list:
        t.clear().ht()
    tls_list.clear()
    return tls_list