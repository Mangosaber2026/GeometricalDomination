# ⚓ Anchor for this module: [[english-alphabets-validators-anchor|english_alphabets_validators.py]] 

import functools as ft
import numbers as num

import turtle_extension as tx
import uf


# ⚓ alphabets_validate anchor: [[alphabets-validate-anchor|alphabets_validate()]] 
#* 📝 Validates the inputs of the functions of [[#EngAlphabets-anchor|EngAlphabets]] 
def alphabets_validate(height, tls):

    uf.ComboValidate(height, name="height")(uf.real_validate(), uf.Positive())

    uf.TypeValidate(tx.ChainTurtle)(tls, name="tls")

    return height, tls


# ⚓ alphabets_deco anchor: [[alphabets-deco-anchor|alphabets_deco()]] 
#* 📝 Decorates [[#EngAlphabets-anchor|EngAlphabets]] functions and validates them through [[#alphabets-validate-anchor|alphabets_validate()]] 
def alphabets_deco(func):

    @ft.wraps(func)
    def wrapper(height: num.Real, tls: tx.ChainTurtle):

        alphabets_validate(height, tls)
        
        return func(height, tls)
    
    return wrapper