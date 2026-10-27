# ⚓ Anchor for this module: [[user-commands-anchor|user_commands.py]] 

from time import sleep as rest

import turtle_extension as tx
import uf

from .. import visuals


# ⚓ Command anchor: [[Command-anchor|class Command]] 
#* 📝 Class used for the [[#user-drawing-ft-anchor|user_drawing_ft()]] 
#* 📝 Contains functions which are used to let the user make their own drawings
@uf.cls_deco_superposition(staticmethod)
class Command:

    # ⚓ fd_ft anchor: [[Command-fd-ft-anchor|fd_ft()]] 
     #* 📝 Moves the turtle forward with [[#ChainTurtle-forward-anchor|ChainTurtle().forward()]] 
    def fd_ft():    # pyright: ignore[reportSelfClsParameterName]

        return tx.t_now().forward(
            uf.get_num(
                TYPE=float, 
                entry="Enter the distance: "
                )   # pyright: ignore[reportArgumentType]
            )


    # ⚓ bk_ft anchor: [[Command-bk-ft-anchor|bk_ft()]] 
     #* 📝 Moves the turtle backward with [[#ChainTurtle-backward-anchor|ChainTurtle().backward()]] 
    def bk_ft():    # pyright: ignore[reportSelfClsParameterName]

        return tx.t_now().backward(
            uf.get_num(
                TYPE=float, 
                entry="Enter the distance: "
                )   # pyright: ignore[reportArgumentType]
            )


    # ⚓ rt_ft anchor: [[Command-rt-ft-anchor|rt_ft()]] 
     #* 📝 Turns the turtle to the right with [[#ChainTurtle-right-anchor|ChainTurtle().right()]] 
    def rt_ft():    # pyright: ignore[reportSelfClsParameterName]

        return tx.t_now().right(
            uf.get_num(
                TYPE=float, 
                entry="Enter an angle: "
                )   # pyright: ignore[reportArgumentType]
            )

    # ⚓ lt_ft anchor: [[Command-lt-ft-anchor|lt_ft()]] 
     #* 📝 Turns the turtle to the left with [[#ChainTurtle-left-anchor|ChainTurtle().left()]] 
    def lt_ft():   # pyright: ignore[reportSelfClsParameterName]

        return tx.t_now().left(
            uf.get_num(
                TYPE=float, 
                entry="Enter an angle: "
                )   # pyright: ignore[reportArgumentType]
            )

    # ⚓ create_tls anchor: [[Command-create-tls-anchor|create_tls()]] 
     #* 📝 Creates turtles and add them to the [[#UV-anchor|UV dictionary]] 
    def create_tls():    # pyright: ignore[reportSelfClsParameterName]

        turtles, _ = tx.tls_color(entry="Enter desired number of turtles: ")    # pyright: ignore[reportGeneralTypeIssues]
        tx.UV["tls"].extend(turtles)
        tx.UV["t"] = len(tx.UV["tls"]) - 1

        return turtles
    

    # ⚓ change_tls anchor: [[Command-change-tls-anchor|change_tls()]] 
     #* 📝 Lets the user change turtles to [[#UV-anchor|UV dictionary]] 
    def change_tls():    # pyright: ignore[reportSelfClsParameterName]

        if len(tx.UV["tls"]) == 1:
            raise uf.value_error()(f"""
                Function: change_tls
                
                There is only one turtle in tx.UV["tls"]!
                Expected: multiple turtles
                Received: {tx.UV["tls"]}
                """)
        tls_change: int = uf.get_num(
            TYPE=int,
            entry="Enter turtle number: ", 
            MIN=1,
            MAX=len(tx.UV["tls"])
            )
        tls_num = tls_change - 1
        tx.UV["t"] = tls_num

        return tls_num


    # ⚓ clear_ft anchor: [[Command-clear-ft-anchor|clear_ft()]] 
     #* 📝 Clears all turtles drawings in the [[#UV-anchor|UV dictionary]] 
    def clear_ft():    # pyright: ignore[reportSelfClsParameterName]
        for t in tx.UV["tls"]:
            t.clear()


    # ⚓ clear_tls anchor: [[Command-clear-tls-anchor|clear_tls()]] 
     #* 📝 Clears all turtles drawings and turtles in the [[#UV-anchor|UV dictionary]] 
    def clear_tls():    # pyright: ignore[reportSelfClsParameterName]
        for t in tx.UV["tls"]:
            t.clear()
            t.ht()


        tx.UV["tls"].clear()
        turtles, turtle_num = tx.tls_color(entry="Enter number of new turtles: ")   # pyright: ignore[reportGeneralTypeIssues]
        tx.UV["tls"].extend(turtles)
        tx.UV["t"] = turtle_num - 1     # pyright: ignore[reportOperatorIssue]

        return turtles


    # ⚓ home_ft anchor: [[Command-home-ft-anchor|home_ft()]] 
     #* 📝 Sets the turtles position to home with [[#ChainTurtle-home-anchor|ChainTurtle().home()]] 
    def home_ft():    # pyright: ignore[reportSelfClsParameterName]
        return tx.t_now().home()


    # ⚓ setpos_ft anchor: [[Command-setpos-ft-anchor|setpos_ft()]] 
     #* 📝 Lets the user choose a coordinate to set the turtles position to 
     #* 📝 without a trace with [[#ChainTurtle-teleport-anchor|ChainTurtle().teleport()]] 
    def setpos_ft():    # pyright: ignore[reportSelfClsParameterName]

        return tx.t_now().teleport(
            uf.helper.x_ft(),
            uf.helper.y_ft()
            )


    # ⚓ move_to_ft anchor: [[Command-move-to-ft-anchor|move_to_ft()]] 
     #* 📝 setpos_ft functionality with trace with [[#ChainTurtle-goto-anchor|ChainTurtle().goto()]] 
    def move_to_ft():    # pyright: ignore[reportSelfClsParameterName]

        return tx.t_now().goto(
            uf.helper.x_ft(),
            uf.helper.y_ft()
            )


    # ⚓ set_timer anchor: [[Command-set-timer-anchor|set_timer()]] 
     #* 📝 Sets a time delay for [[#user-drawing-ft-anchor|user_drawing_ft()]] 
    def set_timer():    # pyright: ignore[reportSelfClsParameterName]

        time_delay: float = uf.get_num(
            TYPE=float,
            entry="Enter delay: ",
            MIN=0
            )
        tx.UV["delay"] = time_delay

        return time_delay


    # ⚓ del_timer anchor: [[Command-del-timer-anchor|del_timer()]] 
     #* 📝 Deletes time delay for the [[#user-drawing-ft-anchor|user_drawing_ft()]] 
    def del_timer():    # pyright: ignore[reportSelfClsParameterName]
        tx.UV["delay"] = None


    # ⚓ writer anchor: [[Command-writer-anchor|writer()]] 
     #* 📝 Lets the user write text with [[#Alphabets-anchor|Alphabets]]
    def writer():    # pyright: ignore[reportSelfClsParameterName]

        tx.t_now().lt(90)   # pyright: ignore[reportArgumentType]
        while True:
            while True:
                text_entry: str = input("""
                < for heart, # for star
                Enter text (% to exit): 
                """).upper()

                if all(letter in visuals.ALPHABETS for letter in text_entry) or text_entry == "%":
                    break

                else:
                    print("Enter something VALID!")
                    rest(1.5)

            if text_entry == "%":
                break

            else:
                vertical_val: float = uf.get_num(
                    float,
                    "Enter letter height (min=5): ",
                    MIN=5
                    )   # pyright: ignore[reportAssignmentType]
                
                for letter in text_entry:
                    visuals.ALPHABETS[letter](vertical_val, tx.t_now())     # pyright: ignore[reportArgumentType]

                tx.SU()


    # ⚓ change_shape anchor: [[Command-change-shape-anchor|change_shape()]] 
    #* 📝 Changes the shape of future turtles with [[#TurtleFct-change-shape-anchor|Turtle.change_shape()]] 
    def change_shape():    # pyright: ignore[reportSelfClsParameterName]
        return tx.TurtleFct.change_shape(tls_num = tx.t_now())


# ⚓ exec_ft anchor: [[exec-ft-anchor|exec_ft()]] 
#* 📝 Provides exec feature as a function
def exec_ft():

    print("Enter exit to exit, otherwise enjoy!")
    rest(2)

    while True:
        try:
            executer = input("Enter: ")
            if executer.lower() == "exit":
                break
            exec(executer)
            tx.SU()

        except Exception as exception_error:
            print(f"Invalid input! Error: {exception_error}")
            rest(2)


# ⚓ get_Command_dict anchor: [[get-Command-dict-anchor|get_Command_dict()]] 
 #* 📝 Creates and returns a dictionary with [[#Command-anchor|Command class]] functions
def get_Command_dict():
    return {
        name.removesuffix("_ft").replace("_", " "): obj
        for name, obj in uf.classes_to_dict(Command).items()
    }


# ⚓ COMMANDS anchor: [[COMMANDS-anchor|dictionary COMMANDS]] 
 #* 📝 COMMAND dictionary storage generated from [[#get-Command-dict-anchor|get_Command_dict()]] 
COMMANDS = get_Command_dict()