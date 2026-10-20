#* Imports the class, dictionary and functions available in user features section [[user_commands.py]]
from .user_commands import (
    COMMANDS,
    Command,
    exec_ft,
    get_Command_dict,
)


#* Specifies all functions, dictionaries and classes available through wildcard import
__all__ = [
    "Command",
    "get_Command_dict",
    "COMMANDS",
    "exec_ft",
]