from .GlobalVariables import t_now, UV
from .GlobalFunctions import SU, tls_color
from .Alphabets import ALPHABETS
from .CustomTurtleShapes import CUSTOM_SHAPES
from time import sleep as rest
from collections.abc import Callable
from .UniversalFunctions.GetVariable import get_num
from .UniversalFunctions.StringCheck import get_str
from .UniversalFunctions.TypingVariables import Real
from .UniversalFunctions.HelperFunctions import helper
from .UniversalFunctions.DecoratorArchive import class_decorator
from .UniversalFunctions.ClassToDict import class_to_dict
from .TurtleSkeleton import tl

@class_decorator(staticmethod)
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
        for turtle in range(turtles_num):
            UV["tls"].append(turtle)
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
        UV["tls"].clear(); tls_color(entry="Enter number of new turtles: ")
        UV["t"]: int = len(UV["tls"]) - 1

    def home_ft() -> None:
        """Sets turtle's position+heading to home with trace"""
        t_now().home()

    def setpos_ft() -> None:
        """Sets turtle's position to (x|y) without trace"""
        t_now().teleport(helper.x_ft(),helper.y_ft())

    def moveto_ft() -> None:
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
                text_entry: str = input("Enter text (% to exit): ").lower()
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

    def user_tls_shape() -> None:
        """Lets the user choose different turtles shapes, including a custom option"""
        turtle_shapes_list: list[str] = tl.getshapes()
        user_shape: str = get_str(f'''
            Here are the options for the turtle shape:
            {turtle_shapes_list}
            Enter choice: ''', turtle_shapes_list, "custom")
        if user_shape in turtle_shapes_list:
            t_now().shape(user_shape)
        else:
            Command.user_tls_shape_ft()

    def user_tls_shape_ft() -> None:
        """Lets the user create custom turtle shapes"""
        user_shape: str = get_str('''
            Here are some custom options:
            cm circle, cm square, cm triangle, cm poly, cm sod (star of David)
            Enter choice: 
            ''', CUSTOM_SHAPES)
        tl.home()
        shape_made = CUSTOM_SHAPES[user_shape]()
        tl.addshape(user_shape, shape_made)
        t_now().shape(user_shape)
        tl.clear(); tl.ht()

    def list_commands() -> dict:
        """
        Creates a dictionary with all User Commands and returns it
        :return: dictionary
        """
        return class_to_dict(Command)

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
            print(f"Invalid input! Error: {exception_error}"); rest(2)

# COMMAND STORAGE: USER PROGRAM
COMMANDS: dict[str, Callable[[], None]] = {
    "fd": Command.fd_ft,
    "bk": Command.bk_ft,
    "rt": Command.rt_ft,
    "lt": Command.lt_ft,
    "create tls": Command.create_tls,
    "change tls": Command.change_tls,
    "clear": Command.clear_ft,
    "clear tls": Command.clear_tls,
    "home": Command.home_ft,
    "setpos": Command.setpos_ft,
    "move to": Command.moveto_ft,
    "set timer": Command.set_timer,
    "del timer": Command.del_timer,
    "writer": Command.writer,
    "change shape": Command.user_tls_shape,
}