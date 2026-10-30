# ⚓ Anchor for this module: [[six-turtles-anchor|six_turtles.py]] 

import math

import turtle_extension as tx
import uf

from . import designs_decorator as designs_deco

#* 📝 The type used for a list of [[#ChainTurtle-anchor|ChainTurtle]] instances
type TurtleListType = list[tx.ChainTurtle]


# ⚓ TurtleSix anchor: [[TurtleSix-anchor|class TurtleSix]] 
#* 📝 Contains all drawings which require SIX turtles,
#* 📝 all functions are accessible directly through [[#Designs-anchor|Designs]] 
class TurtleSix:

      # ⚓ circles6 anchor: [[TurtleSix-circles6-anchor|circles6()]] 
      #* 📝 Draws 6 circles evenly spaced out at seemingly the same time
      @staticmethod
      @designs_deco.turtles(6)
      def circles6(tls: TurtleListType):

         radius = uf.helper.radius_float()

         step = 2 * math.pi * radius / 360         # pyright: ignore[reportOperatorIssue]

         for i, turtle in enumerate(tls):
            turtle.lt(i * 60)

         for a in range(360):
            for turtle in tls:
               turtle.fd(step).rt(1)
            tx.SU()