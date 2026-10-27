# ⚓ Anchor for this module: [[turtle-runner-anchor|turtle_runner.py]] 

from time import sleep as rest

import turtle_extension as tx
import uf

from .. import user_features as user_feats
from .. import visuals


#? //////////////////////////////////////
#? //////// USER DRAWING PROGRAM ///////
#? ////////////////////////////////////
# ⚓ user_drawing_ft anchor: [[user-drawing-ft-anchor|user_drawing_ft()]] 
#* 📝 This runs the customizable user focused function where
#* 📝 the user can draw their own designs with internally defined features
def user_drawing_ft():
    tx.UV["t"]: int = tx.tls_color(index=1)     # type: ignore

    while True:
        user_choice: str = uf.get_str('''BELOW ARE SETTINGS:
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
            user_feats.COMMANDS, 
            visuals.SHAPES_LENGTH, 
            visuals.SHAPES_LENGTH_SIDES, 
            visuals.SHAPES_RADIUS,
            ("n","exec")
            )
        
        tx.get_screen()

        if user_choice in user_feats.COMMANDS:
            user_feats.COMMANDS[user_choice]()

        elif user_choice in visuals.SHAPES_LENGTH:
            visuals.SHAPES_LENGTH[user_choice](
                uf.helper.length_float(),
                tx.t_now()
                )

        elif user_choice in visuals.SHAPES_LENGTH_SIDES:
            visuals.SHAPES_LENGTH_SIDES[user_choice](
                uf.helper.length_float(),
                uf.helper.sides_num(), 
                tx.t_now()
                )

        elif user_choice in visuals.SHAPES_RADIUS:
            visuals.SHAPES_RADIUS[user_choice](
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

        if tx.UV["delay"] is not None:
            uf.real_validate()(tx.UV["delay"], name="delay")
            rest(tx.UV["delay"])

#? /////////////////////////////////
#? //////// MAIN OPERATION ////////
#? ///////////////////////////////
# ⚓ main anchor: [[main-anchor|main()]] 
#* 📝 This is the entrance point to the whole software,
#* 📝 it lets users draw premade functions as well as [[#user-drawing-ft-anchor|customizable ones]] 
def main():
    print("There are 6 turtles in total, you can decide the trace & turtle color!")
    rest(1.5)
    
    tls_list: list[tx.ChainTurtle] | None = None
    
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
        Enter your choice: ''', visuals.PATTERNS, ("own","n"))

        if program_choice == "n":
            print("\nThank you very much for using Sabiq's mini Turtle DSL!!!")
            break

        if tls_list is not None:
            tx.reset_tls(tls_list)
            tx.SU()

        if program_choice == "own":
            user_drawing_ft()

        else:
            tls_list = visuals.PATTERNS[program_choice]() # type: ignore

        rest(3)