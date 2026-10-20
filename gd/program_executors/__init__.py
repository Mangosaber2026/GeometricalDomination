#* Imports the executor [[turtle_runner.py]] for the entire GD software
from .turtle_runner import (
    main,
    user_drawing_ft,
)


#* Specifies all functions available through wildcard import
__all__ = [
    "user_drawing_ft",
    "main",
]