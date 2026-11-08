# ⚓ Anchor for this module: [[three-turtles-anchor|three_turtles.py]] 
#* [Click here to see module description](./premade_designs_docs/three_turtles.md) 

lazy import turtle_extension as tx
lazy import uf

lazy from ..premade_shapes import shapes
lazy from . import designs_decorator as designs_deco

#* 📝 The type used for a list of [[#ChainTurtle-anchor|ChainTurtle]] instances
type TurtleListType = list[tx.ChainTurtle]


# ⚓ TurtleThree anchor: [[TurtleThree-anchor|class TurtleThree]] 
#* 📝 [Click here to see class description](./premade_designs_docs/three_turtles.md) 
class TurtleThree:

      # ⚓ squares10 anchor: [[TurtleThree-squares10-anchor|squares10()]] 
      #* 📝 [Click here to see function description](./premade_designs_docs/three_turtles.md) 
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
         tls_1.fd_inv(vertical_distance).right(45)                   # pyright: ignore[reportArgumentType]

         for t in range(2):
            for _ in range(4):
               shapes.Shapes.square_fill(
                  side = length,
                  tls_num = tls[t],
               )
               tls[t].right(90).fd_inv(diameter)

         tls_2.fd(vertical_distance).left(135)                      # pyright: ignore[reportArgumentType]
         shapes.Shapes.square_fill(
            side = diameter,
            tls_num = tls_2,
         )

         tls_2.teleport(d_half, d_half).left(45)
         shapes.Shapes.square_fill(
            side = diameter,
            tls_num = tls_2,
         )


      # ⚓ sd_flower anchor: [[TurtleThree-sd-flower-anchor|sd_flower()]] 
      #* 📝 [Click here to see function description](./premade_designs_docs/three_turtles.md) 
      @staticmethod
      @designs_deco.turtles(3)
      def sd_flower(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]
         tls_2 = tls[2]

         radius = uf.helper.radius_float()
         hexa_side = (radius * uf.sine(120)) / uf.sine(30)           # pyright: ignore[reportOperatorIssue]

         tls_0.left(30)
         shapes.Shapes.hexa_flower(
            radius = radius,
            tls_num = tls_0,
         )
         shapes.Shapes.SOD(
            side = radius,
            tls_num = tls_1,
         )
         tls_2.left(30)
         shapes.Shapes.hexagon(
            side = hexa_side,                                        # pyright: ignore[reportArgumentType]
            tls_num = tls_2,
         )