# UV = UNIVERSAL VARIABLES
UV = {
    "delay": None,            # Delay for user_drawing_ft()
      "t": 0,                   # user_drawing_ft's current turtle
      "tls": [],                # user_drawing_ft's turtle list
      "tls_shape": "arrow",     # user_drawing_ft's turtle's current shape
      "shape_library": [],      # user_drawing_ft's turtle shapes list
}
def t_now():
    return UV["tls"][UV["t"]]

def t_shape():
    return UV["tls_shape"]

