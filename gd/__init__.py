"""
Welcome to GeometricalDomination!!!

Developer: Miah M. Sabiq

This is a Domain-Specific API (DSAPI) with an embedded DSL made for Python 3.14.6 or later versions.

This software combines conventional Turtle drawings with an ever-increasingly complex architecture built around it,
you are permitted to use all reusable functions as you wish, but with ONE CONDITION:

The developer must be given credit for the use of their functions somewhere in the program where any external user can
easily see it.

Otherwise, hopefully you enjoy this masterpiece!
"""

#* Imports the executor functions in [[turtle_runner.py]]
from .program_executors import (

   #* [[turtle_runner.py]]
   main,               #* [[turtle_runner.py#main]]
   user_drawing_ft,    #* [[turtle_runner.py#user_drawing_ft]]
)

#* Imports the class and dictionary in [[user_commands.py]]
from .user_features import (

   #* [[user_commands.py]]
   COMMANDS,   #* [[user_commands.py]]
   Command,    #* [[Command]]
)

#* Imports the functions, decorators and dictionaries in visuals package
from .visuals import (

   # * [[alphabets.py]]
   ALPHABETS,              # * [[alphabets.py]]
   Alphabets,              # * [[Alphabets]]

   # * [[designs.py]]
   get_Patterns_dict,      # * [[designs.py#get_Patterns_dict]]
   letters_functions,      # * [[designs.py]]
   PATTERNS,               # * [[designs.py]]
   turtles,                # * [[designs.py#turtles]]
   Designs,                # * [[Designs]]

   # * [[shapes_dictionaries.py]]
   SHAPES_LENGTH,          # * [[shapes_dictionaries.py]]
   SHAPES_LENGTH_SIDES,    # * [[shapes_dictionaries.py]]
   SHAPES_RADIUS,          # * [[shapes_dictionaries.py]]

   # * [[shapes.py]]
   Shapes,                 # * [[Shapes]]

)


#* Specifies all functions, dictionaries and decorators in program_executors, user_features and visuals
__all__ = [
   "Alphabets",
   "ALPHABETS",
   "letters_functions",
   "Designs",
   "turtles",
   "get_Patterns_dict",
   "PATTERNS",
   "Shapes",
   "SHAPES_LENGTH",
   "SHAPES_RADIUS",
   "SHAPES_LENGTH_SIDES",
   "main",
   "user_drawing_ft",
   "Command",
   "COMMANDS",
]