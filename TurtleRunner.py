# WELCOME TO MY TURTLE DSL; HOPE YOU ENJOY!
from .Designs import *
from .UserCommands import *
from .GlobalFunctions import reset_tls
from .UniversalFunctions.StringCheck import get_str
from .Shapes_Dictionary import SHAPES_LENGTH, SHAPES_RADIUS, SHAPES_LENGTH_SIDES

# //////////////////////////////////////
# //////// USER DRAWING PROGRAM ///////
# ////////////////////////////////////
def user_drawing_ft() -> None:
    """This is THE executer for the more custom user-friendly drawing program"""
    UV["t"]: int = tls_color(index=1)
    while True:
        user_choice: str = get_str('''BELOW ARE SETTINGS:
            create tls -> create multiple turtles
            change tls -> change to a different turtle
            change shape -> change turtle shape for current turtle
            clear -> clear all drawings
            clear tls -> clear all turtles+drawing
            set timer -> set timer for program delay
            del timer -> delete timer for program delay
            home -> sets current turtle(CT) to (0|0),East
            setpos -> sets position of CT
            move to -> draws to chosen coordinate
            n -> nothing
            BELOW ARE DRAWING OPTIONS:
            fd -> forward, bk -> backward, rt -> right, lt -> left
            circle -> draws circle
            circle fill -> circle + fill
            tri -> draws triangle
            tri fill -> triangle + fill
            tri half -> special: starts at side length/2
            square -> draws square
            square fill -> square + fill
            square half -> special: starts at side length/2
            hexagon -> draws hexagon
            sod -> Star Of David
            sod fill -> star of david fill
            hexa flower -> 6 petal flower (start: center)
            flower tri -> flower of triangles
            poly -> polygon of choice
            poly fill -> polygon + fill
            lotus -> 12 petal flower
            writer -> text writer
            
            if you're an experienced programmer and know the program inside out, then here's another option:
            exec -> pythons execution function
            Enter choice: ''', COMMANDS, SHAPES_LENGTH, SHAPES_LENGTH_SIDES, SHAPES_RADIUS, ("n","exec"))

        if user_choice in COMMANDS:
            COMMANDS[user_choice]()
        elif user_choice in SHAPES_LENGTH:
            SHAPES_LENGTH[user_choice](helper.length_float(), t_now())
        elif user_choice in SHAPES_LENGTH_SIDES:
            SHAPES_LENGTH_SIDES[user_choice](helper.length_float(), helper.sides_num(), t_now())
        elif user_choice in SHAPES_RADIUS:
            SHAPES_RADIUS[user_choice](helper.radius_float(),t_now())
        elif user_choice == "exec":
            exec_ft()
        elif user_choice == "n":
            print("Thank you for using Sabiq's own pattern drawing program!"); rest(2)
            reset_tls(UV["tls"]); UV["t"]=None; break
        SU()
        if UV["delay"] is not None: rest(UV["delay"])

# /////////////////////////////////
# //////// MAIN OPERATION ////////
# ///////////////////////////////
def main() -> None:
    """This is THE executer of the ENTIRE Turtle DSL"""
    print("There are 6 turtles in total, you can decide the trace & turtle color!"); rest(1.5)
    tls_list: list[ChainTurtle] | None = None
    while True:
        program_choice: str = get_str('''Here are the options
        
        circles6 -> 6 circles with 6 turtles
        duo spiral -> beautiful duo spiral
        flower 4petals -> 4 flowers
        square4 -> 4 squares
        squares8 = 8 squares
        squares10 = squares8+twist
        flower infinite -> flowers
        quadrant square -> squares in each quadrant
        multi square grid -> square grid
        hexaflower -> triangles(12) flower
        tri hexaflower -> triangles(12) flower + lines in the middle
        star of david -> Star of David (SD)
        sd pattern -> SD pattern
        sd spiral -> Stars of David spiral
        sd flower -> flower inside SD
        sd triflower -> sd flower triangle formation
        hexaflower sd -> hexa flower inside SD
        diamond pattern -> diamond pattern
        hidden sds -> hidden SDs 
        gd reference -> gd reference icon
        tri wheel -> triangular wheel
        lotus pattern -> lotus flower pattern
        change shape -> change turtle shape
        duo triforce -> duo triforce from Zelda
        
        n -> nothing
        own -> make your own design
        Enter your choice: ''', PATTERNS, ("own","n"))

        if program_choice == "n":
            print("\nThank you very much for using Sabiq's mini Turtle DSL!!!")
            break
        if tls_list is not None: reset_tls(tls_list); SU()

        if program_choice == "own":
            user_drawing_ft()
        else:
            tls_list = PATTERNS[program_choice]()
        rest(3)