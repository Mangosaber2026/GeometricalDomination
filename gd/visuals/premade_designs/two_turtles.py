# ⚓ Anchor for this module: [[two-turtles-anchor|two_turtles.py]] 

import math

import turtle_extension as tx
import uf

from ..premade_shapes import shapes
from . import designs_decorator as designs_deco

#* 📝 The type used for a list of [[#ChainTurtle-anchor|ChainTurtle]] instances
type TurtleListType = list[tx.ChainTurtle]


# ⚓ TurtleTwo anchor: [[TurtleTwo-anchor|class TurtleTwo]] 
#* 📝 Contains all drawings which require TWO turtles,
#* 📝 all functions are accessible directly through [[#Designs-anchor|Designs]] 
class TurtleTwo:


      # ⚓ duo_spiral anchor: [[TurtleTwo-duo-spiral-anchor|duo_spiral()]] 
      #* 📝 Draws 2 spirals in opposite directions
      @staticmethod
      @designs_deco.turtles(2)
      def duo_spiral(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]

         for i in range(500):
            tls_0.fd(i).rt(91)
            tls_1.fd(i).lt(91)
            tx.SU()


      # ⚓ squares8 anchor: [[TurtleTwo-squares8-anchor|squares8()]] 
      #* 📝 Draws 2 pairs of 4 squares 45° tilted from each other
      #* 📝 with growing squares from the middle with axes with diagonal axes
      @staticmethod
      @designs_deco.turtles(2)
      def squares8(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]

         length = uf.helper.length_float()
         interval = uf.helper.intervals_f()
         diameter, diameter_half = uf.helper.diameter_sq(length)
         length_50 = uf.pct50(length)
         length1_5 = length * 1.5

         tls_0.teleport(diameter_half, diameter_half)
         tls_1.teleport(0, length_50).lt(45)

         for index, turtle in enumerate(tls):
            for _ in range(4):
               shapes.Shapes.square_fill(
                  side = length,
                  tls_num = turtle,
               )
               distance = diameter / (index + 1)
               turtle.rt(90).fd_inv(distance)               # pyright: ignore[reportArgumentType]

         tls_0.teleport(0, 0).seth(180)
         tls_1.teleport(0, 0).lt(90)

         for c in uf.range_f(0, length + 1, interval):      # pyright: ignore[reportArgumentType]
            c_half = c / 2
            tls_0.setpos(c_half, c_half)                    # pyright: ignore[reportArgumentType]
            tls_1.setpos(math.sqrt(2) * c_half, 0)          # pyright: ignore[reportOperatorIssue]
            shapes.Shapes.square(
               side = c,
               tls_num = tls_0,
            )
            shapes.Shapes.square(
               side = c,
               tls_num = tls_1,
            )

         tls_0.setpos(0, 0).rt(135)
         tls_1.home()

         for turtle in tls:
            shapes.Shapes.lines(
               distance = length1_5,                        # pyright: ignore[reportArgumentType]
               lines_num = 4,
               tls_num = turtle,
            )


      # ⚓ tri_hexaflower anchor: [[TurtleTwo-tri-hexaflower-anchor|tri_hexaflower()]] 
      #* 📝 Draws a triangular version of [[#Shapes-hexa-flower-anchor|hexaflower]] with [[#Shapes-hexaflower-tri-anchor|hexaflower_tri()]] 
      @staticmethod
      @designs_deco.turtles(2)
      def tri_hexaflower(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]

         length = uf.helper.length_float()
         flower_num = uf.helper.object_num()
         row_count = uf.helper.row_pair()

         diagonal = (length * uf.sine(120)) / uf.sine(30)         # pyright: ignore[reportOperatorIssue]
         diagonal_50 = uf.pct50(diagonal)                         # pyright: ignore[reportArgumentType]
         diagonal_double = diagonal * 2                           # pyright: ignore[reportOperatorIssue]

         height = math.sqrt(diagonal ** 2 - diagonal_50 ** 2)     # pyright: ignore[reportOperatorIssue]
         height_double = height * 2

         length_total = diagonal * flower_num * 2                 # pyright: ignore[reportOperatorIssue]
         length_double = length * 2

         horizontal_distance = length_total - diagonal            # pyright: ignore[reportOperatorIssue]

         for _ in range(row_count):
            for row in range(2):
               for _ in range(flower_num - row):
                  tls_1.lt(30)
                  shapes.Shapes.lines(
                     distance=length_double,                      # pyright: ignore[reportArgumentType]
                     lines_num=6,
                     tls_num=tls_1
                  )
                  tls_1.rt(30)
                  shapes.Shapes.hexaflower_tri(
                     length=length,
                     tls_num=tls_0
                  )

                  for turtle in tls:
                     turtle.bk_inv(diagonal_double)

               for turtle in tls:
                  (
                     turtle
                     . fd_inv(horizontal_distance)
                     . lt(90)
                     . fd_inv(height_double)
                     . rt(90)
                  )


      # ⚓ sd_pattern anchor: [[TurtleTwo-sd-pattern-anchor|sd_pattern()]] 
      #* 📝 Draws a pattern with rows and columns of [[#Shapes-SOD-fill-anchor|filled stars of David]] 
      @staticmethod
      @designs_deco.turtles(2)
      def sd_pattern(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]

         length = uf.helper.length_float()
         star_num = uf.helper.object_num()
         row_count = uf.helper.row_pair()

         outer_side = (length * uf.sine(120)) / uf.sine(30)       # pyright: ignore[reportOperatorIssue]
         outer_side_50 = uf.pct50(outer_side)                     # pyright: ignore[reportArgumentType]
         height = math.sqrt(length ** 2 - outer_side_50 ** 2)     # pyright: ignore[reportOperatorIssue]
         side_2 = (length * uf.sine(30)) / uf.sine(120)           # pyright: ignore[reportOperatorIssue]
         horizontal_distance = (length + height) * 2              # pyright: ignore[reportOperatorIssue]

         for _ in range(row_count):
            for row in range(1, 3):
               for _ in range(star_num):
                  shapes.Shapes.SOD_fill(
                     side = length,
                     tls_num = tls_0,
                  )
                  tls_1.lt(30)
                  shapes.Shapes.SOD_fill(
                     side = side_2,                               # pyright: ignore[reportArgumentType]
                     tls_num = tls_1,
                  )
                  tls_1.rt(30)

                  for turtle in tls:
                     turtle.pu().bk(horizontal_distance).pd()

               for turtle in tls:
                  (
                  turtle
                  . pu()
                  . fd((length + height) * (star_num * 2 + (-1) ** row))
                  . lt(90)
                  . fd(outer_side * 1.5)                          # pyright: ignore[reportOperatorIssue]
                  . rt(90)
                  )


      # ⚓ sd_spiral anchor: [[TurtleTwo-sd-spiral-anchor|sd_spiral()]] 
      #* 📝 Draws a spiraling [[#Shapes-SOD-anchor|SOD()]] with 2 turtles cycling
      @staticmethod
      @designs_deco.turtles(2)
      def sd_spiral(tls: TurtleListType):

         length = uf.helper.length_float()
         pairs_count = uf.get_num(int, "Number of pairs of stars: ", MIN=1)
         tls[1].lt(30)

         for _ in range(pairs_count):
            for turtle in tls:
               shapes.Shapes.SOD(
                  side = length,                                     # pyright: ignore[reportArgumentType]
                  tls_num = turtle,
               )
               length = (length * uf.sine(30)) / uf.sine(120)        # pyright: ignore[reportOperatorIssue]
               turtle.lt(60)


      # ⚓ sd_triflower anchor: [[TurtleTwo-sd-triflower-anchor|sd_triflower()]] 
      #* 📝 Draws a complex [[#Shapes-SOD-anchor|star of david]] with a [[#Shapes-hexa-flower-anchor|hexaflower]] in the middle
      @staticmethod
      @designs_deco.turtles(2)
      def sd_triflower(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]

         radius = uf.helper.radius_float()

         radius_50 = uf.pct50(radius)
         radius_double = radius * 2

         height = math.sqrt(radius ** 2 - radius_50 ** 2)                        # pyright: ignore[reportOperatorIssue]
         height_double = height * 2

         side_c = math.sqrt(radius ** 2 + radius_double ** 2 + radius * 3)       # pyright: ignore[reportOperatorIssue]
         angle_b = uf.asine((radius_double * uf.sine(120)) / side_c)             # pyright: ignore[reportOperatorIssue]
         angle_a = 180 - (angle_b + 120)                                         # pyright: ignore[reportOperatorIssue]
         tls_0.rt(30)

         for _ in range(3):
            shapes.Shapes.hexa_flower(
               radius = radius,
               tls_num = tls_0,
            )
            tls_0.lt(60).circle(radius, 60)

         tls_1.teleport(0, -height)
         shapes.Shapes.triangle_half(
            side = radius * 5,                                                   # pyright: ignore[reportArgumentType]
            tls_num = tls_1,
         )

         tls_1.teleport(0, height_double).lt(180)
         shapes.Shapes.triangle_half(
            side = radius * 4,                                                   # pyright: ignore[reportArgumentType]
            tls_num = tls_1,
         )

         (
            tls_0
            . teleport(-radius_double, height_double)                            # pyright: ignore[reportArgumentType]
            . seth(180)
            . lt(180 - (60 + angle_b))                                           # pyright: ignore[reportOperatorIssue]
         )

         for _ in range(3):
            (
               tls_0
               . fd(side_c)
               . lt(180 - (angle_a * 2 + 60))
               . fd(side_c)
               . lt(180 - (angle_b * 2 + 60))                                    # pyright: ignore[reportOperatorIssue]
            )


      # ⚓ hexaflower_sd anchor: [[TurtleTwo-hexaflower-sd-anchor|hexaflower_sd()]] 
      #* 📝 Draws 6 [[#Shapes-hexa-flower-anchor|hexaflowers]] in a [[#Shapes-SOD-anchor|star of david]] 
      @staticmethod
      @designs_deco.turtles(2)
      def hexaflower_sd(tls: TurtleListType):

         tls_0 = tls[0]
         tls_1 = tls[1]

         radius = uf.helper.radius_float()
         tls_0.lt(30)

         for _ in range(6):
            shapes.Shapes.hexa_flower(
               radius = radius,
               tls_num = tls_0,
            )
            tls_0.circle(radius, 60)
            shapes.Shapes.lines(
               distance = radius,
               lines_num = 6,
               tls_num = tls_1,
            )
            tls_1.lt(60).fd(radius)

         (
            tls_1
            . pu()
            . lt(90)
            . circle(radius, 60)
            . pd()
            . rt(150)
         )
         shapes.Shapes.SOD(
            side = radius * 2,         # pyright: ignore[reportArgumentType]
            tls_num = tls_1,
         )