# ⚓ Anchor for this module: [[english-alphabets-anchor|english_alphabets.py]] 


lazy import uf

lazy from . import english_letters, english_punctuations, english_shapes


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


def punctuation():
    return english_punctuations.EngPunctuation

def engshapes():
    return english_shapes.EngShapes


# eng_alphabets_dict anchor: [[eng-alphabets-dict-anchor|eng_alphabets_dict()]] 
#* 📝 Creates and returns an alphabets dictionary
#* 📝 mapping [[#EngLetters-anchor|letters]], [[#EngPunctuation-anchor|punctuation]] and [[#EngShapes-anchor|shapes]] to their corresponding functions
def eng_alphabets_dict():
    return {
    **uf.classes_to_dict(english_letters.EngLetters),
    " ": punctuation().space,
    ".": punctuation().dot,
    "!": punctuation().exclamation,
    "?": punctuation().question,
    "'": punctuation().apostrophe,
    ":": punctuation().colon,
    ",": punctuation().comma,
    "+": engshapes().plus,
    "=": engshapes().equals,
    "*": engshapes().times,
    "-": engshapes().minus,
    "_": engshapes().underline,
    "<": engshapes().heart,
    "#": engshapes().star,
    }