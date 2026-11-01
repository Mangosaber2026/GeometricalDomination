# ⚓ Anchor for this module: [[four-turtles-anchor|four_turtles.py]] 

import math

import turtle_extension as tx
import uf

from ..premade_shapes import shapes
from . import designs_decorator as designs_deco

#* 📝 The type used for a list of [[#ChainTurtle-anchor|ChainTurtle]] instances
type TurtleListType = list[tx.ChainTurtle]


# ⚓ TurtleFour anchor: [[TurtleFour-anchor|class TurtleFour]] 
#* 📝 [Click here to see class description](./premade_designs_docs/four_turtles.md)
class TurtleFour:

      # ⚓ flower_4petals anchor: [[TurtleFour-flower-4petals|flower_4petals()]] 
      #* 📝 [Click here to see function description](./premade_designs_docs/four_turtles.md)
      @staticmethod
      @designs_deco.turtles(4)
      def flower_4petals(tls: TurtleListType):

         for i, turtle in enumerate(tls):
            turtle.lt(i * 90)

         for a in range(0, 500, 10):
            for turtle in tls:
               turtle.circle(a)


      # ⚓ square4 anchor: [[TurtleFour-square4-anchor|square4()]] 
      #* 📝 [Click here to see function description](./premade_designs_docs/four_turtles.md) 
      @staticmethod
      @designs_deco.turtles(4)
      def square4(tls: TurtleListType):

         length = uf.helper.length_float()
         interval = uf.helper.intervals_f()

         for i, turtle in enumerate(tls):
            turtle.lt(i * 90)

         for side_length in uf.range_f(interval, length + 1, interval):           # pyright: ignore[reportArgumentType]
            for turtle in tls:
               shapes.Shapes.square_half(
                  side = side_length,
                  tls_num = turtle,
               )


      # ⚓ quadrant_square anchor: [[TurtleFour-quadrant-square-anchor|quadrant_square()]] 
      #* 📝 [Click here to see function description](./premade_designs_docs/four_turtles.md) 
      @staticmethod
      @designs_deco.turtles(4)
      def quadrant_square(tls: TurtleListType):

         length = uf.get_num(float, "Enter max side length(ℚ>0): ", MIN=1)
         interval = uf.helper.intervals_f()

         for i, turtle in enumerate(tls):
            turtle.lt(i * 90)

         for side_length in uf.range_f(interval, length + 1, interval):
            for turtle in tls:
               shapes.Shapes.square(
                  side = side_length,
                  tls_num = turtle,
               )


      # ⚓ multi_square_grid anchor: [[TurtleFour-multi-square-grid-anchor|multi_square_grid()]] 
      #* 📝 [Click here to see function description](./premade_designs_docs/four_turtles.md) 
      @staticmethod
      @designs_deco.turtles(4)
      def multi_square_grid(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]
         tls_2 = tls[2]
         tls_3 = tls[3]

         length = uf.helper.length_float()

         length4 = length * 4
         x_val = (length * math.sqrt(2)) / 2                               # pyright: ignore[reportOperatorIssue]
         tls_1.lt(180)

         for i in range(1, 5, 3):
            tls_0.teleport(x_val * i, 0).lt(135)
            shapes.Shapes.square(
               side = length * i,                                          # pyright: ignore[reportArgumentType]
               tls_num = tls_0,
            )
            tls_0.home_inv()

         for a in range(1, 3):
            coordinate = x_val * a
            tls_1.teleport(coordinate, coordinate)
            shapes.Shapes.square(
               side = ((length * 2) * a) / math.sqrt(2),                   # pyright: ignore[reportOperatorIssue]
               tls_num = tls_1,
            )

         x_val4 = x_val * 4
         shapes.Shapes.lines(
            distance = x_val4,
            lines_num = 4,
            tls_num = tls_2,
         )
         tls_3.pu().fd(x_val4).rt(135).pd()

         for _ in range(3):
            (
               tls_3
               . fd_inv(length)
               . rt(90)
               . fd(length4)                                               # pyright: ignore[reportArgumentType]
               . bk(length4)                                               # pyright: ignore[reportArgumentType]
               . lt(90)
            )

         tls_3.pu().fd(length).rt(90).pd()

         for _ in range(3):
            (
               tls_3
               . fd_inv(length)
               . rt(90)
               . fd(length4)                                               # pyright: ignore[reportArgumentType]
               . bk(length4)                                               # pyright: ignore[reportArgumentType]
               . lt(90)
            )