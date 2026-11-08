# ⚓ Anchor for this module: [[shapes-dictionaries-anchor|shapes_dictionaries.py]] 


# ⚓ import_shapes anchor: [[import-shapes-anchor|import_shapes()]] 
#* 📝 Imports the [[#shapes-anchor|shapes.py]] module and returns the [[#Shapes-anchor|class Shapes]] 
def import_shapes():
    from . import shapes
    return shapes.Shapes


# ⚓ shapes_length_dict anchor: [[shapes-length-dict-anchor|shapes_length_dict()]] 
#* 📝 Creates and returns a dictionary mapping all [[#Shapes-anchor|Shapes]] 
#* 📝 functions which require length and turtle as parameters
def shapes_length_dict():
    Shapes_cls = import_shapes()

    return {
        "tri": Shapes_cls.triangle,
        "tri fill": Shapes_cls.triangle_fill,
        "tri half": Shapes_cls.triangle_half,
        "square": Shapes_cls.square,
        "square fill": Shapes_cls.square_fill,
        "square half": Shapes_cls.square_half,
        "hexagon": Shapes_cls.hexagon,
        "sod": Shapes_cls.SOD,
        "sod fill": Shapes_cls.SOD_fill,
        "flower tri": Shapes_cls.hexaflower_tri,
        "triangle": Shapes_cls.triangle,
    }


# ⚓ shapes_length_sides_dict anchor: [[shapes-length-sides-dict-anchor|shapes_length_sides_dict()]] 
#* 📝 Creates and returns a dictionary mapping all [[#Shapes-anchor|Shapes]] 
#* 📝 functions which require length, sides and tls_num as parameters
def shapes_length_sides_dict():
    Shapes_cls = import_shapes()

    return {
        "poly": Shapes_cls.polygon,
        "poly fill": Shapes_cls.polygon_fill,
    }


# ⚓ shapes_radius_dict anchor: [[shapes-radius-dict-anchor|shapes_radius_dict()]] 
#* 📝 Creates and returns a dictionary mappint all [[#Shapes-anchor|Shapes]] 
#* 📝 functions which require radius and tls_num as parameters
def shapes_radius_dict():
    Shapes_cls = import_shapes()

    return {
        "circle": Shapes_cls.circle,
        "circle fill": Shapes_cls.circle_filler,
        "hexa flower": Shapes_cls.hexa_flower,
        "lotus": Shapes_cls.lotus_flower,
    }