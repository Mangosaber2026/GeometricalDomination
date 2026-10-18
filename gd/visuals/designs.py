from functools import wraps
from math import pi, sqrt
from typing import Final

import turtle_extension as tx
import uf

from .shapes import Shapes


def turtles(amount):

   uf.ComboValidate(amount, name="amount")(uf.int_validate(), uf.Positive())

   def decorator(func):
      @wraps(func)
      def wrapper():
         tx.get_screen()
         tls: list[tx.ChainTurtle] = tx.tls_color(tl_num=amount)
         func(tls)
         tx.SU()
         return tls
      return wrapper
   return decorator

def designs_decorator(cls):
   for name, item in vars(cls).items():
      if isinstance(item, type) and name.startswith("Turtle"):
         amount = item.TURTLE_COUNT

         for func_name, func in vars(item).items():
            if not func_name.startswith("_") and callable(func):
               setattr(item, func_name, staticmethod(turtles(amount)(func)))

      elif not name.startswith("_") and callable(item):
         setattr(item, name, staticmethod(item))

   return cls

class DesignsMeta(type):
   def __getattr__(cls, func):
      for class_name, category in vars(cls).items():
         if (
               isinstance(category, type)
               and class_name.startswith("Turtle")
         ):
            function = getattr(category, func, None)

            if callable(function):
               return function

      raise uf.attribute_error()(f"""
            Function: DesignsMeta.__getattr__
            {cls.__name__} has no attribute {func!r}
            """)

@designs_decorator
class Designs(metaclass=DesignsMeta):
   class TurtleOne:
      TURTLE_COUNT: Final = 1

      def hexaflower(tls):

         tls_0 = tls[0]

         length = uf.helper.length_float()
         flower_num = uf.helper.object_num()
         row_count = uf.helper.row_pair()

         diagonal = (length * uf.sine(120)) / uf.sine(30)
         diagonal_double = diagonal * 2
         diagonal_50 = uf.pct50(diagonal)
         height = sqrt(diagonal ** 2 - diagonal_50 ** 2)
         height_double = height * 2
         length_total = diagonal * flower_num * 2

         for _ in range(row_count):
            for row in range(2):
               for _ in range(flower_num - row):
                  Shapes.hexaflower_tri(
                     length = length,
                     tls_num = tls_0,
                  )
                  tls_0.bk_inv(diagonal_double)

               (
                  tls_0
                  . fd_inv(length_total - diagonal)
                  . lt(90)
                  . fd_inv(height_double)
                  . rt(90)
               )

      def star_of_david(tls):

         length = uf.helper.length_float()
         Shapes.SOD(
            side = length,
            tls_num = tls[0],
         )

      def diamond_pattern(tls):

         tls_0 = tls[0]

         length = uf.helper.length_float()
         diamond_num = uf.helper.object_num()
         row_count = uf.helper.row_num()

         outer_side = (length * uf.sine(120)) * 2
         outer_side_50 = uf.pct50(outer_side)
         height = sqrt(length ** 2 - outer_side_50 ** 2)
         length_and_height = length+height
         horizontal_displacement = length_and_height * 2
         total_horizontal_distance = length_and_height * diamond_num * 2

         for _ in range(row_count):
            for _ in range(diamond_num):
               Shapes.SOD(
                  side = length,
                  tls_num = tls_0,
               )
               tls_0.pu().bk(horizontal_displacement).pd()

            (
               tls_0
               . pu()
               . fd(total_horizontal_distance)
               . lt(90)
               . fd(outer_side)
               . rt(90)
            )

      def hidden_sds(tls):

         tls_0 = tls[0]

         length = uf.helper.length_float()
         star_count = uf.helper.object_num()

         for _ in range(star_count):
            Shapes.SOD(
               side = length,
               tls_num = tls_0,
            )
            length = (length * uf.sine(30)) / uf.sine(120)

      def gd_reference(tls):

         tls_0 = tls[0]

         length = uf.helper.length_float()

         diagonal = (length * uf.sine(120)) / uf.sine(30)
         tls_0.lt(30)

         for _ in range(6):
            (
               tls_0
               . begin_fill()
               . fd(diagonal)
               . lt(150)
               . fd(length)
               . rt(120)
               . bk(length)
               . end_fill()

               .fd(length)
               .lt(120)
               .fd(length)
               .rt(60)
               .bk(diagonal)
            )

      def tri_wheel(tls):

         tls_0 = tls[0]

         length = uf.helper.length_float()

         diagonal = (length*uf.sine(120))/uf.sine(30)
         tls_0.width(3)

         for _ in range(12):
            (
               tls_0
               . begin_fill()
               . fd(diagonal)
               . lt(150)
               . fd(length)
               . rt(120)
               . bk(length)
               . end_fill()

               .fd(length)
               .lt(60)
               .fd(length)
               .rt(60)
               .bk(diagonal)
            )

      def lotus_pattern(tls):

         tls_0 = tls[0]

         radius = uf.helper.radius_float()
         lotuses = uf.helper.object_num()
         rows = uf.helper.row_num()

         radius_double = radius * 2
         lotuses_and_2radius = lotuses * radius_double

         for _ in range(rows):
            for _ in range(lotuses):
               Shapes.lotus_flower(
                  radius = radius,
                  tls_num = tls_0,
               )
               tls_0.bk_inv(radius_double)

            (
               tls_0
               . fd_inv(lotuses_and_2radius)
               . lt(90)
               . fd_inv(radius_double)
               . rt(90)
            )

   class TurtleTwo:
      TURTLE_COUNT: Final = 2

      def duo_spiral(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]

         for i in range(500):
            tls_0.fd(i).rt(91)
            tls_1.fd(i).lt(91)
            tx.SU()

      def squares8(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]

         length = uf.helper.length_float()
         interval = uf.helper.intervals_f()
         diameter, diameter_half = uf.helper.diameter_sq(length)
         length_50 = uf.pct50(length)
         length1_5 = length * 1.5

         tls_0.teleport(diameter_half, diameter_half)
         tls_1.teleport(0, length_50).lt(45)

         for i, turtle in enumerate(tls):
            for _ in range(4):
               Shapes.square_fill(
                  side = length,
                  tls_num = turtle,
               )
               turtle.rt(90).fd_inv(diameter / (i + 1))

         tls_0.teleport(0, 0).seth(180)
         tls_1.teleport(0, 0).lt(90)

         for c in uf.range_f(0, length + 1, interval):
            c_half = c / 2
            tls_0.setpos(c_half, c_half)
            tls_1.setpos(sqrt(2) * c_half, 0)
            Shapes.square(
               side = c,
               tls_num = tls_0,
            )
            Shapes.square(
               side = c,
               tls_num = tls_1,
            )

         tls_0.setpos(0, 0).rt(135)
         tls_1.home()

         for turtle in tls:
            Shapes.lines(
               distance = length1_5,
               lines_num = 4,
               tls_num = turtle,
            )

      def tri_hexaflower(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]

         length = uf.helper.length_float()
         flower_num = uf.helper.object_num()
         row_count = uf.helper.row_pair()

         diagonal = (length * uf.sine(120)) / uf.sine(30)
         diagonal_50 = uf.pct50(diagonal)
         diagonal_double = diagonal * 2

         height = sqrt(diagonal ** 2 - diagonal_50 ** 2)
         height_double = height * 2

         length_total = diagonal * flower_num * 2
         length_double = length * 2

         horizontal_distance = length_total - diagonal

         for _ in range(row_count):
            for row in range(2):
               for _ in range(flower_num - row):
                  tls_1.lt(30)
                  Shapes.lines(
                     distance=length_double,
                     lines_num=6,
                     tls_num=tls_1
                  )
                  tls_1.rt(30)
                  Shapes.hexaflower_tri(
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

      def sd_pattern(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]

         length: float | int = uf.helper.length_float()
         star_num: int = uf.helper.object_num()
         row_count: int = uf.helper.row_pair()

         outer_side = (length * uf.sine(120)) / uf.sine(30)
         outer_side_50 = uf.pct50(outer_side)
         height = sqrt(length ** 2 - outer_side_50 ** 2)
         side_2 = (length * uf.sine(30)) / uf.sine(120)
         horizontal_distance = (length + height) * 2

         for _ in range(row_count):
            for row in range(1, 3):
               for _ in range(star_num):
                  Shapes.SOD_fill(
                     side = length,
                     tls_num = tls_0,
                  )
                  tls_1.lt(30)
                  Shapes.SOD_fill(
                     side = side_2,
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
                     . fd(outer_side * 1.5)
                     . rt(90)
                  )

      def sd_spiral(tls):

         length = uf.helper.length_float()
         pairs_count = uf.get_num(int, "Number of pairs of stars: ", MIN=1)
         tls[1].lt(30)

         for _ in range(pairs_count):
            for turtle in tls:
               Shapes.SOD(
                  side = length,
                  tls_num = turtle,
               )
               length = (length * uf.sine(30)) / uf.sine(120)
               turtle.lt(60)

      def sd_triflower(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]

         radius: float | int = uf.helper.radius_float()

         radius_50 = uf.pct50(radius)
         radius_double = radius * 2

         height = sqrt(radius ** 2 - radius_50 ** 2)
         height_double = height * 2

         side_c = sqrt(radius ** 2 + radius_double ** 2 + radius * 3)
         angle_b = uf.asine((radius_double * uf.sine(120)) / side_c)
         angle_a = 180 - (angle_b + 120)
         tls_0.rt(30)

         for _ in range(3):
            Shapes.hexa_flower(
               radius = radius,
               tls_num = tls_0,
            )
            tls_0.lt(60).circle(radius, 60)

         tls_1.teleport(0, -height)
         Shapes.triangle_half(
            side = radius * 5,
            tls_num = tls_1,
         )

         tls_1.teleport(0, height_double).lt(180)
         Shapes.triangle_half(
            side = radius * 4,
            tls_num = tls_1,
         )

         (
            tls_0
            . teleport(-radius_double, height_double)
            . seth(180)
            . lt(180 - (60 + angle_b))
         )

         for _ in range(3):
            (
               tls_0
               . fd(side_c)
               . lt(180 - (angle_a * 2 + 60))
               . fd(side_c)
               . lt(180 - (angle_b * 2 + 60))
            )

      def hexaflower_sd(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]

         radius: float | int = uf.helper.radius_float()
         tls_0.lt(30)

         for _ in range(6):
            Shapes.hexa_flower(
               radius = radius,
               tls_num = tls_0,
            )
            tls_0.circle(radius, 60)
            Shapes.lines(
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
         Shapes.SOD(
            side = radius * 2,
            tls_num = tls_1,
         )

   class TurtleThree:
      TURTLE_COUNT: Final = 3

      def squares10(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]
         tls_2 = tls[2]

         length = uf.helper.length_float()
         diameter, d_half = uf.helper.diameter_sq(length)
         vertical_distance = d_half + (length - d_half)

         tls_0.teleport(d_half, d_half)
         tls_1.fd_inv(vertical_distance).rt(45)

         for t in range(2):
            for _ in range(4):
               Shapes.square_fill(
                  side = length,
                  tls_num = tls[t],
               )
               tls[t].rt(90).fd_inv(diameter)

         tls_2.fd(vertical_distance).lt(135)
         Shapes.square_fill(
            side = diameter,
            tls_num = tls_2,
         )

         tls_2.teleport(d_half, d_half).lt(45)
         Shapes.square_fill(
            side = diameter,
            tls_num = tls_2,
         )

      def sd_flower(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]
         tls_2 = tls[2]

         radius = uf.helper.radius_float()
         hexa_side = (radius * uf.sine(120)) / uf.sine(30)

         tls_0.lt(30)
         Shapes.hexa_flower(
            radius = radius,
            tls_num = tls_0,
         )
         Shapes.SOD(
            side = radius,
            tls_num = tls_1,
         )
         tls_2.lt(30)
         Shapes.hexagon_ft(
            side = hexa_side,
            tls_num = tls_2,
         )

   class TurtleFour:
      TURTLE_COUNT: Final = 4

      def flower_4petals(tls):

         for i, turtle in enumerate(tls):
            turtle.lt(i * 90)

         for a in range(0, 500, 10):
            for turtle in tls:
               turtle.circle(a)

      def square4(tls):

         length = uf.helper.length_float()
         interval = uf.helper.intervals_f()

         for i, turtle in enumerate(tls):
            turtle.lt(i * 90)

         for side_length in uf.range_f(0, length + 1, interval):
            for turtle in tls:
               Shapes.square_half(
                  side = side_length,
                  tls_num = turtle,
               )

      def quadrant_square(tls):

         length = uf.get_num(float, "Enter max side length(ℚ>0): ", MIN=1)
         interval = uf.helper.intervals_f()

         for i, turtle in enumerate(tls):
            turtle.lt(i * 90)

         for side_length in uf.range_f(0, length + 1, interval):
            for turtle in tls:
               Shapes.square(
                  side = side_length,
                  tls_num = turtle,
               )

      def multi_square_grid(tls):

         tls_0 = tls[0]
         tls_1 = tls[1]
         tls_2 = tls[2]
         tls_3 = tls[3]

         length = uf.helper.length_float()

         length4 = length * 4
         x_val = (length * sqrt(2)) / 2
         tls_1.lt(180)

         for i in range(1, 5, 3):
            tls_0.teleport(x_val * i, 0).lt(135)
            Shapes.square(
               side = length * i,
               tls_num = tls_0,
            )
            tls_0.home_inv()

         for a in range(1, 3):
            coordinate = x_val * a
            tls_1.teleport(coordinate, coordinate)
            Shapes.square(
               side = ((length * 2) * a) / sqrt(2),
               tls_num = tls_1,
            )

         x_val4 = x_val * 4
         Shapes.lines(
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
               . fd(length4)
               . bk(length4)
               . lt(90)
            )

         tls_3.pu().fd(length).rt(90).pd()

         for _ in range(3):
            (
               tls_3
               . fd_inv(length)
               . rt(90)
               . fd(length4)
               . bk(length4)
               . lt(90)
            )

   class TurtleSix:
      TURTLE_COUNT: Final = 6

      def circles6(tls):

         radius = uf.helper.radius_float()

         step = 2 * pi * radius / 360

         for i, turtle in enumerate(tls):
            turtle.lt(i * 60)

         for a in range(360):
            for turtle in tls:
               turtle.fd(step).rt(1)
            tx.SU()

   def duo_triforce():

      color_list = ["red", "blue", "green", "magenta", "cyan", "yellow", "black"]
      tls = [tx.ChainTurtle().color(t) for t in color_list]

      tls_6 = tls[6]

      length = uf.helper.length_float()

      length_50 = uf.pct50(length)
      length_25 = uf.pct25(length)

      height = sqrt(length ** 2 - length_50 ** 2)
      height_50 = uf.pct50(height)

      tls[0].teleport(length_50, height).lt(120)

      tls[1].lt(120)

      tls[3].teleport(-length_25, height_50).lt(60)

      tls[4].lt(60)

      tls[5].lt(60).teleport(length_25, height_50)

      for t in range(3):
         Shapes.triangle_fill(
            side = length,
            tls_num = tls[t],
         )
         Shapes.triangle_fill(
            side = length_50,
            tls_num = tls[t + 3],
         )

      for _ in range(3):
         Shapes.triangle_ft(
            side = length,
            tls_num = tls_6,
         )
         tls_6.lt(60).fd(length).lt(60)

      tls_6.setpos(length_25, height_50).lt(120)
      Shapes.triangle_ft(
         side = length_50,
         tls_num = tls_6)
      tx.SU()
      return tls

   def flower_infinite():

      tls, petals_count = tx.tls_color(entry="Enter petal count: ")
      circles_num = uf.get_num(int, "Enter circles count: ", MIN=1)
      interval = uf.helper.intervals_f()

      angle = int(360 / petals_count)

      for i, turtle in enumerate(tls):
         turtle.lt(i * angle)

      for a in uf.range_f(0, circles_num + 1, interval):
         for turtle in tls:
            turtle.circle(a)

      for turtle in tls:
         turtle.lt(90).fd(circles_num * 2)
      tx.SU()
      return tls

   def change_shape():
      tx.TurtleFct.change_shape()

   @classmethod
   def _list_designs(cls):

      dictionary = {}

      for name, item in vars(cls).items():

         if name.startswith("Turtle") and isinstance(item, type):
            dictionary.update(uf.classes_to_dict(item))

         elif callable(item):
            dictionary[name] = item

      return dictionary

def get_Patterns_dict():
   return {
      name.replace("_", " "): func
      for name, func in Designs._list_designs().items()
      if not name.startswith("_")
   }

# DICTIONARY: ALL COMMANDS OF MAIN MENU
PATTERNS = get_Patterns_dict()