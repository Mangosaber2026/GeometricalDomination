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
lazy from .program_executors import (                          # noqa: I001
   #* 📝 [[#turtle-runner-anchor|turtle_runner.py]] 
   main,
   # 🔗 Link to source code: [[#main-anchor|main()]] 
   user_drawing_ft,
   # 🔗 Link to source code: [[#user-drawing-ft-anchor|user_drawing_ft()]] 
)

#* 📝 Imports the class and dictionary in [[#user-features-anchor|user_features]] 
lazy from .user_features import (
   #* 📝 [[#user-commands-anchor|user_commands.py]] 
   Command,
   # 🔗 Link to source code: [[#Command-anchor|class Command]] 
)

#* 📝 Imports the functions, decorators and dictionaries in [[#visuals-anchor|visuals]] 
lazy from .visuals import (
   Designs,
   # 🔗 Link to source code: [[#Designs-anchor|class Designs]] 
   EngAlphabets,
   # 🔗 Link to source code: [[#EngAlphabets-anchor|class EngAlphabets]] 
   Shapes,
   # 🔗 Link to source code: [[#Shapes-anchor|class Shapes]] 
   get_Patterns_dict,
   # 🔗 Link to source code: [[#get-Patterns-dict-anchor|get_Patterns_dict()]] 
   eng_alphabets_dict,
   # 🔗 Link to source code: [[#eng-alphabets-dict-anchor|eng_alphabets_dict()]] 
   turtles,
   # 🔗 Link to source code: [[#turtles-anchor|decorator turtles(amount)]] 
   shapes_length_dict,
   # 🔗 Link to source code: [[#shapes-length-dict-anchor|shapes_length_dict()]] 
   shapes_length_sides_dict,
   # 🔗 Link to source code: [[#shapes-length-sides-dict-anchor|shapes_length_sides_dict()]] 
   shapes_radius_dict,
   # 🔗 Link to source code: [[#shapes-radius-dict-anchor|shapes_radius_dict()]] 
)

#* 📝 Specifies all functions, dictionaries and decorators in program_executors, user_features and visuals
__all__ = [
   "EngAlphabets",
   "eng_alphabets_dict",

   "Designs",
   "turtles",
   "get_Patterns_dict",
   "Shapes",
   "shapes_length_dict",
   "shapes_length_sides_dict",
   "shapes_radius_dict",

   "main",
   "user_drawing_ft",

   "Command",
]