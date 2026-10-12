from .GlobalVariables import (
    UV,
    t_now,
    t_shape,
)

from .GlobalFunctions import (
    get_screen,
    SU,
    mainloop,
    tls_color,
    reset_tls,
)

from .CustomTurtleShapes import (
    UserShape,
    get_UserShape_dict,
    CUSTOM_SHAPES,
)

from .TurtleFunctions import (
TurtleFct,
)

__all__ = [
    "UV",
    "t_now",
    "t_shape",

    "get_screen",
    "SU",
    "mainloop",
    "tls_color",
    "reset_tls",

    "UserShape",
    "get_UserShape_dict",
    "CUSTOM_SHAPES",

    "TurtleFct",
]