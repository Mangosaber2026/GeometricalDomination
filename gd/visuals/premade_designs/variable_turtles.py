# ⚓ Anchor for this module: [[variable-turtles-anchor|variable_turtles.py]] 
#* [Click here to inspect the module description](./premade_designs_docs/variable_turtles.md) 

lazy import turtle_extension as tx
lazy import uf


# ⚓ TurtleToChoose anchor: [[TurtleToChoose-anchor|class TurtleToChoose]] 
#* 📝 [Click here to inspect the class description](./premade_designs_docs/variable_turtles.md) 
class TurtleToChoose:

   # ⚓ flower_infinite anchor: [[TurtleToChoose-flower-infinite-anchor|flower_infinite()]] 
   #* 📝 [Click here to inspect the function description](./premade_designs_docs/variable_turtles.md) 
   @staticmethod
   def flower_infinite():

      tls: list[tx.ChainTurtle]
      
      tls, petals_count = tx.tls_color(entry="Enter petal count: ")              # pyright: ignore[reportGeneralTypeIssues, reportAssignmentType]
      circles_num = uf.get_num(int, "Enter circles count: ", MIN=1)
      interval = uf.helper.intervals_f()
    
      angle = int(360 / petals_count)                                            # pyright: ignore[reportOperatorIssue]
    
      for i, turtle in enumerate(tls):
         turtle.left(i * angle)
    
      for a in uf.range_f(0, circles_num + 1, interval):
         for turtle in tls:
            turtle.circle(a)
    
      for turtle in tls:
         turtle.left(90).forward(circles_num * 2)
         
      tx.SU()

      return tls