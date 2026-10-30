# ⚓ Anchor for this module: [[three-turtles-anchor|three_turtles.py]] 

import turtle_extension as tx
import uf

from ..premade_shapes import shapes
from . import designs_decorator as designs_deco

#* 📝 The type used for a list of [[#ChainTurtle-anchor|ChainTurtle]] instances
type TurtleListType = list[tx.ChainTurtle]


# ⚓ TurtleThree anchor: [[TurtleThree-anchor|class TurtleThree]] 
#* 📝 Contains all drawings which require THREE turtles,
#* 📝 all functions are accessible directly through [[#Designs-anchor|Designs]] 
class TurtleThree:

      # ⚓ squares10 anchor: [[TurtleThree-squares10-anchor|squares10()]] 
      #* 📝 Draws 2 pairs of 4 squares with 2 overlapping square designs in the middle
      @staticmethod
      @designs_deco.turtles(3)
      def squares10(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]
         tls_2 = tls[2]

         length = uf.helper.length_float()
         diameter, d_half = uf.helper.diameter_sq(length)
         vertical_distance = d_half + (length - d_half)           # pyright: ignore[reportOperatorIssue]

         tls_0.teleport(d_half, d_half)
         tls_1.fd_inv(vertical_distance).rt(45)                   # pyright: ignore[reportArgumentType]

         for t in range(2):
            for _ in range(4):
               shapes.Shapes.square_fill(
                  side = length,
                  tls_num = tls[t],
               )
               tls[t].rt(90).fd_inv(diameter)

         tls_2.fd(vertical_distance).lt(135)                      # pyright: ignore[reportArgumentType]
         shapes.Shapes.square_fill(
            side = diameter,
            tls_num = tls_2,
         )

         tls_2.teleport(d_half, d_half).lt(45)
         shapes.Shapes.square_fill(
            side = diameter,
            tls_num = tls_2,
         )


      # ⚓ sd_flower anchor: [[TurtleThree-sd-flower-anchor|sd_flower()]] 
      #* 📝 Draws a [[#Shapes-SOD-anchor|star of david]] with a [[#Shapes-hexaflower-anchor|hexaflower]] in it
      @staticmethod
      @designs_deco.turtles(3)
      def sd_flower(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]
         tls_2 = tls[2]

         radius = uf.helper.radius_float()
         hexa_side = (radius * uf.sine(120)) / uf.sine(30)           # pyright: ignore[reportOperatorIssue]

         tls_0.lt(30)
         shapes.Shapes.hexa_flower(
            radius = radius,
            tls_num = tls_0,
         )
         shapes.Shapes.SOD(
            side = radius,
            tls_num = tls_1,
         )
         tls_2.lt(30)
         shapes.Shapes.hexagon(
            side = hexa_side,                                        # pyright: ignore[reportArgumentType]
            tls_num = tls_2,
         )