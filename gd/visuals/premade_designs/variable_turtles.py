# ⚓ Anchor for this module: [[variable-turtles-anchor|variable_turtles.py]] 

import turtle_extension as tx
import uf


# ⚓ TurtleToChoose anchor: [[TurtleToChoose-anchor|class TurtleToChoose]] 
#* 📝 Contains premade drawing functions which require the user
#* 📝 to choose a number of turtles. All functions here are accessible through [[#Designs-anchor|Designs]] 
class TurtleToChoose:

   # ⚓ flower_infinite anchor: [[TurtleToChoose-flower-infinite-anchor|flower_infinite()]] 
   #* 📝 Draws an arbitrary number of petals with
   #* 📝 an arbitrary number of circles
   @staticmethod
   def flower_infinite():

      tls: list[tx.ChainTurtle]
      
      tls, petals_count = tx.tls_color(entry="Enter petal count: ")     # pyright: ignore[reportGeneralTypeIssues, reportAssignmentType]
      circles_num = uf.get_num(int, "Enter circles count: ", MIN=1)
      interval = uf.helper.intervals_f()
    
      angle = int(360 / petals_count)                                   # pyright: ignore[reportOperatorIssue]
    
      for i, turtle in enumerate(tls):
         turtle.lt(i * angle)
    
      for a in uf.range_f(0, circles_num + 1, interval):
         for turtle in tls:
            turtle.circle(a)
    
      for turtle in tls:
         turtle.lt(90).fd(circles_num * 2)
         
      tx.SU()

      return tls