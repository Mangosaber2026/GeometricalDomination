# ⚓ Anchor for this module: [[english-alphabets-anchor|english_alphabets.py]] 


import uf

from . import english_letters, english_punctuations, english_shapes


# ⚓ Alphabets anchor: [[Alphabets-anchor|class Alphabets]] 
#* 📝 Class designed to draw all letters and some punctuation of the English Alphabet
class Alphabets(
    english_letters.Letters,
    english_punctuations.Punctuation,
    english_shapes.EngShapes,
    ):


    # ⚓ list_alphabets anchor: [[Alphabets-list-alphabets-anchor|list_alphabets()]] 
    #* 📝 Creates and returns a dictionary with all the available functions in [[#Alphabets-anchor|Alphabets]] 
    @classmethod
    def list_alphabets(cls):
        return uf.classes_to_dict(cls)


# ⚓ letters_functions anchor: [[letters-functions-anchor|letters_functions()]] 
#* 📝 Creates and returns a dictionary with all letters in [[#Letters-anchor|Letters]] 
def letters_functions():

    return {
        name: func
        for name, func in uf.classes_to_dict(english_letters.Letters).items()
    }


# ⚓ letters_dict anchor: [[letters-dict-anchor|dictionary letters_dict]] 
#* 📝 Letters storage created with [[#letters-functions-anchor|letters_functions()]] 
letters_dict = letters_functions()


Punctuation = english_punctuations.Punctuation
EngShapes = english_shapes.EngShapes

# ⚓ ALPHABETS anchor: [[ALPHABETS-anchor|dictionary ALPHABETS]] 
#* 📝 ALPHABETS dictionary created with 
#* 📝 [[#letters-functions-anchor|letters_functions()]] and [[#Punctuation-anchor|Punctuation]] and [[#EngShapes-anchor|EngShapes]] 
ALPHABETS = {
    **letters_dict,
    " ": Punctuation.space,
    ".": Punctuation.dot,
    "!": Punctuation.exclamation,
    "?": Punctuation.question,
    "'": Punctuation.apostrophe,
    ":": Punctuation.colon,
    ",": Punctuation.comma,
    "+": EngShapes.plus,
    "=": EngShapes.equals,
    "*": EngShapes.times,
    "-": EngShapes.minus,
    "_": EngShapes.underline,
    "<": EngShapes.heart,
    "#": EngShapes.star,
}