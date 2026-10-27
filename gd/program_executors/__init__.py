# ⚓ Anchor for this module: [[program-executors-anchor|program_executors.__init__.py]] 

#* 📝 Imports the executor [[#turtle-runner-anchor|turtle_runner.py]] for the entire GD software
from .turtle_runner import (
    main,
    # ⚓ Link to source code: [[#main-anchor|main()]] 
    user_drawing_ft,
    # ⚓ Link to source code: [[#user-drawing-ft-anchor|user_drawing_ft()]] 
)


#* 📝 Specifies all functions available through wildcard import
__all__ = [
    "user_drawing_ft",
    "main",
]