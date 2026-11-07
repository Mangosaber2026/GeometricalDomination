# ⚓ Anchor for this module: [[six-turtles-anchor|six_turtles.py]] 
#* [Click here to see module description](./premade_designs_docs/six_turtles.md) 

import math

import turtle_extension as tx
import uf

from . import designs_decorator as designs_deco

#* 📝 The type used for a list of [[#ChainTurtle-anchor|ChainTurtle]] instances
type TurtleListType = list[tx.ChainTurtle]


# ⚓ TurtleSix anchor: [[TurtleSix-anchor|class TurtleSix]] 
#* 📝 [Click here to see class description](./premade_designs_docs/six_turtles.md) 
class TurtleSix:

      # ⚓ circles6 anchor: [[TurtleSix-circles6-anchor|circles6()]] 
      #* 📝 [Click here to see function description](./premade_designs_docs/six_turtles.md) 
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