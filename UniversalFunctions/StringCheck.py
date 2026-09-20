from time import sleep as rest


def get_str(str_input: str, *check_values: str|dict|list|tuple) -> str:
    """
    Checks whether the input string matches the allowed values (*check_values)
    :param str_input: input string
    :param check_values: allowed string values (all lowercase), options: str, dict, list, tuple
    """
    if not isinstance(str_input, str):
        raise TypeError("str_input must be a string")

    while True:
        value: str = input(str_input).lower()
        for check in check_values:
            if not isinstance(check, (str, dict, list, tuple)):
                raise TypeError("check_values must be a string, dict, list, or tuple")
            if isinstance(check, str) and check == value:
                return value
            elif isinstance(check, (dict, list, tuple)) and value in check:
                return value
        print("Enter something VALID!")
        rest(1.5)