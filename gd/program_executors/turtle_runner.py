# ⚓ Anchor for this module: [[turtle-runner-anchor|turtle_runner.py]] 

lazy from time import sleep as rest

lazy import turtle_extension as tx
lazy import uf

lazy from .. import user_features as user_feats
lazy from .. import visuals


#? //////////////////////////////////////
#? //////// USER DRAWING PROGRAM ///////
#? ////////////////////////////////////
# ⚓ user_drawing_ft anchor: [[user-drawing-ft-anchor|user_drawing_ft()]] 
#* 📝 This runs the customizable user focused function where
#* 📝 the user can draw their own designs with internally defined features
def user_drawing_ft():
    tx.UV["t"] = tx.tls_color(index=1)

    COMMANDS = user_feats.get_Command_dict()
    SHAPES_LENGTH = visuals.shapes_length_dict()
    SHAPES_LENGTH_SIDES = visuals.shapes_length_sides_dict()
    SHAPES_RADIUS = visuals.shapes_radius_dict()

    while True:
        user_choice: str = uf.get_str('''
        BELOW ARE SETTINGS:
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
            Enter choice: ''',
            COMMANDS, 
            SHAPES_LENGTH, 
            SHAPES_LENGTH_SIDES, 
            SHAPES_RADIUS,
            ("n","exec")
            )
        
        tx.get_screen()

        if user_choice in COMMANDS:
            COMMANDS[user_choice]()

        elif user_choice in SHAPES_LENGTH:
            SHAPES_LENGTH[user_choice](
                uf.helper.length_float(),
                tx.t_now()
                )

        elif user_choice in SHAPES_LENGTH_SIDES:
            SHAPES_LENGTH_SIDES[user_choice](
                uf.helper.length_float(),
                uf.helper.sides_num(), 
                tx.t_now()
                )

        elif user_choice in SHAPES_RADIUS:
            SHAPES_RADIUS[user_choice](
                uf.helper.radius_float(), 
                tx.t_now()
                )

        elif user_choice == "exec":
            user_feats.exec_ft()

        elif user_choice == "n":
            print("Thank you for using Sabiq's own pattern drawing program!")
            rest(2)

            tx.reset_tls(tx.UV["tls"])
            tx.UV["t"] = None
            break

        tx.SU()

        delay_time = tx.UV["delay"]
        if delay_time is not None:
            uf.real_validate()(delay_time, name="delay")
            rest(delay_time)

#? /////////////////////////////////
#? //////// MAIN OPERATION ////////
#? ///////////////////////////////
# ⚓ main anchor: [[main-anchor|main()]] 
#* 📝 This is the entrance point to the whole software,
#* 📝 it lets users draw premade functions as well as [[#user-drawing-ft-anchor|customizable ones]] 
def main():
    print("""
Welcome to Sabiq's Turtle DSL!!!

This is the main executor of the entire software and presents a collection of premade designs and patterns
of which the sizes, turtle color and even number of objects are customizable.

The 'own' option takes the user to the user-focused program where the user gets to make their own designs 
using the very building blocks the developer used to create the premade designs.

The 'n' option terminates the program.

Hope you enjoy!
""")
    rest(1.5)
    
    tls_list: list[tx.ChainTurtle] | None = None
    PATTERNS = visuals.get_Patterns_dict()
    
    while True:
        program_choice: str = uf.get_str('''Here are the options
        
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
            print("\nThank you very much for using Sabiq's Turtle DSL!!!")
            break

        if tls_list is not None:
            tx.reset_tls(tls_list)
            tx.SU()

        if program_choice == "own":
            user_drawing_ft()

        else:
            tls_list = PATTERNS[program_choice]()                           # type: ignore

        rest(3)