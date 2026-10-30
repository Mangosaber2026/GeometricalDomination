# ⚓ Anchor for this module: [[functions-grapher-anchor|functions_grapher.py]] 

import numbers as num
import typing as tp

import numpy as np
import turtle_extension as tx
import uf

import gd


#* 📝 Parent class for all mathematical functions:
#* 📝 [[#LinearFct-anchor|class LinearFct]] 
#* 📝 [[#SineWave-anchor|class SineWave]] 
#* 📝 [[#CosineWave-anchor|class CosineWave]] 
#* 📝 [[#AbsoluteX-anchor|class AbsoluteX]] 
#* 📝 [[#QuadraticFct-anchor|class QuadraticFct]] 
# ⚓ Drawing anchor: [[Drawing-anchor|class Drawing]] 
class Drawing:

    # ⚓ __init__ anchor: [[Drawing-__init__-anchor|__init__()]] 
    #* 📝 Makes all child classes take a domain for the function
    def __init__(self, domain):

        uf.SequenceValidate(num.Real, num.Real, int)(value=domain, name="domain")
        self.domain = domain
        self.start, self.end, self.steps = self.domain

    def x_val(self):
        return np.linspace(
            self.start,
            self.end,
            self.steps+1).tolist()


    # ⚓ render anchor: [[Drawing-render-anchor|render()]] 
    #* 📝 Renders the generated coordinates from a function
    @staticmethod
    def render(coordinates):

        name: tp.Final = "coordinates"
        uf.TypeValidate(expected=tuple)(value=coordinates, name=name)
        uf.SequenceValidate(
                list, list,
                callable_items=(uf.SequenceValidate(num.Real, ...),)
                )(value=coordinates, name=name)

        tx.get_screen()
        xval, yval = coordinates
        turtle = tx.tls_color(tl_num=2)                                 # pyright: ignore[reportAssignmentType]
        turtle: list[tx.ChainTurtle]
        tls_0 = turtle[0]

        gd.Shapes.lines(
            distance = 700,
            lines_num = 4,
            tls_num = turtle[1]
        )
        for x, y in zip(xval, yval):
            tls_0.setpos(x, y)

        tx.SU()
        tx.mainloop()


    # ⚓ draw anchor: [[Drawing-draw-anchor|draw()]] 
    #* 📝 Generates the coordinates and feeds them to [[#Drawing-render-anchor|render()]] 
    def draw(self):

        self.render(self.generate())                                    # pyright: ignore[reportAttributeAccessIssue]


# ⚓ LinearFct anchor: [[LinearFct-anchor|class LinearFct]] 
#* 📝 Generates the coordinates for a Linear Function
#* 📝 Parent class: [[#Drawing-anchor|class Drawing]] 
class LinearFct(Drawing):

    def __init__(self, domain, k, d):

        super().__init__(domain)
        uf.TypeValidate(expected=num.Real)(value=k, name="k")
        uf.TypeValidate(expected=num.Real)(value=d, name="d")
        self.k, self.d = k, d

    def generate(self):

        x_val = self.x_val()
        y_val = [self.k * x + self.d for x in x_val]
        return x_val, y_val


# ⚓ SineWave anchor: [[SineWave-anchor|class SineWave]] 
#* 📝 Generates the coordinates of a sine function
#* 📝 Parent class: [[#Drawing-anchor|class Drawing]] 
class SineWave(Drawing):

    def generate(self):

        x_val = self.x_val()
        y_val = [100 * uf.sine(x) for x in x_val]
        return x_val, y_val


# ⚓ CosineWave anchor: [[CosineWave-anchor|class CosineWave]] 
#* 📝 Generates the coordinates of a cosine function
#* 📝 Parent class: [[#Drawing-anchor|class Drawing]] 
class CosineWave(Drawing):

    def generate(self):

        x_val = self.x_val()
        y_val = [100 * uf.cosine(x) for x in x_val]
        return x_val, y_val


# ⚓ AbsoluteX anchor: [[AbsoluteX-anchor|class AbsoluteX]] 
#* 📝 Generates the coordinates of the function y = |x|
#* 📝 Parent class: [[#Drawing-anchor|class Drawing]] 
class AbsoluteX(Drawing):

    def generate(self):

        x_val = self.x_val()
        y_val = [100 * abs(x) for x in x_val]
        return x_val, y_val


# ⚓ QuadraticFct anchor: [[QuadraticFct-anchor|class QuadraticFct]] 
#* 📝 Generates the coordinates of a quadratic function
#* 📝 Parent class: [[#Drawing-anchor|class Drawing]] 
class QuadraticFct(Drawing):

    def __init__(
        self, domain, a, b, c):

        super().__init__(domain)
        uf.SequenceValidate(num.Real, ...)(value=(a, b, c), name="variables")
        self.a, self.b, self.c = a, b, c

    def generate(self):

        x_val = self.x_val()
        y_val = [(self.a*x**2) + (self.b*x) + self.c for x in x_val]
        return x_val, y_val