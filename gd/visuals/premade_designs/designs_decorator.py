# ⚓ Anchor for this module: [[designs-decorator-anchor|designs_decorator.py]] 
#* 📝 [Click here to see module description](./premade_designs_docs/designs_decorator.md) 

import functools as ft

import turtle_extension as tx
import uf


# ⚓ turtles anchor: [[turtles-anchor|@turtles(amount)]] 
#* 📝 [Click here to see function description](./premade_designs_docs/designs_decorator.md:10) 
def turtles(amount):

   uf.ComboValidate(amount, name="amount")(uf.int_validate(), uf.Positive())

   def decorator(func):
      @ft.wraps(func)
      def wrapper():
         
         tx.get_screen()
         tls: list[tx.ChainTurtle] = tx.tls_color(tl_num=amount)              # pyright: ignore[reportAssignmentType]
         func(tls)
         tx.SU()

         return tls
      
      return wrapper
   
   return decorator