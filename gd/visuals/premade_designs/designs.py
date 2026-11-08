# ⚓ Anchor for this module: [[designs-anchor|designs.py]] 
#* 📝 [Click here to see module description](./premade_designs_docs/designs.md) 

lazy import turtle_extension as tx
lazy import uf

lazy from . import (
   four_turtles,
   one_turtle,
   self_contained_turtles,
   six_turtles,
   three_turtles,
   two_turtles,
   variable_turtles,
)


# ⚓ Designs anchor: [[Designs-anchor|class Designs]] 
#* 📝 [Click here to see class description](./premade_designs_docs/designs.md) 
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
   #* 📝 [Click here to see function description](./premade_designs_docs/designs.md)
   @staticmethod
   def change_shape():
      tx.TurtleFct.change_shape()

   # ⚓ list_designs anchor: [[Designs-list-designs-anchor|list_designs()]] 
   #* 📝 [Click here to see function description](./premade_designs_docs/designs.md) 
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
#* 📝 [Click here to see function description](./premade_designs_docs/designs.md) 
def get_Patterns_dict():
   return {
      name.replace("_", " "): func
      for name, func in Designs.list_designs().items()
   }