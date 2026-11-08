# ⚓ Anchor for this module: [[self-contained-turtles-anchor|self_contained_turtles.py]] 
# [Click here to see module description](./premade_designs_docs/self_contained_turtles.md)

lazy import math

lazy import turtle_extension as tx
lazy import uf

lazy from ..premade_shapes import shapes


# ⚓ TurtleSelfMade anchor: [[TurtleSelfMade-anchor|class TurtleSelfMade]] 
#* 📝 [Click here to see class description](./premade_designs_docs/self_contained_turtles.md) 
class TurtleSelfMade:

   # ⚓ duo_triforce anchor: [[duo-triforce-anchor|duo_triforce()]] 
   #* 📝 [Click here to see function description](./premade_designs_docs/self_contained_turtles.md)
   @staticmethod
   def duo_triforce():
    
          color_list = ["red", "blue", "green", "magenta", "cyan", "yellow", "black"]
          tls = [tx.ChainTurtle().color(t) for t in color_list]
    
          tls_6 = tls[6]
    
          length = uf.helper.length_float()
    
          length_50 = uf.pct50(length)
          length_25 = uf.pct25(length)
    
          height = math.sqrt(length ** 2 - length_50 ** 2)        # pyright: ignore[reportOperatorIssue]
          height_50 = uf.pct50(height)
    
          tls[0].teleport(length_50, height).left(120)
    
          tls[1].left(120)
    
          tls[3].teleport(-length_25, height_50).left(60)           # pyright: ignore[reportArgumentType]
    
          tls[4].left(60)
    
          tls[5].left(60).teleport(length_25, height_50)
    
          for t in range(3):
             shapes.Shapes.triangle_fill(
                side = length,
                tls_num = tls[t],
             )
             shapes.Shapes.triangle_fill(
                side = length_50,
                tls_num = tls[t + 3],
             )
    
          for _ in range(3):
             shapes.Shapes.triangle(
                side = length,
                tls_num = tls_6,
             )
             tls_6.left(60).forward(length).left(60)
    
          tls_6.setpos(length_25, height_50).left(120)
          shapes.Shapes.triangle(
             side = length_50,
             tls_num = tls_6)
          
          tx.SU()
          return tls