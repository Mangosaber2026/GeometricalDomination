# ⚓ Anchor for this module: [[designs-decorator-anchor|designs_decorator.py]] 

import functools as ft

import turtle_extension as tx
import uf


# ⚓ turtles anchor: [[turtles-anchor|@turtles(amount)]] 
#* 📝 Decorator to be applied to any function which takes
#* 📝 a list of [[ChainTurtle]] and draws a design with them
def turtles(amount):

   uf.ComboValidate(amount, name="amount")(uf.int_validate(), uf.Positive())

   def decorator(func):
      @ft.wraps(func)
      def wrapper():
         
         tx.get_screen()
         tls: list[tx.ChainTurtle] = tx.tls_color(tl_num=amount)
         func(tls)
         tx.SU()

         return tls
      
      return wrapper
   
   return decorator