# ⚓ Anchor for this module: [[english-alphabets-anchor|english_alphabets.py]] 


import uf

from . import english_letters, english_punctuations, english_shapes


# ⚓ Alphabets anchor: [[EngAlphabets-anchor|class EngAlphabets]] 
#* 📝 Class designed to draw all letters and some punctuation of the English Alphabet
class EngAlphabets(
    english_letters.EngLetters,
    english_punctuations.EngPunctuation,
    english_shapes.EngShapes
    ):


    # ⚓ list_alphabets anchor: [[Alphabets-list-alphabets-anchor|list_alphabets()]] 
    #* 📝 Creates and returns a dictionary with all the available functions in [[#EngAlphabets-anchor|EngAlphabets]] 
    @staticmethod
    def list_alphabets():
        return uf.classes_to_dict(
            EngAlphabets,
            english_letters.EngLetters,
            english_punctuations.EngPunctuation,
            english_shapes.EngShapes
            )


# ⚓ letters_functions anchor: [[letters-functions-anchor|letters_functions()]] 
#* 📝 Creates and returns a dictionary with all letters in [[#EngLetters-anchor|EngLetters]] 
def letters_functions():

    return {
        name: func
        for name, func in uf.classes_to_dict(english_letters.EngLetters).items()
    }


# ⚓ letters_dict anchor: [[letters-dict-anchor|dictionary letters_dict]] 
#* 📝 Letters storage created with [[#letters-functions-anchor|letters_functions()]] 
eng_letters_dict = letters_functions()


Punctuation = english_punctuations.EngPunctuation
EngShapes = english_shapes.EngShapes

# ⚓ ALPHABETS anchor: [[ENG_ALPHABETS-anchor|dictionary ENG_ALPHABETS]] 
#* 📝 ALPHABETS dictionary created with 
#* 📝 [[#letters-functions-anchor|letters_functions()]] and [[#Punctuation-anchor|Punctuation]] and [[#EngShapes-anchor|EngShapes]] 
ENG_ALPHABETS = {
    **eng_letters_dict,
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