# ⚓ Anchor for this module: [[one-turtle-anchor|one_turtle.py]] 

import math

import turtle_extension as tx
import uf

from .. import shapes
from . import designs_decorator as designs_deco

#* 📝 The type used for a list of [[#ChainTurtle-anchor|ChainTurtle]] instances
type TurtleListType = list[tx.ChainTurtle]


# ⚓ TurtleOne anchor: [[TurtleOne-anchor|class TurtleOne]] 
#* 📝 Contains all drawings which require ONE turtle,
#* 📝 all functions are accessible directly through [[#Designs-anchor|Designs]] 
class TurtleOne:

	# ⚓ hexaflower anchor: [[TurtleOne-hexaflower-anchor|hexaflower()]] 
	#* 📝 Draws rows and collumns of hexaflowers using [[#Shapes-hexaflower-tri-anchor|hexaflower_tri()]] 
	@staticmethod
	@designs_deco.turtles(1)
	def hexaflower(tls: TurtleListType):

		tls_0 = tls[0]

		length = uf.helper.length_float()
		flower_num = uf.helper.object_num()
		row_count = uf.helper.row_pair()

		diagonal = (length * uf.sine(120)) / uf.sine(30) 			# pyright: ignore[reportOperatorIssue]
		diagonal_double = diagonal * 2								# pyright: ignore[reportOperatorIssue]
		diagonal_50 = uf.pct50(diagonal) 							# pyright: ignore[reportArgumentType]
		height = math.sqrt(diagonal ** 2 - diagonal_50 ** 2) 		# pyright: ignore[reportOperatorIssue]
		height_double = height * 2
		length_total = diagonal * flower_num * 2 					# pyright: ignore[reportOperatorIssue]

		for _ in range(row_count):
         
			for row in range(2):
            
				for _ in range(flower_num - row):
               
					shapes.Shapes.hexaflower_tri(
						length = length,
						tls_num = tls_0,
					)
					tls_0.bk_inv(diagonal_double)

				(
					tls_0
					. fd_inv(length_total - diagonal) 				# pyright: ignore[reportOperatorIssue]
					. lt(90)
					. fd_inv(height_double)
					. rt(90)
				)


	# ⚓ star_of_david anchor: [[TurtleOne-star-of-david-anchor|star_of_david()]] 
	#* 📝 Draws a star of David with [[#Shapes-SOD-anchor|SOD()]] 
	@staticmethod
	@designs_deco.turtles(1)
	def star_of_david(tls: TurtleListType):

		length = uf.helper.length_float()
		shapes.Shapes.SOD(
			side = length,
			tls_num = tls[0],
		)


	# ⚓ diamond_pattern anchor: [[TurtleOne-diamond-pattern-anchor|diamond_pattern()]] 
	#* 📝 Draws rows and columns with a diamond pattern with [[#Shapes-SOD-anchor|SOD()]] 
	@staticmethod
	@designs_deco.turtles(1)
	def diamond_pattern(tls: TurtleListType):

		tls_0 = tls[0]

		length = uf.helper.length_float()
		diamond_num = uf.helper.object_num()
		row_count = uf.helper.row_num()

		outer_side = (length * uf.sine(120)) * 2 							# pyright: ignore[reportOperatorIssue]
		outer_side_50 = uf.pct50(outer_side)
		height = math.sqrt(length ** 2 - outer_side_50 ** 2) 				# pyright: ignore[reportOperatorIssue]
		length_and_height = length+height
		horizontal_displacement = length_and_height * 2 					# pyright: ignore[reportOperatorIssue]
		total_horizontal_distance = length_and_height * diamond_num * 2 	# pyright: ignore[reportOperatorIssue]

		for _ in range(row_count):
			for _ in range(diamond_num):
				shapes.Shapes.SOD(
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


	# ⚓ hidden_sds anchor: [[TurtleOne-hidden-sds-anchor|hidden_sds()]] 
	#* 📝 Draws rotating cyclic stars of David in a star of David frame
	@staticmethod
	@designs_deco.turtles(1)
	def hidden_sds(tls: TurtleListType):

		tls_0 = tls[0]

		length = uf.helper.length_float()
		star_count = uf.helper.object_num()

		for _ in range(star_count):
			shapes.Shapes.SOD(
            side = length, 													# pyright: ignore[reportArgumentType]
            tls_num = tls_0,
         )
			length = (length * uf.sine(30)) / uf.sine(120) 					# pyright: ignore[reportOperatorIssue]


	# ⚓ gd_reference anchor: [[TurtleOne-gd-reference-anchor|gd_reference()]] 
	#* 📝 Draws an icon similar to one in the game Geometry Dash
	@staticmethod
	@designs_deco.turtles(1)
	def gd_reference(tls: TurtleListType):

		tls_0 = tls[0]

		length = uf.helper.length_float()

		diagonal = (length * uf.sine(120)) / uf.sine(30) 					# pyright: ignore[reportOperatorIssue]
		tls_0.lt(30)

		for _ in range(6):
			(
            tls_0
            . begin_fill()
            . fd(diagonal) 													# pyright: ignore[reportArgumentType]
            . lt(150)
            . fd(length)
            . rt(120)
            . bk(length)
            . end_fill()

            .fd(length)
            .lt(120)
            .fd(length)
            .rt(60)
            .bk(diagonal) 													# pyright: ignore[reportArgumentType]
         )


	# ⚓ tri_wheel anchor: [[TurtleOne-tri-wheel-anchor|tri_wheel()]] 
	#* 📝 Draws a wheel with joined filled triangles
	@staticmethod
	@designs_deco.turtles(1)
	def tri_wheel(tls: TurtleListType):

		tls_0 = tls[0]

		length = uf.helper.length_float()

		diagonal = (length * uf.sine(120)) / uf.sine(30) 					# pyright: ignore[reportOperatorIssue]
		tls_0.width(3)

		for _ in range(12):
			(
            tls_0
            . begin_fill()
            . fd(diagonal) 													# pyright: ignore[reportArgumentType]
            . lt(150)
            . fd(length)
            . rt(120)
            . bk(length)
            . end_fill()

            .fd(length)
            .lt(60)
            .fd(length)
            .rt(60)
            .bk(diagonal) 													# pyright: ignore[reportArgumentType]
         )


	# ⚓ lotus_pattern anchor: [[TurtleOne-lotus-pattern-anchor|lotus_pattern()]] 
	#* 📝 Draws a pattern similar to lotuses with [[#Shapes-lotus-flower-anchor|lotus_flower()]] 
	@staticmethod
	@designs_deco.turtles(1)
	def lotus_pattern(tls: TurtleListType):

		tls_0 = tls[0]

		radius = uf.helper.radius_float()
		lotuses = uf.helper.object_num()
		rows = uf.helper.row_num()

		radius_double = radius * 2
		lotuses_and_2radius = lotuses * radius_double 						# pyright: ignore[reportOperatorIssue]

		for _ in range(rows):
			for _ in range(lotuses):
				shapes.Shapes.lotus_flower(
               radius = radius,
               tls_num = tls_0,
            )
				tls_0.bk_inv(radius_double) 								# pyright: ignore[reportArgumentType]

			(
            tls_0
            . fd_inv(lotuses_and_2radius)
            . lt(90)
            . fd_inv(radius_double) 										# pyright: ignore[reportArgumentType]
            . rt(90)
         )