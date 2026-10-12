from .TurtleSkeleton import tl
from numbers import Real
import UF as uf


helper = uf.helper

@uf.cls_deco_superposition(staticmethod)
class UserShape:
    def custom_circle():
        radius: Real = uf.get_num(float, "Enter the radius: ")
        tl.begin_poly()
        tl.circle(radius)
        tl.end_poly()
        return tl.get_poly()

    def custom_square():
        length: Real = helper.length_float()
        tl.begin_poly()

        for _ in range(4):
            tl.fd(length)
            tl.lt(90)

        tl.end_poly()
        return tl.get_poly()

    def custom_triangle():
        length: Real = helper.length_float()
        tl.begin_poly()

        for _ in range(3):
            tl.fd(length)
            tl.lt(120)

        tl.end_poly()
        return tl.get_poly()

    def custom_poly():
        length: Real = helper.length_float()
        sides: int = helper.sides_num()

        radius = length / (2 * uf.sine(180 / sides))
        angle_to_right = (180 - (180 * (sides - 2)) / sides) / 2
        tl.begin_poly()

        tl.rt(angle_to_right)
        tl.circle(radius, 360, sides)
        tl.lt(angle_to_right)

        tl.end_poly()
        return tl.get_poly()

    def custom_SOD():
        side: Real = helper.length_float()
        tl.begin_poly()

        for _ in range(6):
            tl.pu(); tl.fd(side); tl.pd(); tl.rt(60)
            for _ in range(3):
                tl.fd(side); tl.rt(120)
            tl.lt(60); tl.pu(); tl.bk(side); tl.pd(); tl.lt(60)

        tl.end_poly()
        return tl.get_poly()

    @classmethod
    def _list_shapes(cls):
        return uf.classes_to_dict(cls)

def get_UserShape_dict():
    return {
        f"cm {name.removeprefix('custom_')}": func
        for name, func in UserShape._list_shapes().items()
        if not name.startswith("_")
    }

CUSTOM_SHAPES = get_UserShape_dict()