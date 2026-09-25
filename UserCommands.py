from .GlobalVariables import t_now, UV
from .GlobalFunctions import SU, tls_color
from .Alphabets import ALPHABETS
from time import sleep as rest
from collections.abc import Callable
from typing import TypeAlias
from .UniversalFunctions.GetVariable import get_num
from .UniversalFunctions.TypingVariables import Real
from .UniversalFunctions.HelperFunctions import helper
from .UniversalFunctions.DecoratorArchive import cls_deco_superposition
from .UniversalFunctions.ClassToDict import classes_to_dict
from .TurtleFunctions import TurtleFct

command_dict: TypeAlias = dict[str, Callable[[], None]]

@cls_deco_superposition(staticmethod)
class Command:
    def fd_ft() -> None:
        """Forward function for turtle"""
        distance: Real = get_num(float, "Enter the distance: "); t_now().fd(distance)

    def bk_ft() -> None:
        """Backward function for turtle"""
        distance: Real = get_num(float, "Enter the distance: "); t_now().bk(distance)

    def rt_ft() -> None:
        """Right turn function for turtle"""
        angle: Real = get_num(float, "Enter an angle: "); t_now().rt(angle)

    def lt_ft() -> None:
        """Left turn function for turtle"""
        angle: Real = get_num(float, "Enter an angle: "); t_now().lt(angle)

    def create_tls() -> None:
        """Create a chosen number of turtles"""
        turtles, turtles_num = tls_color(entry="Enter desired number of turtles: ")
        UV["tls"].extend(turtles)
        UV["t"]: int = len(UV["tls"]) - 1

    def change_tls() -> None:
        """Change from one turtle to another"""
        if len(UV["tls"]) == 1:
            raise ValueError("There is only one turtle!")
        tls_change: int = get_num(int, "Enter turtle number: ", MIN=1, MAX=len(UV["tls"]))
        UV["t"] = tls_change-1

    def clear_ft() -> None:
        """Clear all turtle drawings"""
        for t in UV["tls"]: t.clear()

    def clear_tls() -> None:
        """Clear all turtle drawings + delete turtles"""
        for t in UV["tls"]: t.clear(); t.ht()
        UV["tls"].clear()
        turtles, turtle_num = tls_color(entry="Enter number of new turtles: ")
        UV["tls"].extend(turtles)
        UV["t"]: int = turtle_num - 1

    def home_ft() -> None:
        """Sets turtle's position+heading to home with trace"""
        t_now().home()

    def setpos_ft() -> None:
        """Sets turtle's position to (x|y) without trace"""
        t_now().teleport(helper.x_ft(),helper.y_ft())

    def move_to_ft() -> None:
        """Sets turtle's position to (x|y) with trace"""
        t_now().goto(helper.x_ft(),helper.y_ft())

    def set_timer() -> None:
        """Sets a timer for user_drawing_ft()"""
        UV["delay"]: Real = get_num(float, "Enter delay: ", MIN=0)

    def del_timer() -> None:
        """Deactivates timer for user_drawing_ft()"""
        UV["delay"]: None = None

    def writer() -> None:
        """Draws out the letters of the English alphabet"""
        t_now().lt(90); x_val: Real = t_now().xcor()
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
                vertical_val: Real = get_num(float,"Enter letter height (min=5): ",MIN=5)
                for letter in text_entry:
                    ALPHABETS[letter](vertical_val,t_now())
                SU()

    def change_shape() -> None:
        """Lets the user choose different turtles shapes, including a custom option"""
        TurtleFct.change_shape(tls_num = t_now())

    def _list_commands() -> command_dict:
        """
        Creates a dictionary with all User Commands and returns it
        :return: dictionary
        """
        return classes_to_dict(Command)

def exec_ft() -> None:
    """Special side function ONLY for debugging purposes"""
    print("Enter exit to exit, otherwise enjoy!"); rest(2)
    while True:
        try:
            executer = input("Enter: ")
            if executer.lower() == "exit":
                break
            exec(executer); SU()
        except Exception as exception_error:
            print(f"Invalid input! Error: {exception_error}")
            rest(2)

def get_Command_dict() -> command_dict:
    """
    Takes all functions from Command and returns a dictionary containing them
    :return: dictionary
    """
    return {
        name.removesuffix("_ft").replace("_", " "): obj
        for name, obj in classes_to_dict(Command).items()
        if not name.startswith("_")
    }

# COMMAND STORAGE: USER PROGRAM
COMMANDS: command_dict = get_Command_dict()