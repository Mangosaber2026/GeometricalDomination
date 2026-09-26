from time import sleep as rest
from typing import overload
from .Validators.FctInputValidators import validate
from .TypingVariables import Real


@overload
def get_num(TYPE: type[int], entry: str, **options) -> int: ...

@overload
def get_num(TYPE: type[float], entry: str, **options) -> float: ...

def get_num(TYPE: type[float]|type[int], entry: str, **options) -> Real:
    """
    Gets a real numerical value from the user

    :param TYPE: float or int;  which type of value to check for
    :param entry: str; input string
    :param options: MAX, MIN, store
    :return: float or int
    """
    if TYPE not in (int, float):
        raise TypeError("TYPE must be type float or int")

    validate(entry, str, "entry")

    if "MIN" in options:
        validate(options["MIN"], Real, "MIN")

    if "MAX" in options:
        validate(options["MAX"], Real, "MAX")

    if "MIN" in options and "MAX" in options:
        if options["MIN"] >= options["MAX"]:
            raise ValueError("MIN has to be less than MAX!")

    if "store" in options:
        validate(options["store"], (Real, type(None)), "store")

    if (
        "store" in options
        and "MIN" in options
        and "MAX" in options
        and options["store"] is not None
        and (options["MIN"] > options["store"] or options["MAX"] < options["store"])
    ):
        raise ValueError("Stored value must be between MIN and MAX!")

    while True:
        try:
            if "store" in options:
                reserve: str = input(entry)
                if reserve == "ans":
                    if isinstance(options["store"], Real):
                        value: Real = options["store"]
                    else:
                        print("\nThere is no value stored yet!")
                        continue
                else:
                    value: Real = TYPE(reserve)
            else:
                value: Real = TYPE(input(entry))
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