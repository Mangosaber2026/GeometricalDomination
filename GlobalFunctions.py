from .UniversalFunctions.GetVariable import get_num
from .TurtleSkeleton import tl, ChainTurtle
from .GlobalVariables import t_shape, UV
from turtle import TurtleGraphicsError
from time import sleep as rest
from .UniversalFunctions.FctInputValidators import validate

screen = tl.Screen()
screen.getcanvas().winfo_toplevel().state("zoomed")
screen.tracer(0)
def SU() -> None:
    """This function updates the turtle screen"""
    global screen
    screen.update()

def tls_color(**options) -> int | tuple[list[ChainTurtle], int] | list[ChainTurtle] | None:
    """This function creates a turtle list with their colors or adds newly creates turtles to the UV["tls"] list
    to be used for the user_drawing_ft()

    USERS NOTICE: it is HIGHLY recommended to NOT enter a turtles count of MORE than a few hundred (max. 200) unless required!!!
    :param options: tl_num -> number of turtles to create, entry -> input string, index -> number of turtles to be created for user_drawing_ft()
    & it returns the index of the last turtle
    :return: tls_num: turtle list with colored turtles, entry: list with colored turtles + number of turtles ,otherwise: index of last turtle
    """
    if "tl_num" in options:
        validate(options["tl_num"], int, "tl_num")
        if options["tl_num"] <= 0:
            raise ValueError("tl_num must be greater than 0")
        turtles_num_count = options["tl_num"]
    elif "entry" in options:
        validate(options["entry"], int, "entry")
        turtles_num_count = get_num(int, options["entry"], MIN=1)
    elif "index" in options:
        validate(options["index"], int, "index")
        if options["index"] <= 0:
            raise ValueError("index must be greater than 0")
        turtles_num_count = options["index"]
    else:
        print("NONE of the entered options exist!")
        return None
    tls: list[ChainTurtle] = []

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


def reset_tls(tls_list: list[ChainTurtle]) -> None:
    """This function deletes the drawings of given turtle list + turtles"""
    if not all(isinstance(turtle, ChainTurtle) for turtle in tls_list):
        raise TypeError("All objects in the list must be of type ChainTurtle!")

    for t in tls_list:
        t.clear(); t.ht()
    tls_list.clear()