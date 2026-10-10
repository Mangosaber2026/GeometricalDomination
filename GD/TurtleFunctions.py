"""
This module contains the class TurtleFct which lets the user change the turtle shape to a customized one.
"""

from .CustomTurtleShapes import CUSTOM_SHAPES
from .TurtleSkeleton import tl, ChainTurtle
from .GlobalVariables import UV
import UF as uf


class TurtleFct:
    @classmethod
    def change_shape(cls, tls_num: ChainTurtle|None = None) -> ChainTurtle | str:
        """
        Lets the user choose different turtles shapes, including a custom option
        :param tls_num: None|ChainTurtle
        :return: None
        """
        if tls_num is not None:
            uf.TypeValidate(ChainTurtle)(tls_num, name="tls_num")

        turtle_shapes_list: list[str] = tl.getshapes()

        user_shape: str = uf.get_str(f'''
            Here are the options for the turtle shape:
            {turtle_shapes_list}
            custom -> custom turtle shapes
            Enter choice: ''', turtle_shapes_list, "custom")

        if user_shape in turtle_shapes_list:
            if tls_num is not None:
                tls_num.shape(user_shape)
                return tls_num
            else:
                UV["tls_shape"] = user_shape
                return user_shape
        else:
            if tls_num is not None:
                return cls._user_tls_shape_ft(tls_num)
            else:
                return cls._user_tls_shape_ft()

    @staticmethod
    def _user_tls_shape_ft(tls_num: ChainTurtle|None = None) -> ChainTurtle | str:
        """
        Lets the user create custom turtle shapes
        :param tls_num: None|ChainTurtle
        :return: None
        """
        if tls_num is not None:
            uf.TypeValidate(ChainTurtle)(tls_num, name="tls_num")

        user_shape: str = uf.get_str(f'''
            Here are some custom options:
            {CUSTOM_SHAPES.keys()}
            Enter choice: 
            ''', CUSTOM_SHAPES)
        tl.home()
        shape_made = CUSTOM_SHAPES[user_shape]()
        tl.addshape(user_shape, shape_made)
        tl.clear()
        tl.ht()

        if tls_num is not None:
            tls_num.shape(user_shape)
            return tls_num
        else:
            UV["tls_shape"] = user_shape
            return user_shape