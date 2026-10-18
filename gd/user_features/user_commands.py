from numbers import Real
from time import sleep as rest

import TurtleExtension as tx
import uf


from ..visuals import ALPHABETS

helper = uf.helper

@uf.cls_deco_superposition(staticmethod)
class Command:
    def fd_ft():
        return tx.t_now().fd(uf.get_num(float, "Enter the distance: "))

    def bk_ft():
        return tx.t_now().bk(uf.get_num(float, "Enter the distance: "))

    def rt_ft():
        return tx.t_now().rt(uf.get_num(float, "Enter an angle: "))

    def lt_ft():
        return tx.t_now().lt(uf.get_num(float, "Enter an angle: "))

    def create_tls():
        turtles, _ = tx.tls_color(entry="Enter desired number of turtles: ")
        tx.UV["tls"].extend(turtles)
        tx.UV["t"]: int = len(tx.UV["tls"]) - 1
        return turtles

    def change_tls():
        if len(tx.UV["tls"]) == 1:
            raise uf.value_error()(f"""
                Function: change_tls
                
                There is only one turtle in tx.UV["tls"]!
                Expected: multiple turtles
                Received: {tx.UV["tls"]}
                """)
        tls_change: int = uf.get_num(int, "Enter turtle number: ", MIN=1, MAX=len(tx.UV["tls"]))
        tls_num = tls_change - 1
        tx.UV["t"] = tls_num
        return tls_num

    def clear_ft():
        for t in tx.UV["tls"]: t.clear()

    def clear_tls():
        for t in tx.UV["tls"]:
            t.clear()
            t.ht()

        tx.UV["tls"].clear()
        turtles, turtle_num = tx.tls_color(entry="Enter number of new turtles: ")
        tx.UV["tls"].extend(turtles)
        tx.UV["t"]: int = turtle_num - 1
        return turtles

    def home_ft():
        return tx.t_now().home()

    def setpos_ft():
        return tx.t_now().teleport(helper.x_ft(),helper.y_ft())

    def move_to_ft():
        return tx.t_now().setpos(helper.x_ft(),helper.y_ft())

    def set_timer():
        time_delay: Real = uf.get_num(float, "Enter delay: ", MIN=0)
        tx.UV["delay"] = time_delay
        return time_delay

    def del_timer():
        tx.UV["delay"]: None = None

    def writer():
        tx.t_now().lt(90)
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
                    ALPHABETS[letter](vertical_val,tx.t_now())
                tx.SU()

    def change_shape():
        return tx.TurtleFct.change_shape(tls_num = tx.t_now())

def exec_ft():
    print("Enter exit to exit, otherwise enjoy!"); rest(2)
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

def get_Command_dict():
    return {
        name.removesuffix("_ft").replace("_", " "): obj
        for name, obj in uf.classes_to_dict(Command).items()
        if not name.startswith("_")
    }

# COMMAND STORAGE: USER PROGRAM
COMMANDS = get_Command_dict()