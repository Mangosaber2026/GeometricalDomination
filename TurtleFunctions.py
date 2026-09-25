from .CustomTurtleShapes import CUSTOM_SHAPES
from .TurtleSkeleton import tl, ChainTurtle
from .UniversalFunctions.StringCheck import get_str
from .GlobalVariables import UV
from .UniversalFunctions.FctInputValidators import validation_deco

def turtlefct_deco(decorator):
    def wrapper(func):
        return decorator(validation_deco(func))
    return wrapper

class TurtleFct:
    @turtlefct_deco(classmethod)
    def change_shape(cls, tls_num: None|ChainTurtle = None) -> None:
        """Lets the user choose different turtles shapes, including a custom option"""
        turtle_shapes_list: list[str] = tl.getshapes()
        user_shape: str = get_str(f'''
            Here are the options for the turtle shape:
            {turtle_shapes_list}
            custom -> custom turtle shapes
            Enter choice: ''', turtle_shapes_list, "custom")
        if user_shape in turtle_shapes_list:
            if isinstance(tls_num, ChainTurtle):
                tls_num.shape(user_shape)
            else:
                UV["tls_shape"] = user_shape
        else:
            if isinstance(tls_num, ChainTurtle):
                cls._user_tls_shape_ft(tls_num)
            else:
                cls._user_tls_shape_ft()

    @turtlefct_deco(staticmethod)
    def _user_tls_shape_ft(tls_num: None|ChainTurtle = None) -> None:
        """Lets the user create custom turtle shapes"""
        user_shape: str = get_str(f'''
            Here are some custom options:
            {CUSTOM_SHAPES.keys()}
            Enter choice: 
            ''', CUSTOM_SHAPES)
        tl.home()
        shape_made = CUSTOM_SHAPES[user_shape]()
        tl.addshape(user_shape, shape_made)
        if isinstance(tls_num, ChainTurtle):
            tls_num.shape(user_shape)
        else:
            UV["tls_shape"] = user_shape
        tl.clear(); tl.ht()