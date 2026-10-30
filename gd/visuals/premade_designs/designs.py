# ⚓ Anchor for this module: [[designs-anchor|designs.py]] 

import turtle_extension as tx  # noqa: I001
import uf

from . import (
   one_turtle,
   two_turtles, 
   three_turtles, 
   four_turtles,
   six_turtles,
   self_contained_turtles,
   variable_turtles,
)


# ⚓ Designs anchor: [[Designs-anchor|class Designs]]
#* 📝 Contains all premade drawing functions made by the developer
class Designs(
   one_turtle.TurtleOne,
   two_turtles.TurtleTwo,
   three_turtles.TurtleThree,
   four_turtles.TurtleFour,
   six_turtles.TurtleSix,
   self_contained_turtles.TurtleSelfMade,
   variable_turtles.TurtleToChoose
):

   # ⚓ change_shape anchor: [[Designs-change-shape-anchor|change_shape()]] 
   #* 📝 Changes the shape of future turtles through [[#TurtleFct-change-shape|change_shape()]] 
   @staticmethod
   def change_shape():
      tx.TurtleFct.change_shape()

   # ⚓ list_designs anchor: [[Designs-list-designs-anchor|list_designs()]] 
   #* 📝 Creates and returns a dictionary containing all available functions in [[Designs]]
   #* 📝 with the help of [[classes_to_dictionary.py#classes_to_dict]]
   @staticmethod
   def list_designs():

      return uf.classes_to_dict(
         Designs,
         one_turtle.TurtleOne,
         two_turtles.TurtleTwo,
         three_turtles.TurtleThree,
         four_turtles.TurtleFour,
         six_turtles.TurtleSix,
         self_contained_turtles.TurtleSelfMade,
         variable_turtles.TurtleToChoose
         )


# ⚓ get_Patterns_dict anchor: [[get-Patterns-dict-anchor|get_Patterns_dict()]] 
#* 📝 Creates and returns a dictionary of [[#Designs-anchor|Designs]] 
#* 📝 mapping its human readable function names with the actual function
def get_Patterns_dict():
    return {
        name.replace("_", " "): func
        for name, func in Designs.list_designs().items()
    }


# ⚓ PATTERNS anchor: [[PATTERNS-anchor|dictionary PATTERNS]] 
#* 📝 Designs dictionary storage with [[#get-Patterns-dict-anchor|get_Patterns_dict()]] 
PATTERNS = get_Patterns_dict()