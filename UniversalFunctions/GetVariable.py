from time import sleep as rest
from typing import overload


@overload
def get_num(TYPE: type[int], entry: str, **options) -> int: ...

@overload
def get_num(TYPE: type[float], entry: str, **options) -> float: ...

def get_num(TYPE: type[float]|type[int], entry: str, **options) -> float|int:
    """
    Gets a real numerical value from the user

    :param TYPE: float or int;  which type of value to check for
    :param entry: str; input string
    :param options: MAX, MIN, STORE
    :return: float or int
    """
    if TYPE not in (int, float):
        raise TypeError("TYPE must be type float or int")

    elif not isinstance(entry, str):
        raise TypeError("entry must be a string")

    if "MIN" in options:
        if not isinstance(options["MIN"], (float, int)):
            raise TypeError("MIN must be type float or int")

    if "MAX" in options:
        if not isinstance(options["MAX"], (float, int)):
            raise TypeError("MAX must be type float or int")

    if "MIN" in options and "MAX" in options:
        if options["MIN"] >= options["MAX"]:
            raise ValueError("MIN has to be less than MAX!")

    if "store" in options:
        if not isinstance(options["store"], (float, int, type(None))):
            raise TypeError("store must be type float or int or None!")
        if not isinstance(options["store"], (TYPE, type(None))):
            raise TypeError(f"store must be type {TYPE} or None!")

    if (
        "store" in options
        and "MIN" in options
        and "MAX" in options
        and options["store"] is not None
        and (options["MIN"] > options["store"] or options["MAX"] < options["store"])
    ):
        raise ValueError("Stored value must be between MIN and MAX!")
    #if "store" and "MIN" and "MAX" in options and options["MIN"] > options["store"] or options["store"] > options["MAX"]:
    #    raise ValueError("stored value in store must be: min <= store <= max!")

    while True:
        try:
            if "store" in options:
                reserve: str = input(entry)
                if reserve == "ans":
                    if options["store"] is not None and isinstance(options["store"], (float,int)):
                        value: float|int = options["store"]
                    else:
                        print("\nThere is no value stored yet!")
                        continue
                else:
                    value: float|int = TYPE(reserve)
            else:
                value: float|int = TYPE(input(entry))
            if "MIN" in options and "MAX" in options and (value < options["MIN"] or value > options["MAX"]):
                if TYPE == int:
                    print(f"INTEGER must be between {options['MIN']} and {options['MAX']}!")
                elif TYPE == float:
                    print(f"RATIONAL NUMBER must be between {options['MIN']} and {options['MAX']}!")
                rest(1.5); continue
            elif "MIN" in options and value < options["MIN"]:
                if TYPE == int:
                    print(f"Enter INTEGER > {options['MIN']}!")
                elif TYPE == float:
                    print(f"Enter RATIONAL NUMBER > {options['MIN']}!")
                rest(1.5); continue
            elif "MAX" in options and value > options['MAX']:
                if TYPE == int:
                    print(f"Enter INTEGER < {options['MAX']}!")
                elif TYPE == float:
                    print(f"Enter RATIONAL NUMBER < {options['MAX']}!")
                rest(1.5); continue
            elif "store" in options:
                options["store"] = value
            return value
        except ValueError:
            if TYPE == int:
                print(f"Enter INTEGER!")
            elif TYPE == float:
                print("Enter RATIONAL NUMBER!")
            rest(1.5)