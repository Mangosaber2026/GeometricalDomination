"""
This module contains the `turtles` decorator, which takes a function and supplies it with 
a list of ChainTurtle instances, depending on the configuration:

@turtles(3)
def some_drawing(tls: list[ChainTurtle()]):
    for item in tls:
        print(item)

In this case, some_drawing is supplied with a list of 3 ChainTurtle instances.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.


import collections.abc as cabc

import turtle_extension as tx

 #* 📝 The type used for a list of [[ChainTurtle]]
type TurtlesList = list[tx.ChainTurtle]

 #* 📝 The type used for one of [[Designs]] functions
type DesignFuncType = cabc.Callable[[TurtlesList], None]

type WrapperFuncType = cabc.Callable[[], TurtlesList]

 #* 📝 The type returned from a wrapper that wraps the [[Designs]] functions
type TurtlesReturnType = cabc.Callable[[DesignFuncType], WrapperFuncType]


def turtles(amount: int) -> TurtlesReturnType:
    """
    DECORATOR:
    Takes a given number of turtles, gets their colors from the user and executes the function.

    :param amount: number of turtles > 0

    :return: list of turtles
    """