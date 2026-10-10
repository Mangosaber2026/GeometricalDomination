"""
This module contains the class Command, which contains functions for the user_drawing_ft() function.
"""

from .GlobalVariables import t_now, UV
from .GlobalFunctions import SU, tls_color
from .Alphabets import ALPHABETS
from time import sleep as rest
from .TurtleFunctions import TurtleFct
from numbers import Real
import UF as uf


helper = uf.helper

@uf.cls_deco_superposition(staticmethod)
class Command:
    def fd_ft():
        return t_now().fd(uf.get_num(float, "Enter the distance: "))

    def bk_ft():
        return t_now().bk(uf.get_num(float, "Enter the distance: "))

    def rt_ft():
        return t_now().rt(uf.get_num(float, "Enter an angle: "))

    def lt_ft():
        return t_now().lt(uf.get_num(float, "Enter an angle: "))

    def create_tls():
        turtles, turtles_num = tls_color(entry="Enter desired number of turtles: ")
        UV["tls"].extend(turtles)
        UV["t"]: int = len(UV["tls"]) - 1
        return turtles

    def change_tls():
        if len(UV["tls"]) == 1:
            raise uf.value_error()(f"""
                Function: change_tls
                
                There is only one turtle in UV["tls"]!
                Expected: multiple turtles
                Received: {UV["tls"]}
                """)
        tls_change: int = uf.get_num(int, "Enter turtle number: ", MIN=1, MAX=len(UV["tls"]))
        tls_num = tls_change - 1
        UV["t"] = tls_num
        return tls_num

    def clear_ft():
        for t in UV["tls"]: t.clear()

    def clear_tls():
        for t in UV["tls"]:
            t.clear()
            t.ht()

        UV["tls"].clear()
        turtles, turtle_num = tls_color(entry="Enter number of new turtles: ")
        UV["tls"].extend(turtles)
        UV["t"]: int = turtle_num - 1
        return turtles

    def home_ft():
        return t_now().home()

    def setpos_ft():
        return t_now().teleport(helper.x_ft(),helper.y_ft())

    def move_to_ft():
        return t_now().setpos(helper.x_ft(),helper.y_ft())

    def set_timer():
        time_delay: Real = uf.get_num(float, "Enter delay: ", MIN=0)
        UV["delay"] = time_delay
        return time_delay

    def del_timer():
        UV["delay"]: None = None

    def writer():
        t_now().lt(90)
        while True:
            while True:
                text_entry: str = input("""
                < for heart, # for star
                Enter text (% to exit): 
                """).upper()
                if all(letter in ALPHABETS for letter in text_entry) or text_entry == "%":
                    break
                else:
                    print("Enter something VALID!"); rest(1.5)
            if text_entry == "%":
                break
            else:
                vertical_val: Real = uf.get_num(float,"Enter letter height (min=5): ",MIN=5)
                for letter in text_entry:
                    ALPHABETS[letter](vertical_val,t_now())
                SU()

    def change_shape():
        return TurtleFct.change_shape(tls_num = t_now())

def exec_ft():
    print("Enter exit to exit, otherwise enjoy!"); rest(2)
    while True:
        try:
            executer = input("Enter: ")
            if executer.lower() == "exit":
                break
            exec(executer)
            SU()

        except Exception as exception_error:
            print(f"Invalid input! Error: {exception_error}")
            rest(2)

def get_Command_dict():
    return {
        name.removesuffix("_ft").replace("_", " "): obj
        for name, obj in uf.classes_to_dict(Command).items()
        if not name.startswith("_")
    }

# COMMAND STORAGE: USER PROGRAM
COMMANDS = get_Command_dict()