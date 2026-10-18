from numbers import Real
from typing import Final

import numpy as np
import TurtleExtension as tx
import uf

from gd.visuals.shapes import Shapes


class Drawing:

    def __init__(self, domain):

        uf.SequenceValidate(Real, Real, int)(domain, name="domain")
        self.domain = domain
        self.start, self.end, self.steps = self.domain

    def x_val(self):
        return np.linspace(
            self.start,
            self.end,
            self.steps+1).tolist()

    @staticmethod
    def render(coordinates):

        name: Final = "coordinates"
        uf.TypeValidate(tuple)(coordinates, name)
        uf.SequenceValidate(
                list, list,
                callable_items=(uf.SequenceValidate(Real, ...),)
                )(coordinates, name)

        tx.get_screen()
        xval, yval = coordinates
        turtle = tx.tls_color(tl_num=2)
        tls_0 = turtle[0]

        Shapes.lines(
            distance = 700,
            lines_num = 4,
            tls_num = turtle[1]
        )
        for x, y in zip(xval, yval):
            tls_0.setpos(x, y)

        tx.SU()
        tx.mainloop()

    def draw(self):

        self.render(self.generate())

class LinearFct(Drawing):

    def __init__(self, domain, k, d):

        super().__init__(domain)
        uf.TypeValidate(Real)(k, name="k")
        uf.TypeValidate(Real)(d, name="d")
        self.k, self.d = k, d

    def generate(self):

        x_val = self.x_val()
        y_val = [self.k * x + self.d for x in x_val]
        return x_val, y_val

class SineWave(Drawing):

    def generate(self):

        x_val = self.x_val()
        y_val = [100 * uf.sine(x) for x in x_val]
        return x_val, y_val

class CosineWave(Drawing):

    def generate(self):

        x_val = self.x_val()
        y_val = [100 * uf.cosine(x) for x in x_val]
        return x_val, y_val

class AbsoluteX(Drawing):

    def generate(self):

        x_val = self.x_val()
        y_val = [100 * abs(x) for x in x_val]
        return x_val, y_val

class QuadraticFct(Drawing):

    def __init__(
        self, domain, a, b, c):

        super().__init__(domain)
        uf.SequenceValidate(Real, ...)((a, b, c), name="variables")
        self.a, self.b, self.c = a, b, c

    def generate(self):

        x_val = self.x_val()
        y_val = [(self.a*x**2) + (self.b*x) + self.c for x in x_val]
        return x_val, y_val