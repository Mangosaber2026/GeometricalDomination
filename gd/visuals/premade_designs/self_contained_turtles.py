# ⚓ Anchor for this module: [[self-contained-turtles-anchor|self_contained_turtles.py]] 

import math

import turtle_extension as tx
import uf

from ..premade_shapes import shapes


# ⚓ TurtleSelfMade anchor: [[TurtleSelfMade-anchor|class TurtleSelfMade]] 
#* 📝 Containes functions which create their own turtles for their designs
#* 📝 All functions here are accessible directly through [[#Designs-anchor|Designs]] 
class TurtleSelfMade:

   # ⚓ duo_triforce anchor: [[duo-triforce-anchor|duo_triforce()]] 
   #* 📝 Draws and colors a triforce in a triforce with the corresponding colors
   #* 📝 Reference: Zelda
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
    
          tls[0].teleport(length_50, height).lt(120)
    
          tls[1].lt(120)
    
          tls[3].teleport(-length_25, height_50).lt(60)           # pyright: ignore[reportArgumentType]
    
          tls[4].lt(60)
    
          tls[5].lt(60).teleport(length_25, height_50)
    
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
             tls_6.lt(60).fd(length).lt(60)
    
          tls_6.setpos(length_25, height_50).lt(120)
          shapes.Shapes.triangle(
             side = length_50,
             tls_num = tls_6)
          tx.SU()
          return tls