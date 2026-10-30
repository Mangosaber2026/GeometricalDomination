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

 #* 📝 Imports the executor functions in [[#program-executors-anchor|program_executors]] 
from .program_executors import (
 #* 📝 [[#turtle-runner-anchor|turtle_runner.py]] 
 main,
 # 🔗 Link to source code: [[#main-anchor|main()]] 
 user_drawing_ft,
 # 🔗 Link to source code: [[#user-drawing-ft-anchor|user_drawing_ft()]] 
)

#* 📝 Imports the class and dictionary in [[#user-features-anchor|user_features]] 
from .user_features import (
 #* 📝 [[#user-commands-anchor|user_commands.py]] 
 COMMANDS,
 # 🔗 Link to source code: [[#COMMANDS-anchor|dictionary COMMANDS]] 
 Command,
 # 🔗 Link to source code: [[#Command-anchor|class Command]] 
)

#* 📝 Imports the functions, decorators and dictionaries in [[#visuals-anchor|visuals]] 
from .visuals import (
 #* 📝 [[#english-alphabets-anchor|english_alphabets.py]] 
 ALPHABETS,
 # 🔗 Link to source code: [[#ALPHABETS-anchor|dictionary ALPHABETS]] 
 PATTERNS,
 # 🔗 Link to source code: [[#PATTERNS-anchor|dictionary PATTERNS]] 
 #* 📝 [[#shapes-dictionaries-anchor|shapes_dictionaries.py]] 
 SHAPES_LENGTH,
 # 🔗 Link to source code: [[#SHAPES-LENGTH-anchor|dictionary SHAPES_LENGTH]] 
 SHAPES_LENGTH_SIDES,
 # 🔗 Link to source code: [[#SHAPES-LENGTH-SIDES-anchor|dictionary SHAPES_LENGTH_SIDES]] 
 SHAPES_RADIUS,
 # 🔗 Link to source code: [[#SHAPES-RADIUS-anchor|dictionary SHAPES_RADIUS]] 
 Alphabets,
 # 🔗 Link to source code: [[#Alphabets-anchor|class Alphabets]] 
 Designs,
 # 🔗 Link to source code: [[#Designs-anchor|class Designs]] 
 #* 📝 [[#shapes-anchor|shapes.py]] 
 Shapes,
 # 🔗 Link to source code: [[#Shapes-anchor|class Shapes]] 
 #* 📝 [[#designs-anchor|designs.py]] 
 get_Patterns_dict,
 # 🔗 Link to source code: [[#get-Patterns-dict-anchor|get_Patterns_dict()]] 
 letters_functions,
 # 🔗 Link to source code: [[#letters-functions-anchor|letters_functions()]] 
 turtles,
 # 🔗 Link to source code: [[#turtles-anchor|decorator turtles(amount)]] 
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