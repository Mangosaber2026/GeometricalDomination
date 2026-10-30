# ⚓ Anchor for this module: [[user-commands-anchor|user_commands.py]] 

from time import sleep as rest

import turtle_extension as tx
import uf

from .. import visuals


# ⚓ Command anchor: [[Command-anchor|class Command]] 
#* 📝 Class used for the [[#user-drawing-ft-anchor|user_drawing_ft()]] 
#* 📝 Contains functions which are used to let the user make their own drawings
class Command:

    # ⚓ fd_ft anchor: [[Command-fd-ft-anchor|fd_ft()]] 
    #* 📝 Moves the turtle forward with [[#ChainTurtle-forward-anchor|ChainTurtle().forward()]] 
    @staticmethod
    def fd_ft():   

        return tx.t_now().forward(
            uf.get_num(
                TYPE=float, 
                entry="Enter the distance: "
                )   # pyright: ignore[reportArgumentType]
            )


    # ⚓ bk_ft anchor: [[Command-bk-ft-anchor|bk_ft()]] 
     #* 📝 Moves the turtle backward with [[#ChainTurtle-backward-anchor|ChainTurtle().backward()]] 
    @staticmethod
    def bk_ft():   

        return tx.t_now().backward(
            uf.get_num(
                TYPE=float, 
                entry="Enter the distance: "
                )   # pyright: ignore[reportArgumentType]
            )


    # ⚓ rt_ft anchor: [[Command-rt-ft-anchor|rt_ft()]] 
     #* 📝 Turns the turtle to the right with [[#ChainTurtle-right-anchor|ChainTurtle().right()]] 
    @staticmethod
    def rt_ft():    

        return tx.t_now().right(
            uf.get_num(
                TYPE=float, 
                entry="Enter an angle: "
                )   # pyright: ignore[reportArgumentType]
            )

    # ⚓ lt_ft anchor: [[Command-lt-ft-anchor|lt_ft()]] 
     #* 📝 Turns the turtle to the left with [[#ChainTurtle-left-anchor|ChainTurtle().left()]] 
    @staticmethod
    def lt_ft():  

        return tx.t_now().left(
            uf.get_num(
                TYPE=float, 
                entry="Enter an angle: "
                )   # pyright: ignore[reportArgumentType]
            )

    # ⚓ create_tls anchor: [[Command-create-tls-anchor|create_tls()]] 
     #* 📝 Creates turtles and add them to the [[#UV-anchor|UV dictionary]] 
    @staticmethod
    def create_tls():   

        turtles, _ = tx.tls_color(entry="Enter desired number of turtles: ")    # pyright: ignore[reportGeneralTypeIssues]
        UV_tls: list[tx.ChainTurtle] = tx.UV["tls"]
        UV_tls.extend(turtles)                                                  # pyright: ignore[reportArgumentType]
        tx.UV["t"] = len(UV_tls) - 1

        return turtles
    

    # ⚓ change_tls anchor: [[Command-change-tls-anchor|change_tls()]] 
     #* 📝 Lets the user change turtles to [[#UV-anchor|UV dictionary]] 
    @staticmethod
    def change_tls():    

        UV_tls: list[tx.ChainTurtle] = tx.UV["tls"]
        
        if len(UV_tls) == 1:
            raise uf.value_error()(f"""
                Function: change_tls
                
                There is only one turtle in tx.UV["tls"]!
                Expected: multiple turtles
                Received: {UV_tls}
                """)
        
        tls_change: int = uf.get_num(
            TYPE=int,
            entry="Enter turtle number: ", 
            MIN=1,
            MAX=len(UV_tls)
            )
        
        tls_num = tls_change - 1
        tx.UV["t"] = tls_num

        return tls_num


    # ⚓ clear_ft anchor: [[Command-clear-ft-anchor|clear_ft()]] 
     #* 📝 Clears all turtles drawings in the [[#UV-anchor|UV dictionary]] 
    @staticmethod
    def clear_ft(): 

        UV_tls: list[tx.ChainTurtle] = tx.UV["tls"] 
        for t in UV_tls:
            t.clear()


    # ⚓ clear_tls anchor: [[Command-clear-tls-anchor|clear_tls()]] 
     #* 📝 Clears all turtles drawings and turtles in the [[#UV-anchor|UV dictionary]] 
    @staticmethod
    def clear_tls():   
        
        UV_tls: list[tx.ChainTurtle] = tx.UV["tls"]

        for t in UV_tls:
            t.clear()
            t.hideturtle()


        UV_tls.clear()
        turtles, turtle_num = tx.tls_color(entry="Enter number of new turtles: ")   # pyright: ignore[reportGeneralTypeIssues]
        UV_tls.extend(turtles)                                                      # pyright: ignore[reportArgumentType]
        tx.UV["t"] = turtle_num - 1                                                 # pyright: ignore[reportOperatorIssue]

        return turtles


    # ⚓ home_ft anchor: [[Command-home-ft-anchor|home_ft()]] 
     #* 📝 Sets the turtles position to home with [[#ChainTurtle-home-anchor|ChainTurtle().home()]] 
    @staticmethod
    def home_ft():
        return tx.t_now().home()


    # ⚓ setpos_ft anchor: [[Command-setpos-ft-anchor|setpos_ft()]] 
     #* 📝 Lets the user choose a coordinate to set the turtles position to 
     #* 📝 without a trace with [[#ChainTurtle-teleport-anchor|ChainTurtle().teleport()]] 
    @staticmethod
    def setpos_ft():   

        return tx.t_now().teleport(
            uf.helper.x_ft(),
            uf.helper.y_ft()
            )


    # ⚓ move_to_ft anchor: [[Command-move-to-ft-anchor|move_to_ft()]] 
     #* 📝 setpos_ft functionality with trace with [[#ChainTurtle-goto-anchor|ChainTurtle().goto()]] 
    @staticmethod
    def move_to_ft():   

        return tx.t_now().goto(
            uf.helper.x_ft(),
            uf.helper.y_ft()
            )


    # ⚓ set_timer anchor: [[Command-set-timer-anchor|set_timer()]] 
     #* 📝 Sets a time delay for [[#user-drawing-ft-anchor|user_drawing_ft()]] 
    @staticmethod
    def set_timer():    

        time_delay = uf.get_num(
            TYPE=float,
            entry="Enter delay: ",
            MIN=0
            )
        tx.UV["delay"] = time_delay

        return time_delay


    # ⚓ del_timer anchor: [[Command-del-timer-anchor|del_timer()]] 
     #* 📝 Deletes time delay for the [[#user-drawing-ft-anchor|user_drawing_ft()]] 
    @staticmethod
    def del_timer():    
        tx.UV["delay"] = None


    # ⚓ writer anchor: [[Command-writer-anchor|writer()]] 
     #* 📝 Lets the user write text with [[#EngAlphabets-anchor|EngAlphabets]] 
    @staticmethod
    def writer():   

        tx.t_now().left(90)   # pyright: ignore[reportArgumentType]
        while True:
            while True:
                text_entry: str = input("""
                < for heart, # for star
                Enter text (% to exit): 
                """).upper()

                if all(letter in visuals.ENG_ALPHABETS for letter in text_entry) or text_entry == "%":
                    break

                else:
                    print("Enter something VALID!")
                    rest(1.5)

            if text_entry == "%":
                break

            else:
                vertical_val: float = uf.get_num(
                    TYPE=float,
                    entry="Enter letter height (min=5): ",
                    MIN=5
                    )                                                           # pyright: ignore[reportAssignmentType]
                
                for letter in text_entry:
                    visuals.ENG_ALPHABETS[letter](vertical_val, tx.t_now())     # pyright: ignore[reportArgumentType]

                tx.SU()


    # ⚓ change_shape anchor: [[Command-change-shape-anchor|change_shape()]] 
    #* 📝 Changes the shape of future turtles with [[#TurtleFct-change-shape-anchor|Turtle.change_shape()]] 
    @staticmethod
    def change_shape():
        return tx.TurtleFct.change_shape(tls_num = tx.t_now())


    # ⚓ list_commands anchor: [[Command-list-commands-anchor|list_commands()]] 
    #* 📝 Creates and returns a dictionary mapping the function names
    #* 📝 with the corresponding function of the [[#Command-anchor|Command class]] 
    @staticmethod
    def list_commands():
        return uf.classes_to_dict(Command)


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
        for name, obj in Command.list_commands().items()
    }


# ⚓ COMMANDS anchor: [[COMMANDS-anchor|dictionary COMMANDS]] 
 #* 📝 COMMAND dictionary storage generated from [[#get-Command-dict-anchor|get_Command_dict()]] 
COMMANDS = get_Command_dict()