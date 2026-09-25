from time import sleep as rest
from .FctInputValidators import validate


def get_str(str_input: str, *check_values: str|dict|list|tuple) -> str:
    """
    Checks whether the input string matches the allowed values (*check_values)
    :param str_input: input string
    :param check_values: allowed string values (all lowercase), options: str, dict, list, tuple
    """
    validate(str_input, str, "str_input")

    while True:
        value: str = input(str_input).lower()
        for check in check_values:
            validate(check, (str, dict, list, tuple), "check")
            if isinstance(check, str) and check == value:
                return value
            elif isinstance(check, (dict, list, tuple)) and value in check:
                return value
        print("Enter something VALID!")
        rest(1.5)