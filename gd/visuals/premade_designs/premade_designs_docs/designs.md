# Designs module

## Source Code: Designs Module

[View source code](../designs.py)

## Overview

This module contains the [Designs class](../designs.py:19), which exports all premade 
drawing functions in the package [premade_designs](../__init__.py).

## Classes


### Designs

This class exports all premade drawing functions from its parent classes:
* [TurtleOne](../one_turtle.py),
* [TurtleTwo](../two_turtles.py),
* [TurtleThree](../three_turtles.py),
* [TurtleFour](../four_turtles.py),
* [TurtleSix](../six_turtles.py),
* [TurtleToChoose](../variable_turtles.py),
* [TurtleSelfMade](../self_contained_turtles.py)

These parent classes have not been prepared to be exported to the public API, 
but they can still be imported from [designs.py](../designs.py) or the corresponding module.

#### change_shape

This function lets the user change the shape of future turtles through [TurtleFct.change_shape()](https://github.com/Mangosaber2026/TurtleExtension/blob/main/turtle_extension/foundations/turtle_functions.py).

##### Source code: change_shape

[Click here to inspect the source code of Designs.change_shape()](../designs.py)

Comment Linking: [[#Designs-change-shape-anchor|Designs.change_shape()]] 

#### list_designs

This function creates and returns a dictionary containing all available functions in [Designs](designs.md#designs) with the help of [classes_to_dict()](https://github.com/Mangosaber2026/UniversalFunctions/blob/main/uf/universal_functions/classes_to_dictionary.py).

##### Source code: list_designs

[Click here to inspect the source code of Designs.list_designs()](../designs.py)

Comment Linking: [[#classes-to-dict-anchor|classes_to_dict()]] 

#### Source Code: Designs

[Click here to inspect the source code of Designs](../designs.py)

Comment Linking: [[#Designs-anchor|class Designs]] 



## Functions

### get_Patterns_dict

This function creates a dictionary of [Designs](designs.md#designs), 
mapping its human-readable function names to their corresponding functions.

#### Source Code: get_Patterns_dict

[Click here to inspect the source code of get_Patterns_dict](../designs.py) 

Comment Linking: [[#get-Patterns-dict-anchor|get_Patterns_dict()]] 

## Dictionaries

### PATTERNS

This dictionary creates and stores a dictionary of [Designs](designs.md#designs) with
[get_Patterns_dict](designs.md#get_patterns_dict).

#### Source Code: PATTERNS

[Click here to inspect the source code of PATTERNS](../designs.py)

Comment Linking: [[#PATTERNS-anchor|dictionary PATTERNS]] 

## Source Code: Designs module

[View source code](../designs.py)