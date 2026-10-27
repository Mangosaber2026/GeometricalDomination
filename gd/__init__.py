# ⚓ Anchor for this module: [[gd-anchor|gd.__init__.py]] 

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

 #* 📝 Imports the executor functions in [[program_executors]]
from .program_executors import (

    #* 📝 [[turtle_runner.py]]
   main,                
   # ⚓ Link to source code: [[#]]
   user_drawing_ft,    
   # ⚓ Link to source code: [[#]]
)

 #* 📝 Imports the class and dictionary in [[user_commands.py]]
from .user_features import (

    #* 📝 [[user_commands.py]]
   COMMANDS,    
   # ⚓ Link to source code: [[#]]
   Command,     
   # ⚓ Link to source code: [[#]]
)

 #* 📝 Imports the functions, decorators and dictionaries in visuals package
from .visuals import (

   # * [[alphabets.py]]
   ALPHABETS,              
   # ⚓ Link to source code: [[#]]
   Alphabets,              
   # ⚓ Link to source code: [[#]]

   # * [[designs.py]]
   get_Patterns_dict,      
   # ⚓ Link to source code: [[#]]
   letters_functions,     
   # ⚓ Link to source code: [[#]]
   PATTERNS,               
   # ⚓ Link to source code: [[#]]
   turtles,                
   # ⚓ Link to source code: [[#]]
   Designs,                
   # ⚓ Link to source code: [[#]]

   # * [[shapes_dictionaries.py]]
   SHAPES_LENGTH,         
   # ⚓ Link to source code: [[#]]
   SHAPES_LENGTH_SIDES,   
   # ⚓ Link to source code: [[#]]
   SHAPES_RADIUS,         
   # ⚓ Link to source code: [[#]]

   # * [[shapes.py]]
   Shapes,                 
   # ⚓ Link to source code: [[#]]

)


 #* 📝 Specifies all functions, dictionaries and decorators in program_executors, user_features and visuals
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